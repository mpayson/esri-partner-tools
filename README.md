# Partner Python Tools
> Useful tools for Esri Partners built with the [ArcGIS API for Python](https://developers.arcgis.com/python/)

## About

Partners working with Esri and ArcGIS implement many common workflows. The [ArcGIS API for Python](https://developers.arcgis.com/python/) is an awesome automation library. This repo is meant to be a collection of POC scripts to automate some of these workflows.

## Prerequisites

* Install the [ArcGIS API for Python](https://developers.arcgis.com/python/) ([instructions](https://developers.arcgis.com/python/guide/install-and-set-up/))
* Access to [Jupyter Notebooks](http://jupyter.org/) (included with ArcGIS Python API __TBD?__ )

## Contents

* [`utils/`](/utils) - Common functions that I've found helpful
  * [`clone_utils.py`](/utils/clone_utils.py) - Functions to assist with cloning groups & items
  * [`user_utils.py`](/utils/user_utils.py) - Functions to assist with adding users
  * [`cool_utils.py`](/utils/cool_utils.py) - Functions that I want to remember and hopefully you will too!
* [`build_org/`](/build_org) - Automate new ArcGIS Online deployments by cloning a template organization
  * [`clone_groups.ipynb`](/build_org/clone_groups.ipynb) - Jupyter Notebook to clone groups and their items
  * [`configure_org.ipynb`](/build_org/configure_org.ipynb) - Jupyter Notebook to customize org UI & add users
* [`bulk_ops/`](/bulk_ops) - Common bulk operations
  * [`bulk_csv_upload.ipynb`](/bulk_ops/bulk_csv_upload.ipynb) - Jupyter Notebook to upload a folder of `csv`s to [hosted feature layers](https://doc.arcgis.com/en/arcgis-online/share-maps/hosted-web-layers.htm) in your GIS
  * [`bulk_csv_geocode.ipynb`](/bulk_ops/bulk_csv_geocode.ipynb) - Jupyter Notebook to [geocode](https://developers.arcgis.com/features/geocoding/) rows in a `csv` file
  * [`bulk_shapefile_upload.ipynb`](/bulk_ops/bulk_shapefile_upload.ipynb) - Jupyter Notebook to upload a folder of Shapefiles to [hosted feature layers](https://doc.arcgis.com/en/arcgis-online/share-maps/hosted-web-layers.htm) in your GIS
  * [`bulk_standard_geography.ipynb`](/bulk_ops/bulk_standard_geography.ipynb) - Jupyter Notebook to enrich [standard geography](https://developers.arcgis.com/rest/geoenrichment/api-reference/standard-geography-query.htm) ids, such as `census block group ids
  `, with their geometries


## Getting Started

*See the README in each directory*

## Issues & Contributing

Want to request a new sample? Have a question? Would [__love__](https://github.com/mpayson/startup-python-tools/issues) to hear from you.

And PRs always welcome!
