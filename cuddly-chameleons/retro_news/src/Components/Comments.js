import React from "react";

import { Container, TextArea, Button } from "nes-react";
import axios from "../AxiosAPI";

class Comments extends React.Component {
    constructor(props) {
        super(props);
        this.state = {comments: [], loading: true, comment: "", failed: false, createSuccess: false, createFailed: false};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    async fetchPosts() {
        try {
            const response = await axios.get('/comments');
            this.setState({comments: response.data});
        } catch (e) {
            console.error(e);
            this.setState({ failed: true });
        }
        this.setState({ loading: false });
    }

    async componentDidMount() {
        await this.fetchPosts();
        this.setState({createFailed: false, createSuccess: false});
    }

    async handleSubmit(event) {
        event.preventDefault();
        try {
            await axios.post('/comments/', {comment: this.state.comment, post: parseInt(this.props.postId)});
            this.setState({createSuccess: true, comment: ""});
        } catch (e) {
            console.error(e);
            this.setState({createFailed: true, createSuccess: false});
        }
        await this.fetchPosts();
    }

    render() {
        if (this.state.loading) {
            return (
                <Container>
                    Loading...
                </Container>
            );
        }

        if (this.state.failed) {
            return (
                <Container>
                    <span style={{ color: "red" }}>
                        An error occurred while trying to fetch comments.
                    </span>
                </Container>
            );
        }

        return (
            <div>
                <Container title="Comments">
                    {this.state.createSuccess ? <Container><span style={{ color: "green" }}>Comment creation successful</span></Container> : ""}
                    {this.state.createFailed ? <Container><span style={{ color: "red" }}>An error occurred while trying to create a new comment.</span></Container> : ""}
                    {
                        this.props.status ?
                        <Container title="Add comment">
                            <form onSubmit={this.handleSubmit}>
                                <label><TextArea name="comment" value={this.state.comment} onChange={this.handleChange} maxLength="10000" /></label>
                                <br />
                                <Button type="submit" value="Comment">Comment</Button>
                            </form>
                        </Container> : ""
                    }
                    {this.state.comments.map((comment, i) => {
                        return (
                            <Container key={i} title={comment.author.username}>
                                {comment.comment}
                            </Container>
                        );
                    })}
                </Container>
            </div>
        );
    }
}

export default Comments;
