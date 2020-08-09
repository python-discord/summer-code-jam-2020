import React, { useEffect, useState, useCallback, Component } from "react";
import { Tabs, Tab, TabBody } from "react95";
import Chat from "./Chat";
import "./Home.css";

const HOME = 0;
const LOBBY = 1;

class Home extends Component {
  constructor(props) {
    super(props);
    this.onTabChange = this.onTabChange.bind(this);
    this.state = {
      activeTab: HOME,
    };
  }
  onTabChange(event, value){
    this.setState({activeTab: value});
  }
  render() {
    return (
      <div>
        <Tabs value={this.state.activeTab} onChange={this.onTabChange}>
          <Tab value={HOME}>Home</Tab>
          <Tab value={LOBBY}>#Lobby</Tab>
        </Tabs>
        <TabBody>
          {this.state.activeTab === HOME && <Chat />}
          {this.state.activeTab === LOBBY && <div>Test</div>}
        </TabBody>
        <div className="main-Content">
          <div class="row mt-5">
            <div class="col offset-md-3"></div>
            <div class="col">
              <p>List goes here</p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
export default Home;
