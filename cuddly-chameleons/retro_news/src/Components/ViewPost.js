import React, { useState, useEffect } from 'react';
import {Link, useParams} from 'react-router-dom';
import { Container, Button } from 'nes-react';
import { Row, Col } from 'react-bootstrap';

import axios from "../AxiosAPI";

function ViewPost(props) {
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
               } catch (e) {
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

     return (
         <Container title={data.title}>
              <Row>
                   <Col md="8" style={{ whiteSpace: "pre" }}>
                        {data.content}
                   </Col>
                   <Col md="4">
                        <Container>
                             Author: {data.author.username}
                             <br />
                             Created: {data.created}
                             <br />
                             {superuser && props.status ? <Link to={`/posts/edit/${id}`}><Button type="button">Edit</Button></Link> : ""}
                        </Container>
                   </Col>
              </Row>
         </Container>
     )
}

export default ViewPost;
