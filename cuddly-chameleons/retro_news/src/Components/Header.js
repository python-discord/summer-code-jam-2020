import React from 'react';
import { Navbar } from 'react-bootstrap';

import UserNav from "./UserNav";

class Header extends React.Component {
    render() {
        return (
            <Navbar bg="light" expand="lg">
                <Navbar.Brand href="/">Retro News</Navbar.Brand>
                <Navbar.Toggle />
                <Navbar.Collapse className="justify-content-end">
                    <UserNav />
                </Navbar.Collapse>
            </Navbar>
        );
    }
}

export default Header;
