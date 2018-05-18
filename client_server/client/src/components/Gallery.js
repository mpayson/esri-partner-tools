import React from 'react';
import { Link } from "react-router-dom";
import registerImg from '../assets/register.png';

const Gallery = ({isAuth, onSignIn}) => {
  const linkClass = isAuth ? "avenir-bold font-size-2" : "avenir-bold font-size-2 not-active link-light-gray";
  const subText = isAuth
  ? (<p className="text-white font-size-1">
      Samples built with the <a className="link-light-blue" href="https://developers.arcgis.com/python/">ArcGIS API for Python</a> and React
    </p>)
  : (<p className="text-white font-size-1">
      Samples built with the <a className="link-light-blue" href="https://developers.arcgis.com/python/">ArcGIS API for Python</a> and React. <a className="link-red" href="https://developers.arcgis.com/python/" onClick={onSignIn}>Sign in</a> to get started!
    </p>);

  return (
    <div>
      <div className="sub-nav arcgis-product-header panel-dark-blue">
        <div className="grid-container padding-leader-1">
          <div className="column-14">
            <h1 className="font-size-8 padding-leader-3 text-white">ArcGIS Client Server</h1>
            {subText}
          </div>
        </div>
      </div>

      <div className="column-19 pre-1 post-1 leader-2">
        <div className="block-group block-group-3-up">
          <div className="card block">
            <figure className="card-image-wrap">
              <img className="card-image" src={registerImg} alt="Bridge Club, 1954"/>
            </figure>
            <div className="card-content">
              <Link className={linkClass} to="/register">Register Demo</Link>
              <p className="font-size--1">Set up and show workflows to communicate with a user's GIS</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Gallery;