import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';
import Car from './components/Car'
import Chart from './components/Chart';

class App extends Component {

  render() {
    return (
      <Switch>
        <Route path="/" component={Car} exact />
        <Route path="/charts" component={Chart} exact />
      </Switch>
    )
  }
}

export default App;