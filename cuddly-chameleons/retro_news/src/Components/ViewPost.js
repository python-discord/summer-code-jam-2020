import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Container } from 'nes-react';
import { Row, Col } from 'react-bootstrap';

import axios from "../AxiosAPI";

function ViewPost() {
     const [data, setData] = useState({title: "", content: "", author: {username: "", email: ""}});
     const [notFound, setNotFound] = useState(false);
     const { id } = useParams();

     useEffect(() => {
          async function fetchData() {
               try {
                    const result = await axios.get(`/posts/${id}`);
                    result.data.created = new Date(result.data.created).toString();
                    setData(result.data);
               } catch (e) {
                    setNotFound(true);
               }
          }
          fetchData();
     }, [id, setNotFound, setData]);

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
                        </Container>
                   </Col>
              </Row>
         </Container>
     )
}

export default ViewPost;
