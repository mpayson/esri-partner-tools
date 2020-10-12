# ArcGISAddFeatures
Headless ArcGIS python script to push attribute data into an ArcGIS Online hosted data table. The script runs on a timer at a user defined interval. 

Prerequisites:
ArcGIS Online account
Hosted data table with fields 'pk', 'amount', 'datetime1'

Usage:
AddFeaturesOnTimer.py 'URL of the hosted table' 'interval (sec)' 'ID' 'Value' 'My User Name' 'My Password'
