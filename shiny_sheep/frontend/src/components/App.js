import React, { Component } from "react";
import { render } from "react-dom";
import {ThemeProvider} from '@react95/core';
import Home from "./Home";
import CustomContext from "./CustomContext";
import Testing2 from "./Testing2";


class App extends Component {
  constructor(props) {
    super(props);
  }


 
   
  render() {
    return (
      <div>
          {/* <CustomContext items={this.state.menu}/> */}
           
            <ThemeProvider>
              {/* <Testing2 test="Test2"/> */}
              {/* <GlobalStyle/> */}
              <Home/>
              {/* <Footer/> */}
              
            </ThemeProvider>
         
      </div>
    )
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
