import React, {useEffect, useState, useCallback} from 'react';
import {Tabs,Tab } from '@react95/core';
import Table from "./Table";


const Home = () =>{
    return (
        <div style ={{width: "75%", margin:"5em auto"}}>
            <Tabs active Tab="Home">
                <Tab title = "Home">
                    <div className ="row" style={{height:"700px"}}>
                        <div className ="col mt-3">
                            <div style={{marginLeft:"2em"}}>
                                <p>Find Game and Chat Rooms</p>
                                <input placeholder="Type to search by keyword"></input>
                                <Table/>
                            </div>
                        </div>
                        <div className="col mt-5" style={{height:"250px"}}>
                            <Tabs active Tab="Overview" style={{backgroundColor:"white"}}>
                                <Tab title="Overview">
                                    <h3>Chess</h3>
                                    <p>Chess is a game played on a 8x8 lorem ipsum</p>
                                    <p>IMG HERE</p>
                                    <p>Its history began in dolor sit amet, consectetur adipiscing elit. 
                                        Phasellus justo enim, hendrerit posuere finibus a, viverra ac magna. 
                                        Donec maximus justo nec dapibus euismod. Morbi sit amet nibh vel diam 
                                        convallis commodo quis quis ante. Phasellus dignissim velit et turpis 
                                        rhoncus pulvinar. Sed a pretium orci, et fringilla mi. Sed non faucibus justo, 
                                        in scelerisque libero. Nullam aliquet feugiat diam vitae dapibus. Nullam in vehicula 
                                        metus, in pellentesque arcu. Aenean at risus condimentum, aliquet turpis in.
                                    </p>
                                </Tab>
                                <Tab title="Game Rooms">
                                    
                                    
                                </Tab>
                                <Tab title="Rate Game">
                                    <p>Rate Game Here</p>
                                </Tab>
                            </Tabs>
                            
                        </div>
                    </div>
                </Tab>
                <Tab title ="#lobby">
                    <h1>Lobby Goes HERE</h1>
                </Tab>
            </Tabs>
        </div>
    );
}

export default Home;