function wm_setup(elem) {
    var x = elem;

    x.getElementsByClassName("window-btn-minimise")[0].onclick = wm_minimise;
    x.getElementsByClassName("window-btn-maximise")[0].onclick = wm_maximise;
    x.onmousedown = wm_focus;

    var x_tb = document.getElementById(x.id+"-lstbtn");

    function wm_minimise(e) {
        x.style.display = "none";
        x.windowstate = "minimised";
        x_tb.classList.remove("nav-item-focused");
        x_tb.classList.add("nav-item-min");
    }

    function wm_restore(e) {
        x.style.display = "block";
        x.windowstate = "focused";
        x_tb.classList.add("nav-item-focused");
        x_tb.classList.remove("nav-item-min");
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
        var windows = document.getElementsByClassName("draggable");

        for (var i = 0; i < windows.length; i++) {
            if (windows[i] != x) {
                windows[i].windowstate = "unfocused";
                windows[i].classList.remove("card-tertiary");
                document.getElementById(windows[i].id+"-lstbtn").classList.remove("nav-item-focused");

                if (windows[i].style.zIndex > x.style.zIndex) {
                    windows[i].style.zIndex = (parseInt(windows[i].style.zIndex)-2).toString();

                    children = windows[i].children;
                    for (var j = 0; j < children.length; j++) {
                        if (children[j] != windows[i]) {
                            children[j].style.zIndex = (parseInt(windows[i].style.zIndex)-2).toString();
                        }
                    }
                }
            }
        }

        x.windowstate = "focused";
        x.classList.add("card-tertiary");
        x.style.zIndex = (windows.length*2 - 2).toString();
        x_tb.classList.add("nav-item-focused");
    }

    function wm_unfocus(e) {
        if (e.target == document.body) {
            x.windowstate = "unfocused";
            x.classList.remove("card-tertiary");
            x_tb.classList.remove("nav-item-focused");
        }
    }
}

function wl_setup(elem, w_id) {
    var x = document.getElementById(w_id);
    var x_tb = document.getElementById(x.id+"-lstbtn");

    elem.onclick = wm_restore_minimise_toggle;

    function wm_restore_minimise_toggle(e) {
        if (x.style.display === "none") {
            x.style.display = "block";
            x.windowstate = "focused";
            x.onmousedown("");

            x_tb.classList.toggle("nav-item-min", false);
            x_tb.classList.add("nav-item-focused");
        } else if (x.windowstate == "focused") {
            x.style.display = "none";
            x.windowstate = "minimised";
            x_tb.classList.add("nav-item-min");
            x_tb.classList.remove("nav-item-focused");
        } else {
            x.windowstate = "focused";
            x.onmousedown("");
            x_tb.classList.add("nav-item-focused");
        }
    }
}

function unfocus_wins(e) {
    if (e.target == document.body) {
        console.log("unfocused");

        for (var i = 0; i < windows.length; i++) {
            windows[i].windowstate = "unfocused";
            windows[i].classList.remove("card-tertiary");
            document.getElementById(windows[i].id+"-lstbtn").classList.remove("nav-item-focused");
        }

        hide_start();
    }
}

function setupWindowManagement(class_name) {
    var windows = document.getElementsByClassName(class_name);

    for (var i = 0; i < windows.length; i++) {
        wm_setup(windows[i]);
    }

    for (var i = 0; i < windows.length; i++) {
        windows[i].onmousedown("");
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
