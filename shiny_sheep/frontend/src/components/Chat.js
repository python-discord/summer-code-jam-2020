import React, { Component } from "react";

const chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/chat/test/"
);

class Chat extends Component {
  constructor(props) {
    super(props);
    chatSocket.onmessage = function (e) {
      const data = JSON.parse(e.data);
      this.setState({ chatLogs: this.chatLogs + data.message})
    };
    chatSocket.onclose = function (e) {
      console.error("Chat socket closed unexpectedly");
    };
    this.state = { chatLogs: [] };
  }

  render() {
    const displayLogs = [];
    for (let log in this.state.chatLogs) {
      displayLogs.push(<span>{log}</span>);
    }
    return (
      <div>
        <textarea id="chat-log" cols="100" rows="20"></textarea>
        <br />
        <input id="chat-message-input" type="text" size="100" />
        <br />
        <input id="chat-message-submit" type="button" value="Send" />
      </div>
    );
  }
}

export default Chat;
