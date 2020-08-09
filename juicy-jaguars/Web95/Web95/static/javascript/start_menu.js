function setup_start() {
    var start = document.getElementById("start-menu");
    var taskbar = document.getElementById("taskbar");
    var startbutton = document.getElementById("start-button");
    var startbanner = document.getElementsByClassName("start-banner")[0];

    var start_settings = document.getElementsByClassName("start-settings")[0];
    var start_settings_button = start.getElementsByClassName("start-level1")[2];

    var start_themes = document.getElementsByClassName("start-themes")[0];
    var start_themes_button = document.getElementsByClassName("start-lvl2-item")[0];

    var start_walls = document.getElementsByClassName("start-wallpapers")[0];
    var start_walls_button = document.getElementsByClassName("start-lvl2-item")[1];

    var start_font = document.getElementsByClassName("start-font")[0];
    var start_font_button = document.getElementsByClassName("start-lvl2-item")[2];

    taskbar.style.zIndex = document.getElementsByClassName("draggable").length*2;

    start.style.top = ((window.innerHeight - document.getElementById("taskbar").offsetHeight) - start.offsetHeight).toString()+"px";
    start.style.left = "0px";

    start_settings.style.top = start_settings_button.getBoundingClientRect().top.toString()+"px";
    start_settings.style.left = (start_settings_button.getBoundingClientRect().right-5).toString()+"px";

    start_themes.style.top = start_themes_button.getBoundingClientRect().top.toString()+"px";
    start_themes.style.left = (start_themes_button.getBoundingClientRect().right-5).toString()+"px";

    start_walls.style.top = start_walls_button.getBoundingClientRect().top.toString()+"px";
    start_walls.style.left = (start_walls_button.getBoundingClientRect().right-5).toString()+"px";

    start_font.style.top = start_font_button.getBoundingClientRect().top.toString()+"px";
    start_font.style.left = (start_font_button.getBoundingClientRect().right-5).toString()+"px";

    start.style.display = "none";
    start_settings.style.display = "none";
    start_themes.style.display = "none";
    start_walls.style.display = "none";
    start_font.style.display = "none";
}

function toggle_start() {
    var start = document.getElementById("start-menu");
    var start_lvl2 = document.getElementsByClassName("start-lvl2");
    var start_lvl3 = document.getElementsByClassName("start-lvl3");

    if (start.style.display == "none") {
        start.style.display = "block";
        start.style.zIndex = document.getElementsByClassName("draggable").length*2;

        for (var i = 0; i < start_lvl2.length; i++) {
            start_lvl2[i].style.zIndex = document.getElementsByClassName("draggable").length+1;
            start_lvl2[i].style.display = "none";
        }

        for (var i = 0; i < start_lvl3.length; i++) {
            start_lvl3[i].style.zIndex = document.getElementsByClassName("draggable").length+2;
            start_lvl3[i].style.display = "none";
        }
    } else {
        start.style.display = "none";

        for (var i = 0; i < start_lvl2.length; i++) {
            start_lvl2[i].style.display = "none";
        }

        for (var i = 0; i < start_lvl3.length; i++) {
            start_lvl3[i].style.display = "none";
        }
    }
}

function toggle_start_settings() {
    var start_settings = document.getElementsByClassName("start-settings")[0];
    var start_themes = document.getElementsByClassName("start-themes")[0];
    var start_wallpapers = document.getElementsByClassName("start-wallpapers")[0];

    if (start_settings.style.display == "none") {
        start_settings.style.display = "block";
        start_settings.style.zIndex = (document.getElementsByClassName("draggable").length*2)+1;
    } else {
        start_settings.style.display = "none";
        start_themes.style.display = "none";
        start_wallpapers.style.display = "none";
    }
}

function toggle_start_themes() {
    var start_themes = document.getElementsByClassName("start-themes")[0];
    var start_wallpapers = document.getElementsByClassName("start-wallpapers")[0];
    var start_font = document.getElementsByClassName("start-font")[0];

    if (start_themes.style.display == "none") {
        start_themes.style.display = "block";
        start_themes.style.zIndex = (document.getElementsByClassName("draggable").length*2)+2;

        start_wallpapers.style.display = "none";
        start_font.style.display = "none";
    } else {
        start_themes.style.display = "none";
    }
}

function toggle_start_wallpapers() {
    var start_wallpapers = document.getElementsByClassName("start-wallpapers")[0];
    var start_themes = document.getElementsByClassName("start-themes")[0];
    var start_font = document.getElementsByClassName("start-font")[0];

    if (start_wallpapers.style.display == "none") {
        start_wallpapers.style.display = "block";
        start_wallpapers.style.zIndex = (document.getElementsByClassName("draggable").length*2)+2;

        start_themes.style.display = "none";
        start_font.style.display = "none";
    } else {
        start_wallpapers.style.display = "none";
    }
}

function toggle_start_font() {
    var start_wallpapers = document.getElementsByClassName("start-wallpapers")[0];
    var start_themes = document.getElementsByClassName("start-themes")[0];
    var start_font = document.getElementsByClassName("start-font")[0];

    if (start_font.style.display == "none") {
        start_font.style.display = "block";
        start_font.style.zIndex = (document.getElementsByClassName("draggable").length*2)+2;

        start_wallpapers.style.display = "none";
        start_themes.style.display = "none";
    } else {
        start_font.style.display = "none";
    }
}

function fontsize_up() {
    var elems = document.getElementsByTagName("*");
    var numVal = 0;
    var unit = "";

    for (var i = 0; i < elems.length; i++) {
        numVal = parseFloat(window.getComputedStyle(elems[i]).fontSize);
        console.log(window.getComputedStyle(elems[i]).fontSize);
        if (numVal != NaN) {
            unit = window.getComputedStyle(elems[i]).fontSize.replace(numVal.toString(), "");
            elems[i].style.fontSize = (numVal*1.25).toString() + unit;
            console.log((numVal*0.8).toString() + unit);
            console.log(" ");
        }
    }
}

function fontsize_down() {
    var elems = document.getElementsByTagName("*");
    var numVal = 0;
    var unit = "";

    for (var i = 0; i < elems.length; i++) {
        numVal = parseFloat(window.getComputedStyle(elems[i]).fontSize);
        console.log(window.getComputedStyle(elems[i]).fontSize);
        if (numVal != NaN) {
            unit = window.getComputedStyle(elems[i]).fontSize.replace(numVal.toString(), "");
            elems[i].style.fontSize = (numVal*0.8).toString() + unit;
            console.log((numVal*0.8).toString() + unit);
            console.log(" ");
        }
    }
}

function hide_start() {
    var start = document.getElementById("start-menu");
    var start_settings = document.getElementsByClassName("start-settings")[0];
    var start_themes = document.getElementsByClassName("start-themes")[0];
    var start_font = document.getElementsByClassName("start-font")[0];

    start.style.display = "none";
    start_settings.style.display = "none";
    start_themes.style.display = "none";
    start_font.style.display = "none";
}
