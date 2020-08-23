import React, { Component } from 'react';
import { Pie } from 'react-chartjs-2';

class Chart extends Component {

    constructor(props) {
        super(props);
        this.state = {
            data: {}
        };
    }

    componentDidMount() {
        fetch('http://127.0.0.1:4996/api/cars/')
        .then(response => response.json())
        .then(cars => {
            let carName = [];
            let carAmount = [];
            cars.forEach(car => {
                carName.push(car.brand);
                carAmount.push(car.price);
            });
            this.setState({
                data: {
                    labels: ['BMW', 'Aston Martin', 'Mercedes-Benz'],
                    datasets: [{
                        data: carAmount,
                        backgroundColor: [
                        '#FF6384',
                        '#36A2EB',
                        '#FFCE56'
                        ],
                        hoverBackgroundColor: [
                        '#FF6384',
                        '#36A2EB',
                        '#FFCE56'
                        ]
                    }]
                }
            })
        });
    }

    render() {
        return (
            <React.Fragment>
                <h1>Pie!</h1>
                <div>
                    <Pie data={this.state.data} options={{ maintainAspectRatio: false }} />
                </div>
            </React.Fragment>
            
        )
    }
}

export default Chart;