import React, { Component } from 'react'
import logo from "../assets/timescape-logos/1999-2010.svg"

export class Home_page_2 extends Component {
  render() {

        {/* Styling */}
        const myFont ={
            fontFamily: "Ariel",
            fontSize: "9pt"
        }

        const myHref = {
            fontFamily: "Arial",
            fontSize:"9pt",
            color: "blue",
            textDecorationLine: 'underline',
            verticalAlign: "bottom"
        }

        const searchBar = {
            fontFamily: "sans-serif",
            justifyContent: "center",
            alignItems: "center",
            fontSize: "9pt",
            verticalAlign: "bottom",
            resize: "none",
            height: "20px",
            width: "375px"
        };

        const myButton = {
            fontFamily: "sans-serif",
            lineHeight: "5px",
            fontSize: "9pt",
            height: "19px"
        };

    return (
        <div className="container-fluid">
            {/* First container for the content of the page*/}
            <div className="row pr-1 justify-content-end"> {/* Upper right corner*/}
                    <a href= "" style={myHref}>Personalized home &nbsp;</a>
                    <p style={myFont}>|</p>
                    <a href= "" style={myHref}>&nbsp; Sign in</a>
            </div>
            <div className="row justify-content-center"> {/* Image */}
                <img src={logo} class="img-fluid" alt="logo" style={{padding: "40px"}}/> 
            </div>
            <div className="container">
                {/* Second container dedicated to the search */}
                <div className="row justify-content-center"> {/* Toolbar */}
                    <div className="col-0 px-2">
                        <a href= "" style={myHref}>Web</a>
                    </div>
                    <div className="col-0 px-2">
                        <a href= "" style={myHref}>Image</a>
                    </div>
                    <div className="col-0 px-2">
                        <a href= "" style={myHref}>Groups</a>
                    </div>
                    <div className="col-0 px-2">
                        <a href= "" style={myHref}>News</a>
                    </div>
                    <div className="col-0 px-2">
                        <a href= "" style={myHref}>Froogle</a>
                    </div>
                    <div className="col-0 px-2">
                        <a href= "" style={myHref}>Local</a>
                    </div>
                    <div className="col-0 px-2">
                        <a href= "" style={myHref}>more »</a>
                    </div>
                </div>
                <div className="row justify-content-center"> {/* Search field */}
                    <input type="text" style={searchBar}/>
                </div>
                <div className="row justify-content-center"> {/* Buttons for the search field */}
                    <input type="submit" style={myButton} value="TimeScape Search"/>
                    <input type="submit" style={myButton} value="I'm Feeling Lucky"/>
                </div>
                {/* End of second container */}
            </div>
            <div className="container">
                {/* Third container dedicated to the bussiness info */}
                <div className="row justify-content-center pt-4 pb-2">
                    <p style={{color: "red", fontFamily: "Arial", fontSize:"9pt"}}>New!&nbsp;</p>
                    <a href="" style={myHref}>TimeScape Finance</a>
                    <p style={{fontFamily: "sans-serif", fontSize: "9pt"}}>: Business info, news, and interactive charts.</p>
                </div>
                <div className="row center-block text-center">
                    <div className="col text-right pr-0">
                        <a href= "" style={myHref}>Advertising Programs</a>
                    </div>
                    <div className="col-0 pt-1 px-1">
                        <a>-</a>
                    </div>
                    <div className="col-0">
                        <a href= "" style={myHref}>Business Solutions</a>
                    </div>
                    <div className="col-0 pt-1 px-1">
                        <a>-</a>
                    </div>
                    <div className="col text-left pl-0">
                        <a href= "" style={myHref}>About TimeScape</a>
                    </div>
                </div>
                <div className="row justify-content-center pt-2">
                    <p style={myFont}>Copyright©Zealous Zebras</p>
                </div>
                {/* End of third container */}
            </div>
            {/* End of first container */}
        </div>
    )
  }
}

export default Home_page_2
