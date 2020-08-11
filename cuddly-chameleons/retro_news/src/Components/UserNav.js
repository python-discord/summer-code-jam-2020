import React from 'react';
import { Button } from 'nes-react';
import { Nav } from 'react-bootstrap';

import axios from "../AxiosAPI";

class UserNav extends React.Component {
    render() {
        if (this.props.status) {
            const logOutAction = async (event) => {
                event.preventDefault();
                const refresh_token = localStorage.getItem('refresh_token');
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                localStorage.removeItem('username');
                this.props.handler(false);
                await axios.post('/user/logout/', {refresh_token: refresh_token});
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
