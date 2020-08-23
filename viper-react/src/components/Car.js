import React, { Component } from 'react';
import CarsList from './CarsList';
import SearchBox from '../SearchBox';
import loader from '../assets/loader.gif';

class Car extends Component {

  async componentDidMount() {
    fetch('http://127.0.0.1:4996/api/cars/')
      .then(response => response.json())
      .then(cars => {this.setState({ cars: cars})});
  }

  constructor() {
    super();
    this.state = {
      cars: [],
      searchfield: ''
    }
  }

  onSearchChange = (event) => {
    this.setState({ searchfield: event.target.value })
  }
  
  render() {
    const filteredCars = this.state.cars.filter(car => {
      return car.model.toLowerCase().includes(this.state.searchfield.toLowerCase());
    })

    if (this.state.cars.length === 0) {
      return (
        <div className="tc">
        <img src={loader} alt="loading"/>
        </div>
      )
    } else {
      return (
        <React.Fragment>
          <center><h1>Cars</h1></center>
          <SearchBox searchChange={this.onSearchChange} />
          <CarsList cars={filteredCars} />
        </React.Fragment>
      );
    }
  }
}

export default Car;