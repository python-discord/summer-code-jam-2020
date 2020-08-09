import React, {useEffect, useState} from "react";
import {Container, TextInput, TextArea, Button} from "nes-react";
import axios from "../AxiosAPI";
import { useParams } from 'react-router-dom';

function EditPost(props) {
    const [loading, setLoading] = useState(true);
    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");
    const [updating, setUpdating] = useState(false);
    const [updated, setUpdated] = useState(false);
    const [failed, setFailed] = useState(false);
    const [superuser, setSuperuser] = useState(false);
    const [notFound, setNotFound] = useState(false);
    const { id } = useParams();

    const handleTitleChange = (event) => {
        setTitle(event.target.value);
        setUpdated(false);
    };

    const handleContentChange = (event) => {
        setContent(event.target.value);
        setUpdated(false);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        setUpdating(true);
        try {
            await axios.put(`/posts/${id}/`, {title: title, content: content});
            setUpdated(true);
        } catch (e) {
            console.error(e);
            setFailed(true);
        }
        setUpdating(false);
    };

    useEffect(() => {
        async function init() {
            if (localStorage.getItem('access_token') || localStorage.getItem('refresh_token')) {
                const result = await axios.get('/superuser/');
                localStorage.setItem('superuser', result.data.is_superuser ? 'true' : 'false');
                setSuperuser(result.data.is_superuser);
                setLoading(false);
                if (superuser) {
                    try {
                        const post = await axios.get(`/posts/${id}/`);
                        setTitle(post.data.title);
                        setContent(post.data.content);
                        document.title = `Retro News - Edit ${post.data.title}`;
                    } catch (e) {
                        console.error(e);
                        setNotFound(true);
                    }
                }
            } else {
                 localStorage.setItem('superuser', 'false');
                 setSuperuser(false);
                 setLoading(false);
            }
        }
        init();
    }, [setLoading, setTitle, setContent, superuser, setSuperuser, id]);

    if (loading) {
        return (
            <Container>
                Loading...
            </Container>
        );
    }

    if (!superuser || !props.status) {
        return (
            <Container>
                <span style={{ color: "red" }}>You don't have permission to edit this post.</span>
            </Container>
        )
    }

    if (notFound) {
        return (
            <Container>
                <span style={{ color: "red" }}>Post with ID {id} don't exist.</span>
            </Container>
        );
    }

    if (updating) {
        return (
            <Container>
                Updating post...
            </Container>
        )
    }

    return (
        <div>
            {updated ? <Container><span style={{color: "green"}}>Post updated</span></Container> : ""}
            {failed ? <Container><span style={{color: "red"}}>An error occurred while trying to update post.</span></Container> : ""}
            <Container>
                <h3>Update post</h3>
                <form onSubmit={handleSubmit}>
                    <label>Title: <TextInput name="title" value={title} onChange={handleTitleChange} /></label>
                    <br />
                    <label>Content: <TextArea name="content" value={content} onChange={handleContentChange} /></label>
                    <br />
                    <Button type="submit" value="Update">Update</Button>
                </form>
            </Container>
        </div>
    );
}

export default EditPost;
