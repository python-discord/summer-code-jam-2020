import React from "react";
import axios from "../AxiosAPI";
import {Container, TextInput, TextArea, Button} from "nes-react";

class CreatePost extends React.Component {
    constructor(props) {
        super(props);
        this.state = {title: "", content: "", creating: false, created: false, failed: false, loading: true, superuser: false};
        document.title = "Retro News - Create Post";
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value, created: false, failed: false});
    }

    async handleSubmit(event) {
        event.preventDefault();
        this.setState({creating: true})
        try {
            await axios.post('/posts/', {title: this.state.title, content: this.state.content});
            this.setState({title: "", content: "", created: true, creating: false});
        } catch (e) {
            console.error(e);
            this.setState({failed: true, creating: true});
        }
    }

    async componentDidMount() {
        if (localStorage.getItem('access_token') || localStorage.getItem('refresh_token')) {
            const result = await axios.get('/superuser/');
            localStorage.setItem('superuser', result.data.is_superuser ? 'true' : 'false');
            this.setState({superuser: result.data.is_superuser, loading: false});
        } else {
            localStorage.setItem('superuser', 'false');
            this.setState({superuser: false, loading: false});
        }
    }

    render() {
        if (this.state.loading) {
            return (
                <Container>
                    Loading...
                </Container>
            );
        }

        if (!this.state.superuser || !this.props.status) {
            return (
                <Container>
                    <span style={{ color: "red" }}>You don't have permission to create a new post.</span>
                </Container>
            )
        }

        if (this.state.creating) {
            return (
                <Container>
                    Creating post...
                </Container>
            )
        }

        return (
            <div>
                {this.state.created ? <Container><span style={{color: "green"}}>Post created</span></Container> : ""}
                {this.state.failed ? <Container><span style={{color: "red"}}>An error occurred while trying to create a new post.</span></Container> : ""}
                <Container>
                    <h3>Create a new post</h3>
                    <form onSubmit={this.handleSubmit}>
                        <label>Title: <TextInput name="title" value={this.state.title} onChange={this.handleChange} /></label>
                        <br />
                        <label>Content: <TextArea name="content" value={this.state.content} onChange={this.handleChange} /></label>
                        <br />
                        <Button type="submit" value="Create">Create</Button>
                    </form>
                </Container>
            </div>
        );
    }
}

export default CreatePost;
