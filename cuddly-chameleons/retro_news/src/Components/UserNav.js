import React from 'react';
import { Button } from 'nes-react';
import { Nav } from 'react-bootstrap';

import axios from "../AxiosAPI";

class UserNav extends React.Component {
    constructor(props) {
        super(props);
        this.state = {logged_in: localStorage.getItem('access_token') && localStorage.getItem('refresh_token') && localStorage.getItem('username')};
    }

    render() {
        if (this.state.logged_in) {
            const logOutAction = async (event) => {
                event.preventDefault();
                await axios.post('/user/logout/', {refresh_token: localStorage.getItem('refresh_token')});
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                localStorage.removeItem('username');
                this.state.logged_in = false;
            };

            return (
                <Button onClick={logOutAction}>Log out</Button>
            )
        }

        return (
            <div>
                <Nav.Link href="/login">Login</Nav.Link>
                <Nav.Link href="/signup">Sign up</Nav.Link>
            </div>
        );
    }
}

export default UserNav;
