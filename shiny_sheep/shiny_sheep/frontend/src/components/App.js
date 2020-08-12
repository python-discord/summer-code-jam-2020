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
            <ThemeProvider theme={original}>
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
