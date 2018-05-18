# ArcGIS Client Server

> Modular ArcGIS POCs with React components and Flask blueprints

## About

These POCs showcase practical and cool workflows for building applications with ArcGIS. Each POC has a corresponding React component and/or Flask blueprint. The POCs are then composed together in a [client app](/client_server/client) and a separate [server API](/client_server/server).

In addition, I've found this to be an awesome way to learn about new libraries, including [ArcGIS API for Python](https://developers.arcgis.com/python/) || [arcgis-rest-js](https://esri.github.io/arcgis-rest-js/) || [Flask](http://flask.pocoo.org/) || [React](https://reactjs.org/) || [react-router](https://github.com/ReactTraining/react-router) || [Calcite Web](https://esri.github.io/calcite-web/)... 

**NOTE** The samples opt for quick [browser-based](https://developers.arcgis.com/documentation/core-concepts/security-and-authentication/browser-based-user-logins/) login against ArcGIS Online--you'll likely have to roll in [server-based](https://developers.arcgis.com/documentation/core-concepts/security-and-authentication/security-and-usage-concerns/) login, a user-management system, etc.

## Getting Started

### Server

Make sure all the [dependencies](/environment.yml) are installed, including [partnerutils](#getting-started). Then:

`$ cd esri-partner-tools/client_server/server`

`$ FLASK_APP=hello.py flask run`

### Client

`$ cd esri-partner-tools/client_server/client`

`$ npm install`

`$ npm start`

Note, for now these connect through the create-react-app development [proxy](https://github.com/facebook/create-react-app/blob/master/packages/react-scripts/template/README.md#proxying-api-requests-in-development).

## Contents

* App [component](/client_server/client/src/App.js) - Simple OAuth 2.0 with [arcgis-rest-js](https://esri.github.io/arcgis-rest-js/),[React](https://reactjs.org/), and [react-router](https://github.com/ReactTraining/react-router) 
* Register [component](/client_server/client/src/components/Register.js) & [blueprint](/client_server/server/api/register.py) - Set up and show workflows to write to a user's GIS