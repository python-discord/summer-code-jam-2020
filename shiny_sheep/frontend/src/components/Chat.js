import React, { Component } from "react";

class Chat extends Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    
   this.state = {
      input: "" 
    }
  }
  componentDidMount(){
  }
  handleChange(event){
    this.setState({input: event.target.value});
  }
  handleSubmit(event){
    event.preventDefault();
    console.log("Submit!");
    const data = JSON.stringify({
      'message': this.state.input
    });
    this.props.chat.websocket.send(data);
    this.setState({ input: "" });
  }

  render() {
    return (
      <div>
        <div>
          {this.props.chat.chatLogs}
        </div>
        <br />
        <form onSubmit={this.handleSubmit}>
          <input value={this.state.input} onChange={this.handleChange} id="chat-message-input" type="text" size="100" autocomplete="off" />
          <br />
          <input id="chat-message-submit" type="submit" value="Send" />
        </form>
      </div>
    );
  }
}

export default Chat;
