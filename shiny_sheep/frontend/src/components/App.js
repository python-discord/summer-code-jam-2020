import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return <h1>Hello world!</h1>
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
