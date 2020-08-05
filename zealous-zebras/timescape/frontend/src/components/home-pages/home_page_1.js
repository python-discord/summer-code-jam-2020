import React, { Component } from 'react'
import "./home_page_1.css"

export class Home_page_1 extends Component {
  render() {

        const myButton = {
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            fontSize: "10pt",
            border: "1px solid black",
            height: "22px",

        };

        const searchField = {
            justifyContent: "center",
            alignItems: "center",
            fontSize: "9pt",
            verticalAlign: "bottom",
            resize: "none",
            height: "25px",
            width: "304px",
            maxLines: "1"
        };

        const myText = {
            fontSize: "10pt",
            margin: "0"
        };

        const myHref = {
            color: "blue",
            fontSize: "10pt",
            textDecorationLine: 'underline'
        };

        const myHrefBold = {
            color: "blue",
            fontSize: "16pt",
            fontWeight: 'bold',
            textDecorationLine: 'underline'
        };

        const myEmail = {
            verticalAlign: "top",
            fontSize: "8pt",
            resize: "none",
            height: "22px",
            width: "150px",
            margin: "0"
        };

        const myDropdown = {
            verticalAlign: "top",
            fontSize: "10pt",
            height: "22px",
        };

        const myWrap = {backgroundColor: "#EFEFEF",
        width: "550px",
        margin: "relative",
        marginLeft: "auto",
        marginRight:"auto",
        alignItems:'center'
        };

    return (
        <div className="container">
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
                                <textarea id="search" name="search" style={searchField}/> 
                            </div>
                        </div>
                        <div className="row justify-content-center">
                            <div className="col-0 px-1 text-center">
                                <select name="results" id="results" style={myDropdown}>
                                    <option value="5-results">5 results</option>
                                    <option value="5-results">10 results</option>
                                    <option value="5-results">15 results</option>
                                    <option value="5-results">20 results</option>
                                    <option value="5-results">25 results</option>
                                    <option value="5-results">50 results</option>
                                </select>
                            </div>
                            <div className="col-0 px-1 text-center">
                                <button type="button" style={myButton}>
                                    Google Search
                                </button>
                            </div>
                            <div className="col-0s px-1 text-center">
                                <button type="button" style={myButton}>
                                    I'm feeling lucky
                                </button>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col text-center">
                                <p style={{fontSize: "10pt" , fontStyle: "italic", margin: "0"}}>
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
                            <p style={{fontSize: "10pt", marginBottom: "15px"}}>
                                Get Google! updates monthly!
                            </p> 
                        </div>
                    </div>
                    <div className="row py-0 justify-content-center">
                        <div className="col-0 px-1 text-center">
                            <textarea id="search" name="search" rows="1" cols="25" placeholder="your e-mail" style={myEmail}/>
                        </div>
                        <div className="col-0 px-1 text-center">
                            <button type="button" style={myButton}>
                                Subscribe
                            </button>
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
