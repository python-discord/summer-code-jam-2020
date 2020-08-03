function wm_minimise(divclass) {
    var x = document.getElementsByClassName(divclass);
    for (var i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
}

function wm_restore(divclass) {
    var x = document.getElementsByClassName(divclass);
    for (var i = 0; i < x.length; i++) {
        x[i].style.display = "block";
    }
}