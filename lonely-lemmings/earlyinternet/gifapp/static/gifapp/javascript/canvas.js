let canvas;
let ctx;
let savedImageData;
let dragging = false;
let strokeColor = 'black';
let fillColor = 'black';
let line_Width = 2;
let polygonSides = 3;

let lastX, lastY;

//currently used tool
let currentTool = 'brush';

//is brush currently used
let usingBrush = false;

//is eraser currently used
let usingEraser = false;

//save states
let SaveStates = [];

//frame number
let frameNumber = 0;

//saved frames
let savedFrames = [];

//represents box that shape is drawn in
class ShapeBoundingBox{
    constructor(left, top, width, height) {
        this.left = left;
        this.top = top;
        this.width = width;
        this.height = height;
    }
}

//represents x,y coordinates of mouse down location
class MouseDownPos{
    constructor(x,y) {
        this.x = x;
        this.y = y;
    }
}

//represents x,y coordinate of current mouse position
class Location{
    constructor(x,y) {
        this.x = x;
        this.y = y;
    }
}

// represents a point on a polygon
class PolygonPoint{
    constructor(x,y) {
        this.x = x;
        this.y = y;
    }
}

let shapeBoundingBox = new ShapeBoundingBox(0,0,0,0);
let mousedown = new MouseDownPos(0,0);
let loc = new Location(0,0);

//grab existing data from database if any
function getImages(){
    let xhr = new XMLHttpRequest();
    let name = document.getElementById("project-name").innerText;
    let url = name +"/load";


    xhr.open("GET", url, true);
    xhr.responseText = "json";

    //callback
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            let response = JSON.parse(xhr.responseText);
            let img_data = response["data"];
            if (img_data.length === 0) {
                SaveStates.push(ctx.getImageData(0, 0, canvas.width, canvas.height));
            } else {
                for (let i = 0; i < img_data.length; i++) {
                    let decode = "data:image/jpeg;base64," + img_data[i];
                    savedFrames.push(decode);
                }
                OpenImage();
            }
        }
    }
    xhr.send();
}

//load page
document.addEventListener('DOMContentLoaded', setupCanvas);

function setupCanvas(){
    canvas = document.getElementById('my-canvas');
    ctx = canvas.getContext('2d');
    ctx.strokeStyle = strokeColor;
    ctx.lineWidth = line_Width;
    getImages();

    //add mouse listeners
    canvas.addEventListener("mousedown", ReactToMouseDown);
    canvas.addEventListener("mousemove", ReactToMouseMove);
    canvas.addEventListener("mouseup", ReactToMouseUp);
}

function ChangeTool(toolClicked){
    document.getElementById("clear").className = "";
    document.getElementById("save").className = "";
    document.getElementById("brush").className = "";
    document.getElementById("line").className = "";
    document.getElementById("rectangle").className = "";
    document.getElementById("ellipse").className = "";
    document.getElementById("polygon").className = "";
    document.getElementById("eraser").className = "";
    document.getElementById(toolClicked).className = "selected";
    currentTool = toolClicked;
}

function GetMousePosition(x,y){
    let canvasSizeData = canvas.getBoundingClientRect();
    return { x: (x - canvasSizeData.left) * (canvas.width  / canvasSizeData.width),
        y: (y - canvasSizeData.top)  * (canvas.height / canvasSizeData.height)
      };
}

function SaveCanvasImage(){
    savedImageData = ctx.getImageData(0,0,canvas.width,canvas.height);
}

function RedrawCanvasImage(){
    ctx.putImageData(savedImageData,0,0);
}

function UpdateRubberbandSizeData(loc){
    shapeBoundingBox.width = Math.abs(loc.x - mousedown.x);
    shapeBoundingBox.height = Math.abs(loc.y - mousedown.y);

    //allow for stretching box up and down
    if(loc.x > mousedown.x){
        shapeBoundingBox.left = mousedown.x;
    } else {
        shapeBoundingBox.left = loc.x;
    }

    if(loc.y > mousedown.y){
        shapeBoundingBox.top = mousedown.y;
    } else {
        shapeBoundingBox.top = loc.y;
    }
}

function getAngleUsingXAndY(mouselocX, mouselocY){
    let adjacent = mousedown.x - mouselocX;
    let opposite = mousedown.y - mouselocY;

    return radiansToDegrees(Math.atan2(opposite, adjacent));
}

function radiansToDegrees(rad){
    if(rad < 0){
        return (360.0 + (rad * (180 / Math.PI))).toFixed(2);
    } else {
        return (rad * (180 / Math.PI)).toFixed(2);
    }
}

function degreesToRadians(degrees){
    return degrees * (Math.PI / 180);
}

function getPolygonPoints(){
    let angle =  degreesToRadians(getAngleUsingXAndY(loc.x, loc.y));
    let radiusX = shapeBoundingBox.width;
    let radiusY = shapeBoundingBox.height;
    let polygonPoints = [];

    for(let i = 0; i < polygonSides; i++){
        polygonPoints.push(new PolygonPoint(loc.x + radiusX * Math.sin(angle),
        loc.y - radiusY * Math.cos(angle)));
        angle += 2 * Math.PI / polygonSides;
    }
    return polygonPoints;
}

function getPolygon(){
    let polygonPoints = getPolygonPoints();
    ctx.beginPath();
    ctx.moveTo(polygonPoints[0].x, polygonPoints[0].y);
    for(let i = 1; i < polygonSides; i++){
        ctx.lineTo(polygonPoints[i].x, polygonPoints[i].y);
    }
    ctx.closePath();
}

