import React, { Component } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import Homepage_1998 from '../home-page/home_page_1998.js'
import Homepage_2006 from '../home-page/home_page_2006.js'
import Homepage_2020 from '../home-page/home_page_2020.js'

function DynamicHome(props){
    const year = useSelector(state => state.year);
    switch (true) {
        case year > 2006:
            return <Homepage_2020 />
        case year > 1998:
            return <Homepage_2006 />
        case 1998:
            return <Homepage_1998 />
        default: 
            return <Homepage_1998 />
    }
}

export default DynamicHome;