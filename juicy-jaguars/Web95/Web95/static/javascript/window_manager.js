function wm_minimise(divId) {
    var x = document.getElementById(divId);
    x.style.display = "none";
    x.windowstate = "minimised";
}

function wm_restore(divId) {
    var x = document.getElementById(divId);
    x.style.display = "block";
    x.windowstate = "focused";
}

function wm_restore_minimise_toggle(divId) {
    var x = document.getElementById(divId);
    if (x.style.display === "none") {
        x.style.display = "block";
        x.windowstate = "focused";
    } else {
        x.style.display = "none";
        x.windowstate = "minimised";
    }
}

function wm_maximise(divId) {
    var x = document.getElementById(divId);

    if (x.maximised == "true") {
        x.style.top = x.oldtop, x.style.left = x.oldleft;
        x.style.width = x.oldwidth.toString()+"px";
        x.style.height = x.oldheight.toString()+"px";

        x.maximised = "false";
    } else {
        x.oldtop = x.style.top, x.oldleft = x.style.left;
        x.style.top = "0px", x.style.left = "0px";

        x.oldwidth = x.offsetWidth, x.oldheight = x.offsetHeight;
        x.style.width = (window.innerWidth).toString()+"px";
        x.style.height = (window.innerHeight - document.getElementById("taskbar").offsetHeight).toString()+"px";

        x.maximised = "true";

        console.log(window.innerWidth.toString()+"px");
    }
}

function wm_focus(divId) {
    var x = document.getElementById(divId);

    x.windowstate = "focused";
}

function wm_unfocus(divId) {
    var x = document.getElementById(divId);

    x.windowstate = "unfocused";
}

function setupWindowManagement(class_name) {
    var windows = document.getElementsByClassName(class_name);
    console.log(windows.length);

    for (var i = 0; i < windows.length; i++) {
        windows[i].getElementsByClassName("window-btn-minimise")[0].onclick = function(e) {wm_minimise(e.target.parentElement.parentElement.id)};
        windows[i].getElementsByClassName("window-btn-maximise")[0].onclick = function(e) {wm_maximise(e.target.parentElement.parentElement.id)};
    }
}

/*
function wm_minimise(divClass) {
    var x = document.getElementsByClassName(divClass);
    for (var i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
}

function wm_restore(divClass) {
    var x = document.getElementsByClassName(divClass);
    for (var i = 0; i < x.length; i++) {
        x[i].style.display = "block";
    }
}
*/
