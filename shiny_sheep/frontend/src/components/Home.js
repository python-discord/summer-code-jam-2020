import React, {
  useEffect,
  useState,
  useCallback,
  Component,
  createContext,
} from "react";
import {
  Tabs,
  Tab,
  TabBody,
  Window,
  WindowHeader,
  WindowContent,
} from "react95";
import Chat from "./Chat";
import "./Home.css";

class Home extends Component {
  constructor(props) {
    super(props);
    this.onTabChange = this.onTabChange.bind(this);
    this.joinChatRoom = this.joinChatRoom.bind(this);
    this.state = {
      activeChat: "#intro",
      chats: undefined,
    };
  }
  updateRoom(roomName, chatRoom) {
    const chats = { ...this.state.chats };
    chats[roomName] = chatRoom;
    this.setState({
      ...this.state,
      chats: chats,
    });
  }
  setupWebsockets(chatWebSocket, roomName, chatRoom) {
    chatWebSocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      chatRoom.chatLogs.push((<span>User: {data.message}</span>), (<br/>));
      this.updateRoom(roomName, chatRoom);
    };
    chatWebSocket.onclose = (event) => {
      chatRoom.chatLogs.push(
        (<span class="websocketMessage">WebSocket: Disconnected!</span>), (<br/>)
      );
      this.updateRoom(roomName, chatRoom);
    };
  }

  joinChatRoom(roomName) {
    // TODO: Check if chatRoom exists
    const chatWebSocket = new WebSocket(
      "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
    );
    const chatRoom = {
      websocket: chatWebSocket,
      chatLogs: [],
    };
    this.updateRoom(roomName, chatRoom);
    this.setupWebsockets(chatWebSocket, roomName, chatRoom);
  }
  componentDidMount() {
    const chatWebSocket = new WebSocket(
      "ws://" + window.location.host + "/ws/intro/"
    );
    const chatRoom = {
      websocket: chatWebSocket,
      chatLogs: [],
    };
    this.updateRoom("#intro", chatRoom);
    this.setupWebsockets(chatWebSocket, "#intro", chatRoom);
  }
  onTabChange(event, value) {
    this.setState({ ...this.state, activeChat: value });
  }
  componentWillUnmount() {
    for (const [roomName, chatRoom] of Object.entries(this.state.chats)) {
      chatRoom.websocket.close();
    }
  }
  render() {
    const chatTabs = [];
    if (this.state.chats !== undefined) {
      for (let chat of Object.keys(this.state.chats)) {
        chatTabs.push(<Tab key={chat} value={chat}>{chat}</Tab>);
      }
    }
    return (
      <Window>
        <WindowHeader>IRC</WindowHeader>
        <WindowContent>
          <Tabs value={this.state.activeChat} onChange={this.onTabChange}>
            {chatTabs}
          </Tabs>
          <TabBody>
            {this.state.chats !== undefined && (
              <Chat joinChatRoom={this.joinChatRoom} chat={this.state.chats[this.state.activeChat]} />
            )}
          </TabBody>
        </WindowContent>
      </Window>
    );
  }
}
export default Home;
