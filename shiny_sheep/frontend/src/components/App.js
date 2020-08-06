import React, { Component } from "react";
import { render } from "react-dom";
import Chat from "./Chat";

class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <h1>Hello world!</h1>
        <Chat/>
      </div>
    )
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
