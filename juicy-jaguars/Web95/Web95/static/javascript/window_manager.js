function wm_minimise(divId) {
    var x = document.getElementById(divId);
    x.style.display = "none";
}

function wm_restore(divId) {
    var x = document.getElementById(divId);
    x.style.display = "block";
}

function wm_maximise(divId) {
    var x = document.getElementById(divId);

    if (x.maximised == "true") {
        x.style.top = x.oldtop, x.style.left = x.oldleft;
        x.style.width = x.oldwidth.toString()+"px";
        x.style.height = x.oldheight.toString()+"px";

        x.maximised = "false";

        console.log("unmax");
    } else {
        x.oldtop = x.style.top, x.oldleft = x.style.left;
        x.style.top = "0px", x.style.left = "0px";

        x.oldwidth = x.offsetWidth, x.oldheight = x.offsetHeight;
        x.style.width = (window.innerWidth).toString()+"px";
        x.style.height = (window.innerHeight - document.getElementById("taskbar").offsetHeight).toString()+"px";

        x.maximised = "true";

        console.log(window.innerWidth.toString()+"px");

        console.log("max");
    }
}

function setupWindowButtons(class_name) {
    var windows = getElementsByClassName(className);

    for (var i = 0; i < windows.length; i++) {
        windows.getElementsByClassName("window-btn-minimise").onclick = wm_minimise(windows[i].id);
        windows.getElementsByClassName("window-btn-maximise").onclick = wm_maximise(windows[i].id);
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
