import React, { Component } from "react";
import { render } from "react-dom";
import { ThemeProvider } from 'styled-components';
import Home from "./Home";
import CustomContext from "./CustomContext";
import original from "react95/dist/themes/original";

class App extends Component {
  constructor(props) {
    super(props);
  }
   
  render() {
    return (
      <div>
            <ThemeProvider theme={original}>
              <Home/>
            </ThemeProvider>
      </div>
    )
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
