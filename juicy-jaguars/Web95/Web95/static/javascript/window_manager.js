function wm_minimise(divId) {
    var x = document.getElementById(divId);
    x.style.display = "none";
}

function wm_restore(divId) {
    var x = document.getElementById(divId);
    x.style.display = "block";
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