import React from "react";
import {Container, TextInput, Button} from "nes-react";
import {Link} from "react-router-dom";
import axios from "../AxiosAPI";

class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {searched: false, searching: false, posts: [], searchString: "", failed: false};
        document.title = "Retro News - Search";
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    async handleSubmit(event) {
        event.preventDefault();
        this.setState({searching: true, failed: false});

        try {
            const result = await axios.get('/posts?title=' + this.state.searchString);
            this.setState({posts: result.data});
            this.setState({searched: true});
        } catch (e) {
            console.error(e);
            this.setState({failed: true});
        }
        this.setState({searching: false})
    }

    render() {
        let searchedArea = "";
        if (this.state.searching) {
            searchedArea = (
                <Container>
                    Searching...
                </Container>
            );
        }

        if (this.state.searched) {
            if (this.state.posts.length === 0) {
                searchedArea = (
                    <Container>
                        <span style={{ color: "red" }}>Can't find posts with search "{this.state.searchString}".</span>
                    </Container>
                );
            } else {
                searchedArea = (
                    <div>
                        {this.state.posts.map((post, i) => {
                            return (
                                <div key={i}>
                                    <Container title={<Link to={`/posts/${post.id}`}>{`${post.title} (from ${post.author.username})`}</Link>}>
                                        <div style={{ whiteSpace: "pre" }}>
                                            {post.content.substring(0, 100)}...
                                        </div>
                                    </Container>
                                </div>
                            );
                        })}
                    </div>
                );
            }
        } else {
            searchedArea = "";
        }

        return (
            <div>
                {this.state.failed ? <Container><span style={{ color: "red" }}>An error occurred when trying to search posts.</span></Container> : ""}
                <Container title="Search">
                    <form onSubmit={this.handleSubmit}>
                        <label>Title: <TextInput name="searchString" value={this.state.searchString} onChange={this.handleChange} /></label>
                        <br />
                        <Button type="submit" value="Search">Search</Button>
                    </form>
                </Container>
                {searchedArea}
            </div>
        );
    }
}

export default Search;
