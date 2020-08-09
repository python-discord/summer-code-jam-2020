import React, { Component } from 'react';
import Draggable from 'react-draggable';
import { Slider, Grid } from '@material-ui/core';
import { createMuiTheme } from '@material-ui/core/styles';
import { ThemeProvider as MuiThemeProvider } from '@material-ui/core/styles';
import './menubar.css';

const theme = createMuiTheme({
  palette: {
    primary: {
      light: '#4dabf5',
      main: '#2196f3',
      dark: '#002884',
    },
  },
});

class MenuBar extends Component {
  constructor(props) {
    super(props);

    const initVal = this.props.initialValue
    this.state = { selectedYear: initVal }
  }

  InputSlider() {
    const initialValue = this.props.initialValue;

    // Gets called whenever the slider value is updated.
    const handleSliderChange = (_, newValue) => {
      this.setState({ selectedYear: newValue });
    };

    return (
      <MuiThemeProvider theme={theme}>
        <Grid container justify="center">
          <Slider
            defaultValue={initialValue}
            onChange={handleSliderChange}
            min={this.props.valueSpan[0]}
            max={this.props.valueSpan[1]}
            marks={this.props.labelValues}
          />
        </Grid>
      </MuiThemeProvider>
    );
  }

  menuContent() {
    return (
      <div className="row menu-box mx-auto align-items-center">
        <div className="menu-section col-auto pl-1">
          <div className="handle p-2 d-flex draggable-icon align-items-center">
            <img src={require("../icons/draggable-handle.svg")} draggable="false" alt="::" height="17px" />
          </div>
          <div className="col-auto align-items-center" style={{ width: "200px" }}>
            {this.InputSlider()}
          </div>
          <div className="col px-0" id="currentYearLabel">
            <p className="my-auto year-label" style={{ width: "60px" }}>{this.state.selectedYear}</p>
          </div>
        </div>
        <div className="verticalLine" />
        <a href="/account" className="menu-section menu-link col">
          <img src={require("../icons/profile-link.svg")} draggable="false" alt="::" height="19px" />
        </a>
      </div>
    )
  }

  render() {
    return (
      <div>
        <Draggable handle=".handle">
          <div className="overlay">
            <div className="d-flex fixed-bottom">
              {this.menuContent()}
            </div>
          </div>
        </Draggable>
      </div>
    );
  }
}

export default MenuBar;