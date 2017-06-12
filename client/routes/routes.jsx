import React, { Component } from 'react';
import { HashRouter as Router, Route, Switch } from 'react-router-dom';
import Nav from '../components/nav.jsx';
import App from '../components/app.jsx';

const Routes = () => (
  <Router>
    <div>
      <Nav />
      <Switch>
          <Route exact path="/" component={App}/>
      </Switch>
    </div>
  </Router>
);

export default Routes;
