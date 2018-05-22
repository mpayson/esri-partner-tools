import React, { Component } from 'react';
import {UserSession} from '@esri/arcgis-rest-auth';
import { Route, Switch, Link, Redirect } from "react-router-dom";
import PrivateRoute from './components/common/PrivateRoute';
import Gallery from './components/Gallery';
import Distribute from './components/Distribute';
import clientId from './config';
import './App.css';

class App extends Component {

  state = {
    redirectToReferrer: false,
    session: null
  }

  constructor(props, context){
    super(props, context);
    this.handleLogin = this.handleLogin.bind(this);
    this.handleLogout = this.handleLogout.bind(this);
  }

  componentWillMount(){

    const serializedSession = localStorage.getItem('__ARCGIS_REST_USER_SESSION__');
    if (serializedSession !== null && serializedSession !== "undefined") {
      let parsed = JSON.parse(serializedSession);
      parsed.tokenExpires = new Date(parsed.tokenExpires);
      this.setState({
        session: new UserSession(parsed)
      });
    }
  }

  handleLogin(evt){
    evt.preventDefault();
    const redirect_uri = window.location.origin + '/callback';
    console.log(redirect_uri)
    UserSession.beginOAuth2({
      clientId: clientId,
      redirectUri: redirect_uri,
      popup: true
    }).then(newSession => {
      this.setState({
        session: newSession
      });
      localStorage.setItem('__ARCGIS_REST_USER_SESSION__', newSession.serialize());
    }).catch(err => {
      console.log(err);
    })
  }

  handleLogout(evt){
    this.setState({
      session: null
    })
    localStorage.removeItem('__ARCGIS_REST_USER_SESSION__')
  }

  render() {

    const accountBtn = this.state.session
    ? <button className="top-nav-link icon-ui-sign-out margin-left-1" onClick={this.handleLogout}>Log Out</button>
    : <button className="top-nav-link icon-ui-user margin-left-1" onClick={this.handleLogin}>Sign In</button>
    
    const isAuth = this.state.session ? true : false;
    console.log(isAuth)
    return (
      <div>
          <header className="top-nav">
            <div className="grid-container">
              <div className="column-24">
                <Link className="top-nav-title" to="/">ArcGIS Client Server</Link>
                <nav className="class-top-nav-list right" aria-labelledby="usernav">
                  {accountBtn}
                </nav>
              </div>
            </div>
          </header>

        <Switch>
          <Route exact path="/" render={(props) => <Gallery {...props} isAuth={isAuth} onSignIn={this.handleLogin}/>}/>
          <PrivateRoute path="/register" render={(props) => <Distribute {...props} session={this.state.session}/>} avail={isAuth}/>
        </Switch>

      </div>
    );
  }
}



export default App;
