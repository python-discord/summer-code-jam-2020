function setup_start() {
    var start = document.getElementById("start-menu");
    var taskbar = document.getElementById("taskbar");
    var startbutton = document.getElementById("start-button");
    var startbanner = document.getElementsByClassName("start-banner")[0];

    var start_settings = document.getElementsByClassName("start-settings")[0];
    var start_settings_button = start.getElementsByClassName("start-level1")[2];

    taskbar.style.zIndex = document.getElementsByClassName("draggable").length;

    start.style.top = ((window.innerHeight - document.getElementById("taskbar").offsetHeight) - start.offsetHeight).toString()+"px";
    start.style.left = "0px";

    start_settings.style.top = start_settings_button.getBoundingClientRect().top.toString()+"px";
    start_settings.style.left = (start_settings_button.getBoundingClientRect().right-5).toString()+"px";

    console.log(start_settings_button.offsetTop.toString()+"px");
    console.log((start_settings_button.offsetLeft + start_settings_button.offsetWidth).toString()+"px");

    start.style.display = "none";
    start_settings.style.display = "none";
}

function toggle_start() {
    var start = document.getElementById("start-menu");
    var start_settings = document.getElementsByClassName("start-settings")[0];

    if (start.style.display == "none") {
        start.style.display = "block";
        start_settings.style.display = "none";

        start.style.zIndex = document.getElementsByClassName("draggable").length;
        start_settings.style.zIndex = document.getElementsByClassName("draggable").length+1;
    } else {
        start.style.display = "none";
        start_settings.style.display = "none";
    }
}

function toggle_start_settings() {
    var start_settings = document.getElementsByClassName("start-settings")[0];

    if (start_settings.style.display == "none") {
        start_settings.style.display = "block";
        start_settings.style.zIndex = document.getElementsByClassName("draggable").length+1;
    } else {
        start_settings.style.display = "none";
    }
}
