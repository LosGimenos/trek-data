import React, { Component } from 'react';
import request from 'superagent';

export default class App extends Component {
  componentDidMount() {
    console.log('component mounted!!')
    request
      .get('/trek_data/api/v1/info', (req, res) => {
        console.log(res);
      })
  }

  render() {
    return (
      <div>
         <h1>Where No Kewleez Have Gone Before!!</h1>
      </div>
    );
  }
}

