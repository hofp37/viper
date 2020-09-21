import React, { Component } from 'react';
import { Pie } from 'react-chartjs-2';

class Chart extends Component {

    constructor(props) {
        super(props);
        this.state = {
            data: {}
        };
    }

    createBrandsList = (labels, cars) => {
        let brandsList = [];
        let label;

        for (label of labels) {
            brandsList.push(cars.filter(car => car.brand === label));
        }
        return brandsList;
    }

    getBrandsListAmounts = (brandsList) => {
        let brandsListAmounts = [];
        let brand;

        for (brand of brandsList) {
            brandsListAmounts.push(brand.length);
        }
        return brandsListAmounts
    }

    dynamicColors = (labels) => {
        let colorsArray = [];

        for (let i = 0; i < labels.length; i++) {
            const r = Math.floor(Math.random() * 255);
            const g = Math.floor(Math.random() * 255);
            const b = Math.floor(Math.random() * 255);
            colorsArray.push("rgb(" + r + "," + g + "," + b + ")");
        }
        return colorsArray;
    }

    componentDidMount() {
        fetch('http://127.0.0.1:4996/api/cars/')
        .then(response => response.json())
        .then(cars => {
            let labels = [];
            const distinct = (value, index, self) => self.indexOf(value) === index;
            const labelsAll = cars.map(car => car.brand);
            labels = labelsAll.filter(distinct);
            const brandsList = this.createBrandsList(labels, cars);
            
            this.setState({
                data: {
                    labels: labelsAll.filter(distinct),
                    datasets: [{
                        data: this.getBrandsListAmounts(brandsList),
                        backgroundColor: this.dynamicColors(labels)
                    }]
                }
            })
        });
    }

    render() {
        return (
            <React.Fragment>
                <br/>
                <h1>Pie!</h1>
                <div>
                    <Pie data={this.state.data} options={{ maintainAspectRatio: false }} width={400} height={400} />
                </div>
            </React.Fragment>
            
        )
    }
}

export default Chart;