//slider scripts
//button color values
var buttonRed = "0";
var buttonGreen = "0";
var buttonBlue = "0";

//REQUIRES: color to be "red", "green", "blue", 0<= value <=255
function setButtonColor(value, color){
    if(color === "red") {
        buttonRed = value;
    } else if (color === "green") {
        buttonGreen = value;
    } else if (color === "blue") {
        buttonBlue = value;
    }

    document.getElementById("color-button").style.backgroundColor =
    'rgb(' + buttonRed + ',' + buttonGreen + ',' + buttonBlue + ')';
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
}

//polygon slider
var polygonSlider = document.getElementById("polygonSideSlider");
var polygonOutput = document.getElementById("polygon_value");
polygonOutput.innerHTML = polygonSlider.value;

polygonSlider.oninput = function() {
    polygonOutput.innerHTML = this.value;
}
