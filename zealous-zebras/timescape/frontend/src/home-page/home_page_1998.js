import React, { Component } from 'react'
import logo from "../assets/timescape-logos/1998.svg"

export class Home_page_1 extends Component {
  render() {

        {/* Styling */}
        const myText = {
            fontFamily: "Lucida Grande",
            fontSize: "11pt",
            margin: "0"
        };

        const myWrap = {
            backgroundColor: "#EFEFEF",
            width: "975px",
            margin: "relative",
            marginLeft: "auto",
            marginRight:"auto",
            alignItems:'center'
        };

        const myButton = {
            fontFamily: "sans-serif",
            lineHeight: "5px",
            fontSize: "9pt",
            height: "19px",
            verticalAlign: "top",
        };

        const myDropdown = {
            fontFamily: "sans-serif",
            verticalAlign: "top",
            fontSize: "10pt",
            height: "19px",
        };

        const searchField = {
            fontFamily: "sans-serif",
            justifyContent: "center",
            alignItems: "center",
            fontSize: "9pt",
            verticalAlign: "bottom",
            resize: "none",
            height: "20px",
            width: "322px",
        };
        
        const myHref = {
            fontFamily: "Lucida Grande",
            color: "blue",
            fontSize: "10pt",
            textDecorationLine: 'underline'
        };

        const myHrefBold = {
            fontFamily: "Lucida Grande",
            color: "blue",
            fontSize: "16pt",
            fontWeight: 'bold',
            textDecorationLine: 'underline',
        };

        const myEmail = {
            fontFamily: "sans-serif",
            verticalAlign: "top",
            fontSize: "8pt",
            resize: "none",
            height: "19px",
            width: "150px",
            margin: "0"
        };

    return (
        <div className="container">
            {/* First container for the content of the page */}
            <div className="row justify-content-center"> {/* Image */}
                <img src={logo} class="img-fluid" alt="logo" style={{padding: "40px"}}/> 
            </div>
            <div className="row">
                <div className="wrap" style={myWrap}> {/* Wrap for the background color */}
                    <div className="container">
                    {/* Second container containing the search bar, dropdown and buttons relative to the search */}    
                        <div className="row">
                            <div className="col text-center">
                                <p style={myText}>
                                    Search the web using TimeScape!
                                </p> 
                            </div>
                        </div>
                        <div className="row">
                            <div className="col text-center">
                                <input type="text" name="search" style={searchField}/> {/* Search field */}
                            </div>
                        </div>
                        <div className="row justify-content-center">
                            <div className="col-0 px-1 text-center">
                                <select name="results" id="results" style={myDropdown}> {/* Dropdown */}
                                    <option value="5-results">10 results</option>
                                    <option value="5-results">30 results</option>
                                    <option value="5-results">100 results</option>
                                </select>
                            </div>
                            <div className="col-0 px-1 text-center"> {/* Buttosn for the search field */}
                                <input type="submit" value="TimeScape Search" style={myButton}/>
                            </div>
                            <div className="col-0s px-1 text-center">
                                <input type="submit" value="I'm feeling lucky" style={myButton}/>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col text-center"> {/* Web stats */}
                                <p style={{fontFamily: "Lucida Grande", fontSize: "10pt" , fontStyle: "italic", margin: "0"}}>
                                Index contains ~25 million pages (soon to be much bigger)
                                </p> 
                            </div>
                        </div>
                    {/* End of second container */}
                    </div>
                </div>
            </div>
            <div className="row"> {/* General info */}
                <div className="col pb-3 center-block text-center">
                    <a href="" style={myHrefBold}>
                        About TimeScape!
                    </a>
                </div>
            </div>
            <div className="row">
                <div className="col text-right px-1">
                    <a href="" style={myHref}>
                        Stanford Search
                    </a>
                </div>
                <div className="col text-left px-1">
                    <a href="" style={myHref}>
                        Linux Search
                    </a>
                </div>
            </div>
            <div className="wrap" style={myWrap}>
                <div className="container">
                    {/* Second container which is dedicated to asking users email */}
                    <div className="row">
                        <div className="col center-block text-center">
                            <p style={myText}>
                                Get TimeScape! updates monthly!
                            </p> 
                        </div>
                    </div>
                    <div className="row py-0 justify-content-center">
                        <div className="col-0 px-1 text-center">
                            <input type="text" placeholder="your e-mail" style={myEmail}/> {/* Email field */}
                        </div>
                        <div className="col-0 px-1 text-center">
                            <input type="submit" value="Subscribe" style={myButton}/> {/* Button for submiting email */}
                        </div>
                        <div className="col-0 px-1 text-center">
                            <a href="" style={myHref}>
                                Archive
                            </a>
                        </div>
                    </div>
                    {/* end of second container */}
                </div>
            </div>
            <div className="row">
                <div className="col text-center">
                    <p style={{fontSize: "8pt", margin: "0", verticalAlign: "top"}}>
                        Copyright©Zealous Zebras
                    </p> 
                </div>
            </div>
        </div>
    )
  }
}

export default Home_page_1
