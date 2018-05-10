"""utility functions to assist with cloning groups & items"""

def search_item_title(target, title):
    """search org for an existing item with title

    args:
    target -- target GIS to search
    item -- item with title to search
    """
    s_items = target.content.search(query='title:{}'.format(title))
    for s_item in s_items:
        if s_item.title == title:
            return s_item
    return None

def search_group_title(target, title):
    """search org for an existing group with title

    args:
    target -- target GIS to search
    group -- group with title to search
    """
    s_items = target.groups.search(title)
    for s_item in s_items:
        if s_item.title == title:
            return s_item
    return None

def clone_items_modify(items, target,
                       modify_item_callback=None, modify_group_callback=None, **kwargs):
    """Clone groups and items to a target GIS
    * Abstraction over arcgis.gis.ContentManager.clone_items to:
    - Provide callbacks to update properties, sometimes shouldn't have 1:1 copy

    args:
    items -- items/groups to be cloned. specifying groups will clone groups & their items
    target -- target gis where items or groups will be cloned
    modify_item_callback -- callback to update Item properties, expects:
        args: (item_clone, target_gis)
        returns: flattened dict of args, eg {'title':'<>'; 'data':'<>'}, args here:
    https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html?highlight=clone_items#arcgis.gis.Item.update

    modify_group_callback -- callback to update Group properties, expects:
        args: (group_clone, expected_title, target_gis)
        returns: dict of args here:
    https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html?highlight=clone_items#arcgis.gis.Group.update

    **kwargs:
    all additional args described here:
    https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html?highlight=clone_items#arcgis.gis.ContentManager.clone_items
    """

    from arcgis.gis import Group
    from arcgis.gis import Item

    # clone the items
    results = target.content.clone_items(items, **kwargs)

    # update the cloned properties

    # list of all the groups
    source_groups = [item for item in items if isinstance(item, Group)]

    # update each result
    # clone_items automatically changes group name if name already exists in target
    # this requires additional logic to pass back the expected name
    for result in results:
        if isinstance(result, Item) and modify_item_callback:
            props = modify_item_callback(result, target)
            args = {}
            args['data'] = props.pop('data', None)
            args['thumbnail'] = props.pop('thumbnail', None)
            args['metadata'] = props.pop('metadata', None)
            args['item_properties'] = props
            result.update(**args)
        elif isinstance(result, Group) and modify_group_callback:
            source_tag = next(tag for tag in result.tags if 'source-' in tag)
            source_id = source_tag[7:]
            source_group = next(group for group in source_groups if group.id == source_id)
            props = modify_group_callback(result, source_group.title, target)
            result.update(**props)

    return results
