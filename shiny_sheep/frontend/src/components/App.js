import React, { Component } from "react";
import { render } from "react-dom";
import {GlobalStyle,ThemeProvider} from '@react95/core';
import { createGlobalStyle } from 'styled-components';
import Chat from "./Chat";
import Footer from "./Footer";
import Home from "./Home";


const GlobalStyles = createGlobalStyle`
  body {
    font-family: 'ms_sans_serif';
    background-color: #008080;
    
  }
`;

class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
          <ThemeProvider>
            <GlobalStyle/>
            <Home/>
            <Footer/>
          {/* <Chat/> */}
         
         
          </ThemeProvider>
    

      </div>
    )
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
