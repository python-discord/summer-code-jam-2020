import React from 'react';
import {Navbar, Nav} from 'react-bootstrap';

import UserNav from "./UserNav";
import {Button, Container} from "nes-react";
import {Link} from "react-router-dom";

class Header extends React.Component {
    render() {
        return (
            <Container>
                <Navbar bg="light" expand="lg">
                    <Navbar.Brand href="/">Retro News</Navbar.Brand>
                    <Navbar.Toggle />
                    <Navbar.Collapse className="justify-content-end">
                        <Nav className="ml-auto">
                            <Link to={"/search"} className="px-2"><Button>Search</Button></Link>
                            {localStorage.getItem('superuser') === 'true' && this.props.status ? <Link to={"/posts/new"} className="px-2"><Button type="button">Create post</Button></Link> : ""}
                            <UserNav className="px-2" status={this.props.status} handler={this.props.handler} />
                        </Nav>
                    </Navbar.Collapse>
                </Navbar>
            </Container>
        );
    }
}

export default Header;
