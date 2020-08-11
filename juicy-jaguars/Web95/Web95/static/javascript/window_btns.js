function onPress(e) {
    e.target.classList.add("window-btn-pressed-active");
}

function onUnpress(e) {
    e.target.classList.remove("window-btn-pressed-active");
}

function loadButtonEffects() {
    buttons = document.getElementsByClassName("window-btn");
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].onmousedown = onPress;
        buttons[i].onmouseup = onUnpress;
        buttons[i].onmouseexit = onUnpress;
    }
}
