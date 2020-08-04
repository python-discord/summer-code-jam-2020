function setup_start() {
    var start = document.getElementById("start-menu");
    var taskbar = document.getElementById("taskbar");
    var startbutton = document.getElementById("start-button");
    var startbanner = document.getElementsByClassName("start-banner")[0];

    taskbar.style.zIndex = document.getElementsByClassName("draggable").length;

    start.style.top = ((window.innerHeight - document.getElementById("taskbar").offsetHeight) - start.offsetHeight).toString()+"px";
    start.style.left = "0px";
    start.style.display = "none";
}

function toggle_start() {
    var start = document.getElementById("start-menu")

    if (start.style.display == "none") {
        start.style.display = "block";
        start.style.zIndex = document.getElementsByClassName("draggable").length;
    } else {
        start.style.display = "none";
    }
}
