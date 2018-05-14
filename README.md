# Esri Partner Tools

> Useful tools for Esri Partners built with the [ArcGIS API for Python](https://developers.arcgis.com/python/)

<details>
  <summary> Contents
  </summary>

* [About](#about)
* [Prerequisites](#prerequisites)
* [Contents](#contents)
* [Getting Started](#getting-started)
* [Issues and Contributing](#issues-and-contributing)

</details>

## About

Partners working with Esri and ArcGIS implement many common workflows. The [ArcGIS API for Python](https://developers.arcgis.com/python/) is an awesome automation library. This repo is meant to be a collection of POC scripts to automate some of these workflows. While much of the code is in Jupyter Notebooks, it can easily be ported to pure python to run on the server or as headless apps.

## Prerequisites

* Install the [ArcGIS API for Python](https://developers.arcgis.com/python/) ([instructions](https://developers.arcgis.com/python/guide/install-and-set-up/))
* Access to [Jupyter Notebooks](http://jupyter.org/)

## Contents

* **[`partnerutils/`](/partnerutils) - Functions that I've found helpful**
  * [`cool_utils.py`](/partnerutils/cool_utils.py) - functions I want to remember and hopefully you will too!
  * [`user_utils.py`](/partnerutils/user_utils.py) - assist with adding users
  * [`clone_utils.py`](/partnerutils/clone_utils.py) - assist with cloning groups & items
  * [`feature_utils.py`](partnerutils/feature_utils.py) - assist with features and feature data types
* **[`common/`](/common) - Common workflows with the Python API**
  * [`csv_geocode.ipynb`](/common/csv_geocode.ipynb) - [geocode](https://developers.arcgis.com/features/geocoding/) rows in `csvs` and `dataframes`
  * [`share_to_groups.ipynb`](/common/share_to_groups.ipynb) - share content to your users via [groups](https://doc.arcgis.com/en/arcgis-online/share-maps/groups.htm) without cloning the data
  * [`standard_geography.ipynb`](/common/standard_geography.ipynb) - enrich [standard geography](https://developers.arcgis.com/rest/geoenrichment/api-reference/standard-geography-query.htm) ids, such as `census blocks`, with geometries
* **[`feature_layers/`](/feature_layers) - Common operations with [hosted feature layers](https://doc.arcgis.com/en/arcgis-online/share-maps/hosted-web-layers.htm)**
  * [`csv_upload.ipynb`](/feature_layers/csv_upload.ipynb) - upload a folder of `csvs` & `dataframes`
  * [`shapefile_upload.ipynb`](/feature_layers/shapefile_upload.ipynb) - upload a folder of `Shapefiles`
  * [`append_data.ipynb`](/feature_layers/append_data.ipynb) - append data from `csvs` & `dataframes`
  * [`manage_fields.ipynb`](/feature_layers/manage_fields.ipynb) - view and edit fields
  * [`manage_indexes.ipynb`](/feature_layers/manage_indexes.ipynb) - view, edit, and refresh indexes
* **[`build_org/`](/build_org) - Automate new ArcGIS Online deployments**
  * [`clone_groups.ipynb`](/build_org/clone_groups.ipynb) - clone groups and their items
  * [`configure_org.ipynb`](/build_org/configure_org.ipynb) - customize org UI, create groups, & add users
  * [`create_share_group.ipynb`](/build_org/create_share_group.ipynb) - create a [group](https://doc.arcgis.com/en/arcgis-online/share-maps/groups.htm) and invite members to share content with your users

## Getting Started

Many samples use [`partnerutils`](/partnerutils). To use this package, either copy & paste the functions as specified in each notebook OR:

1. `$ git clone https://github.com/mpayson/esri-partner-tools.git`
2. `$ cd esri-partner-tools`
3. `$ pip install -e .`

This will install a [local package](https://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install). As it turns out, top-level utils are [annoying](https://stackoverflow.com/questions/34478398/import-local-function-from-a-module-housed-in-another-directory-with-relative-im) and I've been using these functions in other projects.

Otherwise, the notebooks should give enough detail to get started. If not, [holler](https://github.com/mpayson/esri-partner-tools/issues)!

## Issues and Contributing

Want to request a new sample? Have a question? Would [__love__](https://github.com/mpayson/esri-partner-tools/issues) to hear from you.

And PRs always welcome!
