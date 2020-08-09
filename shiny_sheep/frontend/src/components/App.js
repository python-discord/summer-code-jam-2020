import React, { Component } from "react";
import { render } from "react-dom";
import {ThemeProvider} from '@react95/core';
import Home from "./Home";



class App extends Component {
  constructor(props) {
    super(props);
  }

  signOut(){
    console.log(window.location);
    window.location.pathname = "accounts/logout";
    console.log(window.location);
  }
  
  changePssd(){
    window.location.pathname = "accounts/password/change";
  }
  
  render() {
    return (
      <div> 
            <ThemeProvider>
             
              <div style={{float:"right"}}>
                <button onClick={this.signOut}>Sign Out</button>
                <button onClick={this.changePssd}>Change Password</button>
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
