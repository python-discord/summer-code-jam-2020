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
                    <UserNav status={this.props.status} handler={this.props.handler} />
                </Navbar.Collapse>
            </Navbar>
        );
    }
}

export default Header;
