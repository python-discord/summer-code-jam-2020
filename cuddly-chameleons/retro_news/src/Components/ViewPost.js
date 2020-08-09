import React, { useState, useEffect } from 'react';
import {Link, useParams, useHistory} from 'react-router-dom';
import { Container, Button } from 'nes-react';
import { Row, Col } from 'react-bootstrap';

import axios from "../AxiosAPI";
import Comments from "./Comments";

function ViewPost(props) {
     const history = useHistory();
     const [data, setData] = useState({title: "", content: "", author: {username: "", email: ""}});
     const [notFound, setNotFound] = useState(false);
     const [superuser, setSuperuser] = useState(false);
     const { id } = useParams();

     useEffect(() => {
          async function fetchData() {
               if (localStorage.getItem('access_token') || localStorage.getItem('refresh_token')) {
                    const result = await axios.get('/superuser/');
                    localStorage.setItem('superuser', result.data.is_superuser ? 'true' : 'false');
                    setSuperuser(result.data.is_superuser);
               } else {
                    setSuperuser(false);
               }

               try {
                    const result = await axios.get(`/posts/${id}`);
                    result.data.created = new Date(result.data.created).toString();
                    setData(result.data);
                    document.title = "Retro News - " + result.data.title;
               } catch (e) {
                    console.error(e);
                    document.title = "Retro News - Post not found";
                    setNotFound(true);
               }
          }
          fetchData();
     }, [id, setNotFound, setData, setSuperuser]);

     if (notFound) {
          return (
              <Container>
                   <span style={{ color: "red" }}>Cannot find post with ID {id}.</span>
              </Container>
          )
     }

     const deleteAction = async (event) => {
          event.preventDefault();
          try {
               await axios.delete('/posts/' + id + "/");
               history.push('/');
          } catch (e) {
               console.error(e);
          }
     };

     return (
         <Container title={data.title}>
              <Row>
                   <Col md="8" style={{ whiteSpace: "pre", overflow: "auto" }}>
                        {data.content}
                   </Col>
                   <Col md="4">
                        <Container>
                             Author: {data.author.username}
                             <br />
                             Created: {data.created}
                             <br />
                             {superuser && props.status ? <div><Link to={`/posts/edit/${id}`} className="px-2"><Button type="button">Edit</Button></Link><Button onClick={deleteAction} className="px-2">Delete</Button></div> : ""}
                        </Container>
                   </Col>
              </Row>
              <Comments postId={id} className="px-5" status={props.status} />
         </Container>
     )
}

export default ViewPost;
