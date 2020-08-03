import React, { Component } from 'react';
import Draggable from 'react-draggable';

import './menubar.css'

class MenuBar extends Component {
  render() {
    return (
      <div>
        <Draggable handle=".handle">
          <div className="overlay">
            <div className="d-flex fixed-bottom">
              <div className="menu-box mx-auto">
                <span className="handle">::: </span>
                <span>Some content</span>
              </div>
            </div>
          </div>
        </Draggable>
      </div>
    );
  }
}

export default MenuBar;