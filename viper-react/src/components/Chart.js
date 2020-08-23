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
            let labels = [];
            const distinct = (value, index, self) => self.indexOf(value) === index;
            let labelsAll = cars.map(car => car.brand);
            labels = labelsAll.filter(distinct);
        
            let bmwList = cars.filter(car => car.brand === 'BMW');
            let astonMartinList = cars.filter(car => car.brand === 'Aston Martin');
            let mercedesBenzList = cars.filter(car => car.brand === 'Mercedes-Benz');
            console.log(cars);
            this.setState({
                data: {
                    labels: labels,
                    datasets: [{
                        data: [1, astonMartinList.length, bmwList.length, mercedesBenzList.length],
                        backgroundColor: [
                        '#ff6363',
                        '#ffd863',
                        '#63ffa4',
                        '#63b4ff'
                        ],
                        hoverBackgroundColor: [
                        '#ff6363',
                        '#ffd863',
                        '#63ffa4',
                        '#63b4ff'
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
                    <Pie data={this.state.data} options={{ maintainAspectRatio: false }} width={400} height={400} />
                </div>
            </React.Fragment>
            
        )
    }
}

export default Chart;