function wm_setup(elem) {
    var x = elem;

    x.getElementsByClassName("window-btn-minimise")[0].onclick = wm_minimise;
    x.getElementsByClassName("window-btn-maximise")[0].onclick = wm_maximise;

    function wm_minimise(e) {
        x.style.display = "none";
        x.windowstate = "minimised";
    }

    function wm_restore(e) {
        x.style.display = "block";
        x.windowstate = "focused";
    }

    function wm_maximise(e) {
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

    function wm_focus(e) {
        x.windowstate = "focused";
        x.classList.add("card-tertiary");
    }

    function wm_unfocus(e) {
        x.windowstate = "unfocused";
        x.classList.remove("card-tertiary");
    }
}

function wl_setup(elem, w_id) {
    var x = document.getElementById(w_id);
    elem.onclick = wm_restore_minimise_toggle;
    function wm_restore_minimise_toggle(e) {
        if (x.style.display === "none") {
            x.style.display = "block";
            x.windowstate = "focused";
        } else {
            x.style.display = "none";
            x.windowstate = "minimised";
        }
    }
}

function setupWindowManagement(class_name) {
    var windows = document.getElementsByClassName(class_name);

    for (var i = 0; i < windows.length; i++) {
        wm_setup(windows[i])
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
