import React from 'react';
import { BrowserRouter, Route } from "react-router-dom";
import {UserSession} from '@esri/arcgis-rest-auth';
import clientId from './config';
import App from './App.js';

const Routes = () => (
  <BrowserRouter>
    <div>
      <Route path="/" component={App}/>
      <Route path="/callback" render={(props) => {
        let session = UserSession.completeOAuth2({
          clientId: clientId
        });
        localStorage.setItem('__ARCGIS_REST_USER_SESSION__', session.serialize());
        return (
          <h1>LOADING</h1>
        )
      }}/>
    </div>
  </BrowserRouter>
)

export default Routes