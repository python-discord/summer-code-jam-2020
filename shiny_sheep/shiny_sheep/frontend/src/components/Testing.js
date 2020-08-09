import React, {useEffect, useState, useCallback} from 'react';
import {ThemeProvider, GlobalStyle,TaskBar,Modal,List,Icon } from '@react95/core';
import styled, { createGlobalStyle } from 'styled-components';


const MODAL_DEFAULT_POSITION = { x: window.innerWidth/2 -250, y: 150 }
const GlobalStyles = createGlobalStyle`
  body {
    font-family: 'ms_sans_serif';
    background-color: #008080;
    
  }
`;


const Testing = () =>{
 
  const [showAboutModal, setShowAboutModal] = useState(true);

  const handleOpenModal = useCallback(()=>{
    setShowAboutModal(true)
  },[]);

  const handleCloseModal = useCallback(()=>{
    setShowAboutModal(false);
  },[]);

  return (
    <div>
    <ThemeProvider>
    <GlobalStyles/>
    {showAboutModal && ( <Modal
        closeModal={handleCloseModal}
        defaultPosition={MODAL_DEFAULT_POSITION}
        height={50}
        icon='info_bubble'
        menu={[
          {
            name: 'File',
            list: (
              <List>
                <List.Item onClick={handleCloseModal}>Exit</List.Item>
                <List.Item onClick={handleCloseModal}>Extra</List.Item>
                <List.Item onClick={handleCloseModal}>Options</List.Item>
              </List>
            ),
          },
          {
              name: 'Edit',
              list:(
                  <List>
                      <List.Item>Undo</List.Item>
                      <List.Item>Redo</List.Item>
                  </List>
              )
          }
          
        ]}

        title='Review'
        width={500}
        height={550}
      >
        <p>
          Hi this is a test
        </p>
        
      </Modal>
    )}
    </ThemeProvider>
    </div>
  );
  

}

export default Testing;