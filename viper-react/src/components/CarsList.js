import React from 'react'
import { withStyles, makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const StyledTableCell = withStyles((theme) => ({
    head: {
        backgroundColor: theme.palette.common.black,
        color: theme.palette.common.white,
    },
    body: {
        fontSize: 14,
    },
}))(TableCell);

const StyledTableRow = withStyles((theme) => ({
    root: {
        '&:nth-of-type(odd)': {
            backgroundColor: theme.palette.action.hover,
        },
    },
}))(TableRow);

const useStyles = makeStyles({
    table: {
        minWidth: 700,
        width: '70%'
    },
});

const CarsList = ({ cars }) => {
    const classes = useStyles();

    return (
        <React.Fragment>
        <TableContainer component={Paper}>
            <Table className={classes.table} size="small" aria-label="customized table" align='center'>
                <TableHead>
                    <TableRow>
                        <StyledTableCell>#</StyledTableCell>
                        <StyledTableCell align="left">Brand</StyledTableCell>
                        <StyledTableCell align="left">Model</StyledTableCell>
                        <StyledTableCell align="left">Price</StyledTableCell>
                        <StyledTableCell align="left">Mileage</StyledTableCell>
                        <StyledTableCell align="left">Year&nbsp;Manufactured</StyledTableCell>
                        <StyledTableCell align="left">Snaptime</StyledTableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {cars.map((car, i) => (
                        <StyledTableRow key={i}>
                            <StyledTableCell component="th" scope="row">
                                {car.car_id}
                            </StyledTableCell>
                            <StyledTableCell align="left">{car.brand}</StyledTableCell>
                            <StyledTableCell align="left">{car.model}</StyledTableCell>
                            <StyledTableCell align="left">{car.price}</StyledTableCell>
                            <StyledTableCell align="left">{car.mileage}</StyledTableCell>
                            <StyledTableCell align="left">{car.year_manufactured}</StyledTableCell>
                            <StyledTableCell align="left">{car.snaptime}</StyledTableCell>
                        </StyledTableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
        </React.Fragment>
    );
}

export default CarsList;