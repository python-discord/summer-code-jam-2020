import React, {useEffect, useState, useCallback} from 'react';
import {TaskBar,List } from '@react95/core';
import someImg from "../../../static/images/favicons/favicon.ico";


const MODAL_DEFAULT_POSITION = { x: 500, y: 100 }

const SOCIAL_ANCHORS_LIST = [
    {
      icon: someImg,
      name: 'PC',
      url: 'https://www.youtube.com/',
    },
    {
      icon: someImg,
      name: 'Files',
      url: 'https://www.youtube.com/',
    },

  ]

const Footer = () =>{
    const [showAboutModal, setShowAboutModal] = useState(true);

    const handleOpenModal = useCallback(()=>{
      setShowAboutModal(true)
    },[]);
  
    const handleCloseModal = useCallback(()=>{
      setShowAboutModal(false);
    },[]);


    return (
        <TaskBar
        list={
          <List>
            <List.Item icon={someImg}>
              This PC
            </List.Item>
            <List.Item icon={someImg}>
              Files
            </List.Item>

            <List.Divider />

            <List.Item icon={someImg} onClick={handleOpenModal}>
              About
            </List.Item>
          
          </List>
        }
        />
    );
}

export default Footer;