import React, {useEffect, useState, useCallback} from 'react';
import {Tabs,Tab } from '@react95/core';
import Chat from "./Chat";
import "./Home.css";


const Home = () =>{
    return (
        <div>
            <Tabs active Tab="Home" >
                <Tab title = "Home">
                    <div className ="main-Content">
                       Placeholder
                    </div>
                </Tab>
                <Tab title ="#lobby">
                    <div className = "main-Content">
                        <div class="row mt-5">
                            <div class="col">
                                <Chat/>
                            </div>
                            <div class="col">
                                <p>List goes here</p>
                            </div>
                        </div>
                    </div>
                </Tab>
            </Tabs>
        </div>
    );
}

export default Home;