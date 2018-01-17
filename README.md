# Startup Python Tools
> Useful tools for Esri Startups built with the [ArcGIS API for Python](https://developers.arcgis.com/python/)

## About

Startups working with Esri and ArcGIS implement many common workflows. The [ArcGIS API for Python](https://developers.arcgis.com/python/) is an awesome automation library. This repo is meant to be a collection of POC scripts to automate some of these workflows.

## Contents

* [`build_org/`](/build-org) - Automate new ArcGIS Online deployments by cloning a template organization
  * [`clone_groups.ipynb`](/build-org/clone_groups.ipynb) - Jupyter Notebook to clone groups and their items
  * [`configure_org.ipynb`](/build-org/configure_org.ipynb) - Jupyter Notebook to customize org UI & add users
* [`utils/`](/utils) - Common functions that I've found helpful
  * [`clone_utils.py`](/utils/clone_utils.py) - Functions to assist with cloning groups & items
  * [`user_utils.py`](/utils/user_utils.py) - Functions to assist with adding users

## Getting Started

*See the README in each directory*