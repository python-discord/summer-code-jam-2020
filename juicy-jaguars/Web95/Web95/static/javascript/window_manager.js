function wm_hide(divclass) {
    var x = document.getElementsByClassName(divclass);
    for (var i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
}

function wm_show(divclass) {
    var x = document.getElementsByClassName(divclass);
    for (var i = 0; i < x.length; i++) {
        x[i].style.display = "block";
    }
}