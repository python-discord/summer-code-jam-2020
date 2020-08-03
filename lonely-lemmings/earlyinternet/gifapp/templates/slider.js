//slider scripts
//button color values
var buttonRed = "00";
var buttonGreen = "00";
var buttonBlue = "00";

document.getElementById("color-button").style.backgroundColor = "#000000";

//REQUIRES: color to be "red", "green", "blue", 0<= value <=255
function setButtonColor(value, color){
    //fill in blank values during hex conversion
    function pad(n){
      return (n.length<2) ? "0"+n : n;
    }

    if(color === "red") {
        buttonRed = parseInt(value, 10).toString(16);
    } else if (color === "green") {
        buttonGreen = parseInt(value, 10).toString(16);
    } else if (color === "blue") {
        buttonBlue = parseInt(value, 10).toString(16);
    }
    hex = "#" + pad(buttonRed) + pad(buttonGreen) + pad(buttonBlue);

    document.getElementById("color-button").style.backgroundColor = hex;
    strokeColor = hex;
    fillColor = hex;
}

//red slider
var redSlider = document.getElementById("redSlider");
var redOutput = document.getElementById("red_value");
redOutput.innerHTML = redSlider.value;

redSlider.oninput = function() {
    redOutput.innerHTML = this.value;
    setButtonColor(this.value, "red");
}

//green slider
var greenSlider = document.getElementById("greenSlider");
var greenOutput = document.getElementById("green_value");
greenOutput.innerHTML = greenSlider.value;

greenSlider.oninput = function() {
    greenOutput.innerHTML = this.value;
    setButtonColor(this.value, "green");
}

//blue slider
var blueSlider = document.getElementById("blueSlider");
var blueOutput = document.getElementById("blue_value");
blueOutput.innerHTML = blueSlider.value;

blueSlider.oninput = function() {
    blueOutput.innerHTML = this.value;
    setButtonColor(this.value, "blue");
}

//width slider
var widthSlider = document.getElementById("lineWidthSlider");
var widthOutput = document.getElementById("width_value");
widthOutput.innerHTML = widthSlider.value;

widthSlider.oninput = function() {
    widthOutput.innerHTML = this.value;
    line_Width = this.value;
}

//polygon slider
var polygonSlider = document.getElementById("polygonSideSlider");
var polygonOutput = document.getElementById("polygon_value");
polygonOutput.innerHTML = polygonSlider.value;

polygonSlider.oninput = function() {
    polygonOutput.innerHTML = this.value;
    polygonSides = this.value;
}
