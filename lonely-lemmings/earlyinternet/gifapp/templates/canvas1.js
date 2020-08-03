let canvas;
let ctx;
let dragging = false;
let strokeColor = 'black';
let fillColor = 'black';
let line_Width = 2;

var lastX, lastY;

//currently used tool
let currentTool = 'brush';

//canvas dimensions
let canvasWidth = 600;
let canvasHeight = 600;

//is brush currently used
let usingBrush = false;

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

let mousedown = new MouseDownPos(0,0);
let loc = new Location(0,0);

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
    lastX = x;
    lastY = y;      
}
 
function ReactToMouseDown(e){
    usingBrush = true;
    loc = GetMousePosition(e.clientX, e.clientY);
    DrawBrush(loc.x, loc.y);
};
 
function ReactToMouseMove(e){
    canvas.style.cursor = "crosshair";
    loc = GetMousePosition(e.clientX, e.clientY);
    DrawBrush(loc.x, loc.y);
};
 
function ReactToMouseUp(e){
    usingBrush = false;
    ctx.beginPath();
}