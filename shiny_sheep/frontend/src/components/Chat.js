import React, { Component } from "react";

const chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/intro/"
);

class Chat extends Component {
  constructor(props) {
    super(props);

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    
    this.state = { 
      chatLogs: "",
      input: ""
    };
  }
  componentDidMount(){
    chatSocket.onmessage = (event) => { 
      const data = JSON.parse(event.data);
      this.appendChatLogs(data.message);
    };
    chatSocket.onclose = (event) => {
      this.appendChatLogs("Disconnected!");
      console.error("Chat socket closed unexpectedly");
    };
  }
  handleChange(event){
    this.setState({input: event.target.value});
  }
  handleSubmit(event){
    const data = JSON.stringify({
      'message': this.state.input
    });
    chatSocket.send(data);
    this.setState({ input: "" });
    event.preventDefault();
  }
  appendChatLogs(message){
    this.setState({ chatLogs: this.state.chatLogs + message + '\n'})
  }

  render() {
    return (
      <div>
        <textarea value={this.state.chatLogs} id="chat-log" cols="100" rows="20"></textarea>
        <br />
        <form onSubmit={this.handleSubmit}>
          <input value={this.state.input} onChange={this.handleChange} id="chat-message-input" type="text" size="100" />
          <br />
          <input id="chat-message-submit" type="submit" value="Send" />
        </form>
      </div>
    );
  }
}

export default Chat;
