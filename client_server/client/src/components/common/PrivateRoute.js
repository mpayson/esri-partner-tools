import React from 'react';

import { Route, Redirect } from "react-router-dom";

const PrivateRoute = ({ render: render, avail: isAvail, ...rest }) => (
  <Route
    {...rest}
    render={props =>
      isAvail
      ? (render(props))
      : (
        <Redirect
          to={{
            pathname: "/",
            state: { from: props.location }
          }}
        />
      )
    }
  />
);

export default PrivateRoute;