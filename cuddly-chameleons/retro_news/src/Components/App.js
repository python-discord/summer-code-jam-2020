import React from 'react';
import '../css/App.css';
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Header from './Header';
import Login from './Login';
import SignUp from './SignUp';
import ViewPost from "./ViewPost";
import ViewPosts from "./ViewPosts";
import CreatePost from './CreatePost';
import EditPost from "./EditPost";
import Search from './Search';

class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {logged_in: localStorage.getItem('access_token') && localStorage.getItem('refresh_token')};
        this.toggleLogin = this.toggleLogin.bind(this);
    }

    toggleLogin(status) {
        this.setState({ logged_in: status });
    }

    render() {
        return (
            <BrowserRouter>
                <Header handler={this.toggleLogin} status={this.state.logged_in} />
                <Switch>
                    <Route path="/login" children={<Login handler={this.toggleLogin} />}/>
                    <Route path="/signup" children={<SignUp handler={this.toggleLogin} />}/>
                    <Route path="/search" children={<Search />} />
                    <Route path="/posts/new" children={<CreatePost status={this.state.logged_in} />} />
                    <Route path="/posts/edit/:id" children={<EditPost status={this.state.logged_in} />} />
                    <Route path="/posts/:id" children={<ViewPost status={this.state.logged_in} />} />
                    <Route path={["/", "/posts"]} children={<ViewPosts />} />
                </Switch>
            </BrowserRouter>
        );
    }
}

export default App;
