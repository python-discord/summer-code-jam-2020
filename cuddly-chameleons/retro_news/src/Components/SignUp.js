import React from 'react';

import { Container, TextInput, Button } from 'nes-react';

import axios from '../AxiosAPI';

class SignUp extends React.Component {
    constructor(props) {
        super(props);
        this.state = {username: "", password: "", email: "", creating: false, errors: {}};
        document.title = "Retro News - Sign Up";

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    async handleSubmit(event) {
        event.preventDefault();
        this.setState({ creating: true });

        try {
            const response = await axios.post(
                '/user/create/',
                {email: this.state.email, username: this.state.username, password: this.state.password}
            );

            const tokenResponse = await axios.post('/token/obtain/', {
                username: response.data.username,
                password: this.state.password
            });
            axios.defaults.headers['Authorization'] = "JWT " + tokenResponse.data.access;
            localStorage.setItem('access_token', tokenResponse.data.access);
            localStorage.setItem('refresh_token', tokenResponse.data.refresh);
            localStorage.setItem('username', this.state.username);
            localStorage.setItem('superuser', response.data.superuser === true ? 'true' : 'false');

            this.setState({creating: false});
            this.setState({username: "", password: "", email: ""});
            this.props.handler(true);

            return tokenResponse.data;
        } catch (error) {
            console.log(error);
            this.setState({creating: false});
            this.setState({ errors: error.response.data });
        }
    }

    render() {
        if (localStorage.getItem('access_token') && localStorage.getItem('refresh_token')) {
            return (
                <Container>
                    Logged in as {localStorage.getItem('username')}{localStorage.getItem('superuser') === 'true' ? " (superuser)" : ""}.
                </Container>
            );
        }

        if (this.state.creating) {
            return (
                <Container>
                    Creating account...
                </Container>
            );
        }

        return (
            <Container>
                <h3>Sign up</h3>
                <form onSubmit={this.handleSubmit}>
                    <label>Username: <TextInput name="username" value={this.state.username} onChange={this.handleChange} /></label>
                    { this.state.errors.username ? <br /> : null }
                    <span style={{color: "red"}}>{ this.state.errors.username ? this.state.errors.username : null }</span>
                    <br />
                    <label>Email: <TextInput name="email" value={this.state.email} onChange={this.handleChange} /></label>
                    { this.state.errors.email ? <br /> : null }
                    <span style={{color: "red"}}>{ this.state.errors.email ? this.state.errors.email : null }</span>
                    <br />
                    <label>Password: <TextInput name="password" value={this.state.password} onChange={this.handleChange} type="password" /></label>
                    { this.state.errors.password ? <br /> : null }
                    <span style={{color: "red"}}>{ this.state.errors.password ? this.state.errors.password : null }</span>
                    <br />
                    <Button type="submit" value="Login">Sign up</Button>
                </form>
            </Container>
        );
    }
}

export default SignUp;