function drawRubberbandShape(loc){
    ctx.strokeStyle = strokeColor;
    ctx.fillStyle = fillColor;
    ctx.lineWidth = line_Width;
    if(currentTool === "line"){
        ctx.beginPath();
        ctx.moveTo(mousedown.x, mousedown.y);
        ctx.lineTo(loc.x, loc.y);
        ctx.stroke();
    } else if(currentTool === "rectangle"){
        ctx.strokeRect(shapeBoundingBox.left, shapeBoundingBox.top, shapeBoundingBox.width, shapeBoundingBox.height);
    } else if(currentTool === "ellipse"){
        let radiusX = shapeBoundingBox.width / 2;
        let radiusY = shapeBoundingBox.height / 2;
        ctx.beginPath();
        ctx.ellipse(mousedown.x, mousedown.y, radiusX, radiusY, Math.PI / 4, 0, Math.PI * 2);
        ctx.stroke();
    } else if(currentTool === "polygon"){
        getPolygon();
        ctx.stroke();
    }
}

function UpdateRubberbandOnMove(loc){
    UpdateRubberbandSizeData(loc);
    drawRubberbandShape(loc);
}

function DrawBrush(x, y, color){
    if (usingBrush) {
        ctx.beginPath();
        ctx.strokeStyle = color;
        ctx.lineWidth = line_Width;
        ctx.lineJoin = "round";
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(x, y);
        ctx.closePath();
        ctx.stroke();
    }
    lastX = x; lastY = y;
}

function drawCircle(x, y){
    if(usingEraser){
        ctx.globalCompositeOperation = "destination-out";
        ctx.beginPath();
        ctx.arc(x, y, line_Width, 0, Math.PI*2);
        ctx.fill();
    }
}

function ReactToMouseDown(e){
    canvas.style.cursor = "crosshair";
    loc = GetMousePosition(e.clientX, e.clientY);
    mousedown.x = loc.x;
    mousedown.y = loc.y;
    dragging = true;

    if(currentTool === 'brush'){
        usingBrush = true;
        DrawBrush(loc.x, loc.y, strokeColor);
    }
    else if (currentTool === 'eraser'){
        usingEraser = true;
        drawCircle(loc.x, loc.y);
    }
    SaveCanvasImage();
}

function ReactToMouseMove(e){
    canvas.style.cursor = "crosshair";
    loc = GetMousePosition(e.clientX, e.clientY);

    if(currentTool === 'brush'){
        DrawBrush(loc.x, loc.y, strokeColor);
        SaveCanvasImage();
    } else if (currentTool === 'eraser') {
        drawCircle(loc.x, loc.y);
        SaveCanvasImage();
    }else {
        if(dragging){
            RedrawCanvasImage();
            UpdateRubberbandOnMove(loc);
        }
    }
}

function ReactToMouseUp(e){
    canvas.style.cursor = "default";
    loc = GetMousePosition(e.clientX, e.clientY);
    RedrawCanvasImage();
    UpdateRubberbandOnMove(loc);
    dragging = false;
    usingBrush = false;
    usingEraser = false;
    if(currentTool === 'brush') {
        ctx.beginPath();
    }
    SaveCanvasImage();
    ctx.globalCompositeOperation = "source-over";
    SaveStates.push(savedImageData);
}

function OpenImage(){
    let img = new Image();
    img.onload = function(){
        ctx.clearRect(0,0,canvas.width, canvas.height);
        ctx.drawImage(img,0,0);
    }
    img.src = savedFrames[frameNumber];
}

function UpdateFrameNumber(){
    document.getElementById("frame-button").innerHTML = frameNumber;
}

function SaveImage() {
    savedFrames[frameNumber] = canvas.toDataURL();
}

function Next(){
    SaveImage();
    frameNumber +=1;
    if (frameNumber < savedFrames.length){
        OpenImage();
    }
    SaveStates = [];
    SaveCanvasImage();
    SaveStates.push(savedImageData);
    UpdateFrameNumber();
}

function Previous(){
    if (frameNumber > 0){
        SaveImage();
        frameNumber -=1;
        OpenImage();
        UpdateFrameNumber();
        SaveStates = [];
        SaveCanvasImage();
        SaveStates.push(savedImageData);
    }
}

function Delete(){
    savedFrames.splice(frameNumber, 1);

    if (frameNumber === 0){
        Clear();
        return null;
    }
    if (frameNumber === savedFrames.length){
        frameNumber -=1;
        UpdateFrameNumber();
    }
    SaveStates = [];
    SaveCanvasImage();
    SaveStates.push(savedImageData);
    OpenImage();
}

function SendData(type){
    let xhr = new XMLHttpRequest();
    let name = document.getElementById("project-name").innerText;
    let url = name + "/" + type;

    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    let frames = savedFrames.length - 1;
    //callback
    xhr.onreadystatechange = function (){
        if (xhr.readyState === 4 && xhr.status === 200) {
            alert("Frames 0 to " + frames.toString(10) + " Saved to Server!");
        }
    }

    let data = JSON.stringify({"image_BLOB": savedFrames});
    xhr.send(data);
}

function RequestRender(){
    let xhr = new XMLHttpRequest();
    let name = document.getElementById("project-name").innerText;
    let url = name + "/render"

    xhr.open("GET", url, true);

    //callback
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 404){
                alert(xhr.responseText);
            } else if(xhr.status === 200){
                alert(xhr.responseText);
            }
        }
    }
    xhr.send();
}

function Undo(){
    if(SaveStates.length > 1){
        SaveStates.pop();
        let saveState = SaveStates[SaveStates.length - 1];
        ctx.putImageData(saveState,0,0);
    }
}

function Clear(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}