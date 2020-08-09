import React, { Component } from "react";

class Chat extends Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);

    this.state = {
      input: "",
    };
  }
  componentDidMount() {}
  handleChange(event) {
    this.setState({ input: event.target.value });
  }
  handleSubmit(event) {
    event.preventDefault();
    if (this.state.input.length != 0) {
      const joinCommandRe = /^\/join (\w+)$/;
      const commandMatch = joinCommandRe.exec(this.state.input);
      if (commandMatch) {
        const chatRoomName = commandMatch[1];
        this.props.joinChatRoom(chatRoomName);
      } else {
        const data = JSON.stringify({
          message: this.state.input,
        });
        this.props.chat.websocket.send(data);
      }
      this.setState({ input: "" });
    }
  }

  render() {
    return (
      <div style={{float:"right"}}>
        <div>{this.props.chat.chatLogs}</div>
        <br />
        <form onSubmit={this.handleSubmit}>
          <input
            value={this.state.input}
            onChange={this.handleChange}
            id="chat-message-input"
            type="text"
            size="100"
            autocomplete="off"
          />
          <br />
          <input id="chat-message-submit" type="submit" value="Send" />
        </form>
      </div>
    );
  }
}

export default Chat;
