import React, {useEffect, useState} from "react";
import axios from "../AxiosAPI";
import { Container } from "nes-react";
import {Link} from "react-router-dom";

function ViewPosts() {
    const [posts, setPosts] = useState([]);
    const [errored, setErrored] = useState(false);
    document.title = "Retro News - Posts";

    useEffect(() => {
        async function fetchData() {
            try {
                const result = await axios.get('/posts');
                setPosts(result.data);
            } catch (e) {
                console.error(e);
                setErrored(true);
            }
        }
        fetchData();
    }, [setPosts, setErrored]);

    if (errored) {
        return (
            <Container>
                <span style={{ color: "red" }}>
                    An error occurred while trying to fetch posts.
                </span>
            </Container>
        );
    }

    if (!posts.length) {
        return (
            <Container>
                No posts found
            </Container>
        );
    }

    return (
        <div>
            {posts.map((post, i) => {
                return (
                    <div key={i}>
                        <Container title={<Link to={`/posts/${post.id}`}>{`${post.title} (from ${post.author.username})`}</Link>}>
                            <div style={{ whiteSpace: "pre", overflow: "auto" }}>
                                {post.content.substring(0, 100)}...
                            </div>
                        </Container>
                    </div>
                );
            })}
        </div>
    );
}

export default ViewPosts;
