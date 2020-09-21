import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';
import Car from './components/Car'
import Chart from './components/Chart';
import Navigation from './components/Navigation';
import 'bootstrap/dist/css/bootstrap.min.css';

class App extends Component {

  render() {
    return (
      <React.Fragment>
        <Navigation />
        <Switch>
          <Route path="/" component={Car} exact />
          <Route path="/charts" component={Chart} exact />
        </Switch>
      </React.Fragment>
    )
  }
}

export default App;