import React, { Component } from "react";
import { render } from "react-dom";
import {ThemeProvider} from '@react95/core';
import Home from "./Home";



class App extends Component {
  constructor(props) {
    super(props);
  }
  
  render() {
    return (
      <div> 
            <ThemeProvider>
              <div style={{float:"right"}}>
                <button>Sign In</button>
                <button>Change Password</button>
              </div>
              <Home/>
            </ThemeProvider>
         
      </div>
    )
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
