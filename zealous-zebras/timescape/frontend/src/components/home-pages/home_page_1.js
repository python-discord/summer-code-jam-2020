import React, { Component } from 'react'
import "./home_page_1.css"
import image from "../../assets/google-logos/1.png"

export class Home_page_1 extends Component {
  render() {
    return (
        <div className="container">
            <div className="row">
                <div className="col center-block text-center">
                    <img src={image} class="img-fluid" alt="Responsive image"/> 
                </div>
            </div>
            <div className="row">
                <div className="container bg-light">
                    <div className="row py-0">
                        <div className="col center-block text-center">
                            <p style={{margin: "0px"}}>Search the web using Google!</p> 
                        </div>
                    </div>
                    <div className="row">
                        <div className="col border py-0 center-block text-center">
                            <textarea id="search" style={{margin: "0px"}} name="search" rows="1" cols="50"/> 
                        </div>
                    </div>
                    <div className="row border py-0 justify-content-center">
                        <div className="col-0 px-1 pb-0 text-center">
                            <select name="results" id="results">
                                <option value="5-results">5 results</option>
                                <option value="5-results">10 results</option>
                                <option value="5-results">15 results</option>
                                <option value="5-results">20 results</option>
                                <option value="5-results">25 results</option>
                                <option value="5-results">50 results</option>
                            </select>
                        </div>
                        <div className="col-0 px-1 pb-0 text-center">
                            <button>Google Search</button>
                        </div>
                        <div className="col-0s px-1 pb-0 text-center">
                            <button>I'm feeling lucky</button>
                        </div>
                    </div>
                    <div className="row">
                        <div className="col center-block text-center">
                            <p>Index contains ~25 million pages (soon to be much bigger)</p> 
                        </div>
                    </div>
                </div>
            </div>
            <div className="row">
                <div className="col center-block text-center">
                    <a href="">About Google!</a>
                </div>
            </div>
            <div className="row">
                <div className="col text-center">
                    <a href="">Stanford Search</a>
                </div>
                <div className="col text-center">
                    <a href="">Linux Search</a>
                </div>
            </div>
            <div className="container bg-light">
                <div className="row">
                    <div className="col center-block text-center">
                        <p>Get Google! updates monthly!</p> 
                    </div>
                </div>
                <div className="row row py-0 justify-content-center">
                    <div className="col-0 px-1 pb-0 text-center">
                        <textarea id="search" name="search" rows="1" cols="25"/>
                    </div>
                    <div className="col-0 px-1 pb-0 text-center">
                        <button>Subscribe</button>
                    </div>
                    <div className="col-0 px-1 pb-0 text-center">
                        <a href="">Archive</a>
                    </div>
                </div>
            </div>
            <div className="row">
                <div className="col center-block text-center">
                    <p>Copyright</p> 
                </div>
            </div>
        </div>
    )
  }
}

export default Home_page_1
