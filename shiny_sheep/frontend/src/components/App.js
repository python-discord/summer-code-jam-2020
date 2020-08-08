import React, { Component } from "react";
import { render } from "react-dom";
import {GlobalStyle,ThemeProvider,Icon} from '@react95/core';
import { createGlobalStyle } from 'styled-components';
import Chat from "./Chat";
import Footer from "./Footer";
import Home from "./Home";
import CustomContext from "./CustomContext";
import Testing from "./Testing";


const GlobalStyles = createGlobalStyle`
  body {
    font-family: 'ms_sans_serif';
    background-color: #008080;
    
  }
`;

class App extends Component {
  constructor(props) {
    super(props);
    this.state={
      menu:[{label:"PlaceHolder1",callback:this.itemCallback},
      {label:"Placeholder2", callback:this.item2Callback},
      {label:"Placeholder3", callback:this.item3Callback},]
    
    }
  }


  itemCallback() {
      alert('clicked');
    }
    
    item2Callback() {
      alert("clicked on Item 2");
    }
    
    item3Callback() {
      alert("clicked on Item3");
    }
   
  render() {
    return (
      <div>
          <CustomContext items={this.state.menu}/>
           
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
