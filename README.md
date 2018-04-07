# Partner Python Tools
> Useful tools for Esri Partners built with the [ArcGIS API for Python](https://developers.arcgis.com/python/)

## About

Partners working with Esri and ArcGIS implement many common workflows. The [ArcGIS API for Python](https://developers.arcgis.com/python/) is an awesome automation library. This repo is meant to be a collection of POC scripts to automate some of these workflows.

## Prerequisites

* Install the [ArcGIS API for Python](https://developers.arcgis.com/python/) ([instructions](https://developers.arcgis.com/python/guide/install-and-set-up/))
* Access to [Jupyter Notebooks](http://jupyter.org/) (included with ArcGIS Python API __TBD?__ )

## Contents

* **[`utils/`](/utils) - Common functions that I've found helpful**
  * [`clone_utils.py`](/utils/clone_utils.py) - assist with cloning groups & items
  * [`user_utils.py`](/utils/user_utils.py) - assist with adding users
  * [`cool_utils.py`](/utils/cool_utils.py) - functions I want to remember and hopefully you will too!
* **[`common_ops/`](/common_ops) - Common operations**
  * [`add_to_definition.ipynb`](/common_ops/add_to_definition.ipynb) - updates such as _adding indexes_, _adding fields_, and more
* **[`bulk_ops/`](/bulk_ops) - Common bulk operations**
  * [`csv_upload.ipynb`](/bulk_ops/csv_upload.ipynb) - upload a folder of `csvs` & `dataframes` to [hosted feature layers](https://doc.arcgis.com/en/arcgis-online/share-maps/hosted-web-layers.htm) in your GIS
  * [`shapefile_upload.ipynb`](/bulk_ops/shapefile_upload.ipynb) - upload a folder of Shapefiles to [hosted feature layers](https://doc.arcgis.com/en/arcgis-online/share-maps/hosted-web-layers.htm) in your GIS
  * [`csv_geocode.ipynb`](/bulk_ops/csv_geocode.ipynb) - [geocode](https://developers.arcgis.com/features/geocoding/) rows in `csvs` and `dataframes`
  * ['append_data.ipynb'](/bulk_ops/append_data.ipynb) - create & append data to service from `csvs` & `dataframes`
  * [`standard_geography.ipynb`](/bulk_ops/standard_geography.ipynb) - enrich [standard geography](https://developers.arcgis.com/rest/geoenrichment/api-reference/standard-geography-query.htm) ids, such as `census blocks`, with geometries
* **[`build_org/`](/build_org) - Automate new ArcGIS Online deployments by cloning a template organization**
  * [`clone_groups.ipynb`](/build_org/clone_groups.ipynb) - clone groups and their items
  * [`configure_org.ipynb`](/build_org/configure_org.ipynb) - customize org UI & add users


## Getting Started

*See the README in each directory*

## Issues & Contributing

Want to request a new sample? Have a question? Would [__love__](https://github.com/mpayson/startup-python-tools/issues) to hear from you.

And PRs always welcome!
