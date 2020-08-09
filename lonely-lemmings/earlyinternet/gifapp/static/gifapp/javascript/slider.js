//slider scripts
//button color values
let buttonRed = "00";
let buttonGreen = "00";
let buttonBlue = "00";

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
    let hex = "#" + pad(buttonRed) + pad(buttonGreen) + pad(buttonBlue);

    document.getElementById("color-button").style.backgroundColor = hex;
    strokeColor = hex;
    fillColor = hex;
}

//red slider
let redSlider = document.getElementById("redSlider");
let redOutput = document.getElementById("red_value");
redOutput.innerHTML = redSlider.value;

redSlider.oninput = function() {
    redOutput.innerHTML = this.value;
    setButtonColor(this.value, "red");
}

//green slider
let greenSlider = document.getElementById("greenSlider");
let greenOutput = document.getElementById("green_value");
greenOutput.innerHTML = greenSlider.value;

greenSlider.oninput = function() {
    greenOutput.innerHTML = this.value;
    setButtonColor(this.value, "green");
}

//blue slider
let blueSlider = document.getElementById("blueSlider");
let blueOutput = document.getElementById("blue_value");
blueOutput.innerHTML = blueSlider.value;

blueSlider.oninput = function() {
    blueOutput.innerHTML = this.value;
    setButtonColor(this.value, "blue");
}

//width slider
let widthSlider = document.getElementById("lineWidthSlider");
let widthOutput = document.getElementById("width_value");
widthOutput.innerHTML = widthSlider.value;

widthSlider.oninput = function() {
    widthOutput.innerHTML = this.value;
    line_Width = this.value;
}

//polygon slider
let polygonSlider = document.getElementById("polygonSideSlider");
let polygonOutput = document.getElementById("polygon_value");
polygonOutput.innerHTML = polygonSlider.value;

polygonSlider.oninput = function() {
    polygonOutput.innerHTML = this.value;
    polygonSides = this.value;
}
