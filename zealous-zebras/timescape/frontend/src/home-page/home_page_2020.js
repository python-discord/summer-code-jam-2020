import React, { Component } from 'react'
import logo from "../assets/timescape-logos/2015-2020.svg"

export class Home_page_2 extends Component {
  render() {

      {/* Styling */}

      const searchBar = {
        borderWidth:1,
        borderColor:'rgba(0,0,0,0.2)',
        alignItems:'center',
        justifyContent:'center',
        width:600,
        height:45,
        backgroundColor:'#fff',
        borderRadius:50,
        
      }

      const myButton = {
        fontSize: "11pt",
        color: "darkslategray",
        borderWidth: 0,
        alignItems: 'center',
        justifyContent: 'center',
        width: 140,
        height: 35,
        backgroundColor: '#F4F4F4',
        borderRadius: 5,
        marginLeft: 10,
        marginRight: 5,
        marginTop: 35
      }

      const myHref = {
        fontSize: "11pt",
        color: "darkslategray"
      }

    return (
        <div className="container">
          {/* First container for the content of the page */}
          <div className="row justify-content-center"> {/* Logo */}
            <img src={logo} class="img-fluid" alt="logo" style={{padding: "40px", marginTop:"165px"}}/> 
          </div>
          <div className="row justify-content-center"> {/* Searchbar */}
            <input type="text" style={searchBar}/>
          </div>
          <div className="row justify-content-center"> {/* Buttons */}
            <input type="submit" style={myButton} value="TimeScape Search"/>
            <input type="submit" style={myButton} value="I'm Feeling Lucky"/>
          </div>
          <div className="container-fluid fixed-bottom bg-light border">
            {/* Second container for the footer */}
            <div className="row p-2">
              <div className="col-0 px-2">
                <a href= "" style={myHref}>Advertising</a>
              </div>
              <div className="col-0 px-2">
                <a href= "" style={myHref}>Business</a>
              </div>
              <div className="col-0 px-2 mr-auto">
                <a href= "" style={myHref}>How Search works</a>
              </div>
              <div className="col-0 px-2">
                <a href= "" style={myHref}>Privacy</a>
              </div>
              <div className="col-0 px-2">
                <a href= "" style={myHref}>Terms</a>
              </div>
              <div className="col-0 px-2">
                <a href= "" style={myHref}>Settings</a>
              </div>
            </div>
            {/* End of second container */}
          </div>
          {/* End of first container */}
        </div>
    )
  }
}

export default Home_page_2
