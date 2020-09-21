import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { Navbar, NavDropdown, Nav } from 'react-bootstrap'

class Navigation extends Component {


    render() {
        return (
            <Navbar expand="lg" bg="dark" variant="dark">
                <Navbar.Brand>Sauto</Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="mr-auto">
                        <Nav.Link><Link to="/" style={{ color: '#FFF' }}>Cars</Link></Nav.Link>
                        <Nav.Link><Link to="/charts" style={{ color: '#FFF' }}>Charts</Link></Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        )
    }
}

export default Navigation;