import React, { Component } from 'react'
import "./home_page_1.css"

export class Home_page_1 extends Component {
  render() {

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
            verticalAlign: "top",
            alignText: "center",
            fontSize: "9pt",
            height: "22px",

        };

        const myDropdown = {
            fontFamily: "sans-serif",
            verticalAlign: "top",
            fontSize: "10pt",
            height: "22px",
        };

        const searchField = {
            fontFamily: "sans-serif",
            justifyContent: "center",
            alignItems: "center",
            fontSize: "9pt",
            verticalAlign: "bottom",
            resize: "none",
            height: "25px",
            width: "300px",
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
            height: "22px",
            width: "150px",
            margin: "0"
        };

    return (
        <div className="container">
            {/* first container containing the search bar and buttons relative to the search */}
            <div className="row">
                <div className="col text-center">
                    <img src="" class="img-fluid" alt="Responsive image" style={{padding: "40px"}}/> 
                </div>
            </div>
            <div className="row">
                <div className="wrap" style={myWrap}>
                    <div className="container">
                        <div className="row">
                            <div className="col text-center">
                                <p style={myText}>
                                    Search the web using Google!
                                </p> 
                            </div>
                        </div>
                        <div className="row">
                            <div className="col text-center">
                                <input type="text" name="search" style={searchField}/> 
                            </div>
                        </div>
                        <div className="row justify-content-center">
                            <div className="col-0 px-1 text-center">
                                <select name="results" id="results" style={myDropdown}>
                                    <option value="5-results">10 results</option>
                                    <option value="5-results">30 results</option>
                                    <option value="5-results">100 results</option>
                                </select>
                            </div>
                            <div className="col-0 px-1 text-center">
                                <input type="submit" value="Google Search" style={myButton}/>
                            </div>
                            <div className="col-0s px-1 text-center">
                                <input type="submit" value="I'm feeling lucky" style={myButton}/>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col text-center">
                                <p style={{fontFamily: "Lucida Grande", fontSize: "10pt" , fontStyle: "italic", margin: "0"}}>
                                Index contains ~25 million pages (soon to be much bigger)
                                </p> 
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div className="row">
                <div className="col pb-3 center-block text-center">
                    <a href="" style={myHrefBold}>
                        About Google!
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
                    <div className="row">
                        <div className="col center-block text-center">
                            <p style={myText}>
                                Get Google! updates monthly!
                            </p> 
                        </div>
                    </div>
                    <div className="row py-0 justify-content-center">
                        <div className="col-0 px-1 text-center">
                            <input type="text" placeholder="your e-mail" style={myEmail}/>
                        </div>
                        <div className="col-0 px-1 text-center">
                            <input type="submit" value="Subscribe" style={myButton}/>
                        </div>
                        <div className="col-0 px-1 text-center">
                            <a href="" style={myHref}>
                                Archive
                            </a>
                        </div>
                    </div>
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
