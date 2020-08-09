import React from 'react';
import { Container, TextInput, Button } from 'nes-react';

import axios from '../AxiosAPI';

class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {username: "", password: "", logging_in: false, invalid: false};
        document.title = "Retro News - Login";

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({invalid: false});
        this.setState({[event.target.name]: event.target.value});
    }

    async handleSubmit(event) {
        event.preventDefault();
        this.setState({ logging_in: true })

        try {
            const response = await axios.post('/token/obtain/', {
                username: this.state.username,
                password: this.state.password,
            });

            axios.defaults.headers['Authorization'] = "JWT " + response.data.access;
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            localStorage.setItem('username', this.state.username);
            localStorage.setItem('superuser', response.data.superuser === true ? 'true' : 'false');

            this.setState({logging_in: false});
            this.setState({username: "", password: ""});
            this.props.handler(true);
            return response.data;
        } catch (e) {
            this.setState({invalid: true, logging_in: false});
        }
    }

    render() {
        if (this.state.logging_in) {
            return (
                <Container>
                    Logging in...
                </Container>
            );
        }

        if (localStorage.getItem('access_token') && localStorage.getItem('refresh_token')) {
            return (
                <Container>
                    Logged in as {localStorage.getItem('username')}{localStorage.getItem('superuser') === 'true' ? " (superuser)" : ""}.
                </Container>
            );
        }

        return (
            <Container>
                <h3>Login</h3>
                <span style={{ color: "red" }}>{this.state.invalid ? "Invalid username or password." : ""}</span>
                <form onSubmit={this.handleSubmit}>
                    <label>Username: <TextInput name="username" value={this.state.username} onChange={this.handleChange} /></label>
                    <br />
                    <label>Password: <TextInput name="password" value={this.state.password} onChange={this.handleChange} type="password" /></label>
                    <br />
                    <Button type="submit" value="Login">Login</Button>
                </form>
            </Container>
        );
    }
}

export default Login;
