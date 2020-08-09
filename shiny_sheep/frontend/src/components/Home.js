import React, {useEffect, useState, useCallback} from 'react';
import {Tabs,Tab } from '@react95/core';
import Chat from "./Chat";
import "./Home.css";
import UserTable from "./UserTable";

const USERS = ['Ami','Layla','Eric','John'];

const Home = () =>{
    return (
        <div>
            <Tabs active Tab="Home" >
                <Tab title = "Home">
                    <div className ="main-Content">
                       <div className="row my-auto" >
                           <div className="col offset-md-6">Welcome!
                               </div>
                       </div>
                    </div>
                </Tab>
                <Tab title ="#lobby">
                    <div className = "main-Content">
                        <div className="row mt-5">
                            
                            <div className="col-md-8" style={{paddingLeft:"10px"}}>
                                <Chat/>
                            </div>
                            <div className="col-sm-1 mr-5" style ={{backgroundColor:"white",float:"left"}}>
                                <UserTable  users = {USERS}/>
                            </div>
                           
                        </div>
                    </div>
                </Tab>
            </Tabs>
        </div>
    );
}

export default Home;