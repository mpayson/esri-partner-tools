# Esri Partner Tools

> Useful tools for Esri Partners built with the [ArcGIS API for Python](https://developers.arcgis.com/python/)

<details>
  <summary> Contents
  </summary>

* [About](#about)
* [Prerequisites](#prerequisites)
* [Contents](#contents)
* [Getting Started](#getting-started)
* [Sample Data](#sample-data)
* [Issues and Contributing](#issues-and-contributing)

</details>

## About

Partners working with Esri and ArcGIS implement many common workflows. The [ArcGIS API for Python](https://developers.arcgis.com/python/) is an awesome automation library. This repo is meant to be a collection of POC scripts to automate some of these workflows.

While much of the code is in Jupyter Notebooks, it can easily be ported to pure python to run on the server or as headless apps. [`partnerutils/`](/partnerutils) can also be installed as a local package:
> `$ pip install -q -U git+https://github.com/mpayson/esri-partner-tools`

## Prerequisites

* Install the [ArcGIS API for Python](https://developers.arcgis.com/python/) ([instructions](https://developers.arcgis.com/python/guide/install-and-set-up/))
* Access to [Jupyter Notebooks](http://jupyter.org/)

## Contents

* **[`partnerutils/`](/partnerutils) - Functions that I've found helpful**
  * [`cool_utils.py`](/partnerutils/cool_utils.py) - functions I want to remember and hopefully you will too!
  * [`etl_utils.py`](/partnerutils/etl_utils.py) - assist with common ETL logic
  * [`user_utils.py`](/partnerutils/user_utils.py) - assist with adding users
  * [`clone_utils.py`](/partnerutils/clone_utils.py) - assist with cloning groups & items
  * [`feature_utils.py`](partnerutils/feature_utils.py) - assist with features and feature data types
* **[`common_workflows/`](/common_workflows) - Common workflows with the Python API**
  * [`csv_geocode.ipynb`](/common_workflows/csv_geocode.ipynb) - [geocode](https://developers.arcgis.com/features/geocoding/) rows in `csvs` and `dataframes`
  * [`vector_data_products.ipynb`](/common_workflows/vector_data_products.ipynb) - end-to-end workflows for managing vector content and derivative information products
  * [`distribute_items.ipynb`](/common_workflows/distribute_items.ipynb) - common patterns for distributing items to another organization
  * [`standard_geography.ipynb`](/common_workflows/standard_geography.ipynb) - enrich [standard geography](https://developers.arcgis.com/rest/geoenrichment/api-reference/standard-geography-query.htm) ids, such as `census blocks`, with geometries
* **[`feature_layers/`](/feature_layers) - Common operations with [hosted feature layers](https://doc.arcgis.com/en/arcgis-online/share-maps/hosted-web-layers.htm)**
  * [`csv_upload.ipynb`](/feature_layers/csv_upload.ipynb) - upload a folder of `csvs` & `dataframes`
  * [`shapefile_upload.ipynb`](/feature_layers/shapefile_upload.ipynb) - upload a folder of `Shapefiles`
  * [`geojson_upload.ipynb`](/feature_layers/geojson_upload.ipynb) - upload a geojson file
  * [`update_data.ipynb`](/feature_layers/update_data.ipynb) - a couple different workflows for updating uploaded / hosted data
  * [`create_views.ipynb`](/feature_layers/create_views.ipynb) - create database views with separate permissions against one authoritative layer
  * [`manage_fields.ipynb`](/feature_layers/manage_fields.ipynb) - view and edit fields
  * [`manage_indexes.ipynb`](/feature_layers/manage_indexes.ipynb) - view, edit, and refresh indexes
  * [`enable_time.ipynb`](/feature_layers/enable_time.ipynb) - add time metadata that will be reflected in ArcGIS app UIs
* **[`build_org/`](/build_org) - Automate new ArcGIS Online deployments**
  * [`clone_groups.ipynb`](/build_org/clone_groups.ipynb) - clone groups and their items
  * [`configure_org.ipynb`](/build_org/configure_org.ipynb) - customize org UI, create groups, & add users
  * [`create_share_group.ipynb`](/build_org/create_share_group.ipynb) - create a [group](https://doc.arcgis.com/en/arcgis-online/share-maps/groups.htm) and invite members to share content with your users
  * [`register_application.ipynb`](/build_org/register_application.ipynb) automatically create and [register an app](https://developers.arcgis.com/documentation/core-concepts/security-and-authentication/signing-in-arcgis-online-users/)

## Getting Started

Many samples use [`partnerutils`](/partnerutils). To use this package, either copy & paste the functions as specified in each notebook OR:

`$ pip install -q -U git+https://github.com/mpayson/esri-partner-tools`

This will install the `partnerutils` as a local package in your active environment. The utilities can then be used as follows

```python
from arcgis.gis import GIS
from partnerutils.processing_utils import batch_geocode_memo

gis = GIS(username="username", password="password")
addresses = ['El Burrito Redlands CA', '380 New York St Redlands CA']
results = batch_geocode_memo(addresses)

print(results)
```

Shout out to Ryan @ SafeGraph for showing me this is [a thing](https://github.com/SafeGraphInc/safegraph_py). Otherwise, the notebooks should give enough detail to get started. If not, **[holler](https://github.com/mpayson/esri-partner-tools/issues)**!

## Sample Data

I included some sample data for testing and trialing:
* [`NYC_Restaurant_Inspections.csv`](/sample_data/NYC_Restaurant_Inspections.csv) - a slice of DOHMH New York City Restaurant Inspection Results. [Source](https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j])
* [`sample_census_tract_geoid.csv`](/sample_data/sample_census_tract_geoid.csv) - a couple census tract geoids. Copied from [here](https://geo.nyu.edu/catalog/nyu-2451-34513)

## Issues and Contributing

Want to request a new sample? Have a question? Would [__love__](https://github.com/mpayson/esri-partner-tools/issues) to hear from you.

And PRs always welcome!
