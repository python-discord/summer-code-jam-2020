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
      <div className="row d-flex align-items-center">
        <div className="col-1 handle d-flex draggable-icon align-items-center">
          <img src={require("../icons/draggable-handle.svg")} draggable="false" alt="::" height="17px" />
        </div>
        <div className="col pl-3 pr-1" id="currentYearLabel">
          <p className="my-auto year-label" style={{ width: "50px" }}>{this.state.selectedYear}</p>
        </div>
        <div className="col-auto pl-0 align-items-center" style={{ width: "200px" }}>
          {this.InputSlider()}
        </div>
      </div>
    )
  }

  render() {
    return (
      <div>
        <Draggable handle=".handle">
          <div className="overlay">
            <div className="d-flex fixed-bottom">
              <div className="menu-box mx-auto align-items-center">
                {this.menuContent()}
              </div>
            </div>
          </div>
        </Draggable>
      </div>
    );
  }
}

export default MenuBar;