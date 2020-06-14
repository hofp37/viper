import React, { Component } from 'react';
import Cars from './components/cars';

class App extends Component {
  
  state = {
    cars: []
  }

  async componentDidMount() {
    const response = await fetch('http://127.0.0.1:4996/api/cars/');
    const json = await response.json();
    this.setState({ cars: json})
  }
  
  render() {
    return (
      <Cars cars={this.state.cars} />
    );
  }
}

export default App;