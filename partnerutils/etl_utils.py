"""********************************************
* A couple ETL utility functions for working with ArcGIS
********************************************"""
import tempfile
import json
import datetime

DEFAULT_TITLE = 'GeoJSON Utils POC'
DEFAULT_TAG = 'geojson-utils-poc'

def date_to_ags(date):
    """Returns an ArcGIS-formatted date from a Python date object
    
    args:
    date - Python date object"""
    tz = datetime.timezone.utc
    return date.astimezone(tz).strftime('%m/%d/%Y %H:%M:%S')

def timestamp_to_ags(timestamp):
    """Returns an ArcGIS-formatted date from a timestamp
    
    args:
    timestamp -- timestamp in milliseconds since epoch"""
    seconds = timestamp / 1000
    date = datetime.datetime.fromtimestamp(seconds)
    return date_to_ags(date)

def _add_unique_index(layer, field):
    """Adds a unique index for upsert operations to update, or avoid duplicating, existing rows

    args:
    layer -- where to add the index
    field -- the field to index
    """
    new_index = {
        "name": "External UID",
        "fields": field,
        "isUnique": True,
        "description": "External UID for upsert operations"
    }
    add_dict = {"indexes" : [new_index]}
    return layer.manager.add_to_definition(add_dict)

def add_geojson(gis, geojson, **item_options):
    """Uploads geojson and returns the file item
    
    args:
    gis -- gis object where item is added
    geojson -- geojson object to upload as file
    item_options -- additional item properties, see here:
    https://developers.arcgis.com/python/api-reference/arcgis.gis.toc.html#arcgis.gis.ContentManager.add"""

    # get default args
    title = item_options.pop('title', DEFAULT_TITLE)
    tags = item_options.pop('tags', DEFAULT_TAG)
        
    # save geojson to tempfile and add as item
    with tempfile.NamedTemporaryFile(mode="w", suffix='.json') as fp:
        fp.write(json.dumps(geojson))
        item = gis.content.add({
            **item_options,
            'type': 'GeoJson',
            'title': title,
            'tags': tags,
        }, data=fp.name)
    
    return item

def append_to_layer(gis, layer, geojson, uid_field=None):
    """Appends geojson to an existing service and returns the results

    Note, this is the best approach for bulk updates in ArcGIS Online.
    There are other options here, such as transactional edits
    > https://github.com/mpayson/esri-partner-tools/blob/master/feature_layers/update_data.ipynb
    
    args:
    gis -- gis object where the layers live
    layer -- FeatureLayer to be updated
    geojson -- geojson object to add to the layer
    uid_field -- identifies existing features to update with new features (must be uniquely indexed)
    """

    item = add_geojson(gis, geojson, title="Dataminr update")
    result = None

    try:
        # if there's a uid_field make sure it's indexed before append
        indexes = layer.properties.indexes
        if uid_field and not any(i['fields'] == uid_field for i in indexes):
            _add_unique_index(layer, uid_field)

        result = layer.append(
            item_id=item.id,
            upload_format="geojson",
            upsert=(uid_field != None),
            upsert_matching_field=uid_field # update existing features with matching uid_fields
        )
    finally:
        item.delete() # if not deleted next run will eror and pollute ArcGIS

    return result

def create_layer(gis, geojson, template_item):
    """Publishes geojson as a hosted service based on an existing template item
    and returns the resulting layer item
    
    args:
    gis -- gis where the layer should live
    geojson -- initial geojson to populate the layer
    template_item -- existing Item that has been pre-configured with desired properties"""

    results = gis.content.clone_items([template_item], copy_data=False)
    item = results[0]
    lyr = item.layers[0]

    append_to_layer(gis, lyr, geojson)

    return item

def create_scratch_layer(gis, geojson, uid_field=None, **item_options):
    """Publishes geojson as a hosted service and returns the layer item

    Note, use this to quickly add geojson with system default properties. In production,
    it's easier to set desired properties on a template layer then use create_layer.
    
    args:
    gis -- gis where the layer should live
    geojson -- initial geojson to populate the layer
    uid_field -- global uid field that can be used to determine existing features on updates
    item_options -- additional item properties, see here:
    https://developers.arcgis.com/python/api-reference/arcgis.gis.toc.html#arcgis.gis.ContentManager.add"""

    item = add_geojson(gis, geojson, **item_options)
    try:
        lyr_item = item.publish()
    finally:
        item.delete()
    
    # add a unique index for upsert operations so don't duplicate rows
    if uid_field:
        lyr = lyr_item.layers[0]
        _add_unique_index(lyr, uid_field)
  
    return lyr_item

def get_existing_item(gis, tags=None):
    """Searches for an existing layer item and returns it
    
    Note, for now this just assumes there's just one layer item for the tags
    
    args:
    gis -- gis to search
    tags -- tags to search for layers within the gis"""
    t = tags if tags else DEFAULT_TAG
    search_items = gis.content.search('tags:"{0}" AND type:"Feature Service"'.format(t))
    
    return search_items[0] if len(search_items) > 0 else None

def delete_before(lyr, date, field):
    """Deletes all features in a layer before a given date

    args:
    lyr -- the feature layer with features to delete
    date -- the date before which to delete features
    field -- the date field"""
    where = "{0} < '{1}'".format(field, date_to_ags(date))
    return lyr.delete_features(where=where)

def delete_before_days(lyr, number_days, field):
    """Deletes all features with dates before the specified
    number of days back from today

    args:
    lyr -- the feature layer with features to delete
    number_days -- the number of days back before which to delete features
    field -- the date field
    """
    dt = datetime.datetime.today() - datetime.timedelta(number_days)
    return delete_before(lyr, dt, field)
