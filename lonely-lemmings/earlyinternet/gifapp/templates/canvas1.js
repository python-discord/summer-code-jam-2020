let canvas;
let ctx;
let savedImageData;
let dragging = false;
let strokeColor = 'black';
let fillColor = 'black';
let line_Width = 2;
let polygonSides = 3;

var lastX, lastY;

//currently used tool
let currentTool = 'brush';

//canvas dimensions
let canvasWidth = 600;
let canvasHeight = 600;

//is brush currently used
let usingBrush = false;

//Array of drawings
var DrawingArray = new Array();

//represents box that shape is drawn in
class ShapeBoundingBox{
    constructor(left, top, width, height) {
        this.left = left;
        this.top = top;
        this.width = width;
        this.height = height;
    }
}

//represents a drawing
class Drawing{
    constructor(){
        this.PointArray = new Array();
    }

    draw(){
        for(let i = 0; i < this.PointArray.length; i++){
            ctx.strokeStyle = this.PointArray[i].color;
            ctx.lineWidth = this.PointArray[i].width;
            ctx.lineCap = "round";
            ctx.beginPath();
            ctx.moveTo(this.PointArray[i].x, this.PointArray[i].y);
            if (i != this.PointArray.length - 1){
                ctx.lineTo(this.PointArray[i+1].x, this.PointArray[i+1].y);
            }
            ctx.stroke();
        }
    }

    addPoint(point){
        this.PointArray.push(point);
    }
}

//represents a point
class Point{
    constructor(x, y, color, width){
        this.x = x;
        this.y = y;
        this.color = color;
        this.width = width;
    }
}


//represents x,y coordinates of mouse down location
class MouseDownPos{
    constructor(x,y) {
        this.x = x,
        this.y = y;
    }
}

//represents x,y coordinate of current mouse position
class Location{
    constructor(x,y) {
        this.x = x,
        this.y = y;
    }
}

let shapeBoundingBox = new ShapeBoundingBox(0,0,0,0);
let mousedown = new MouseDownPos(0,0);
let loc = new Location(0,0);
var CurrentDrawing = new Drawing();

//load page
document.addEventListener('DOMContentLoaded', setupCanvas);

function setupCanvas(){
    canvas = document.getElementById('my-canvas');
    ctx = canvas.getContext('2d');
    ctx.strokeStyle = strokeColor;
    ctx.lineWidth = line_Width;
    //add mouse listeners
    canvas.addEventListener("mousedown", ReactToMouseDown);
    canvas.addEventListener("mousemove", ReactToMouseMove);
    canvas.addEventListener("mouseup", ReactToMouseUp);
}

function ChangeTool(toolClicked){
    document.getElementById("open").className = "";
    document.getElementById("save").className = "";
    document.getElementById("brush").className = "";
    document.getElementById("line").className = "";
    document.getElementById("rectangle").className = "";
    document.getElementById("ellipse").className = "";
    document.getElementById("polygon").className = "";
    document.getElementById(toolClicked).className = "selected";
    currentTool = toolClicked;
}

function GetMousePosition(x,y){
    let canvasSizeData = canvas.getBoundingClientRect();
    return { x: (x - canvasSizeData.left) * (canvas.width  / canvasSizeData.width),
        y: (y - canvasSizeData.top)  * (canvas.height / canvasSizeData.height)
      };
}

function DrawBrush(x, y){
    if (usingBrush) {
        ctx.strokeStyle = strokeColor;
        ctx.lineWidth = line_Width;
        ctx.lineCap = "round";
        ctx.lineTo(x, y);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(x, y);
    }   
}

function SaveCanvasImage(){
    savedImageData = ctx.getImageData(0,0,canvas.width,canvas.height);
}

function RedrawCanvasImage(){
    ctx.putImageData(savedImageData,0,0);
}
 
function ReactToMouseDown(e){
    canvas.style.cursor = "crosshair";
    usingBrush = true;
    SaveCanvasImage();
    loc = GetMousePosition(e.clientX, e.clientY);
    let point = new Point(loc.x, loc.y, strokeColor, line_Width);
    CurrentDrawing.addPoint(point);
    DrawBrush(loc.x, loc.y);
};
 
function ReactToMouseMove(e){
    canvas.style.cursor = "crosshair";
    loc = GetMousePosition(e.clientX, e.clientY);
    let point = new Point(loc.x, loc.y, strokeColor, line_Width);
    CurrentDrawing.addPoint(point);
    DrawBrush(loc.x, loc.y);
};
 
function ReactToMouseUp(e){
    usingBrush = false;
    loc = GetMousePosition(e.clientX, e.clientY);
    let point = new Point(loc.x, loc.y, strokeColor, line_Width);
    CurrentDrawing.addPoint(point);
    ctx.beginPath();
    RedrawCanvasImage();
    CurrentDrawing.draw();
}