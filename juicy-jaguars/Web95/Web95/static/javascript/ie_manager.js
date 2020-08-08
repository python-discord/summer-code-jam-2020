function ie_home() {
    document.getElementById("ie-addr-bar").value = "http://www.google.com";
    ie_refresh();
}

function ie_refresh() {
    if (document.getElementById("ie-addr-bar").value == "about:blank") {
        document.getElementById("ie-iframe").src = document.getElementById("ie-addr-bar").value;
    } else {
        document.getElementById("ie-iframe").src = "/page/"+encodeURIComponent(document.getElementById("ie-addr-bar").value);
    }
}

function ie_blank() {
    document.getElementById("ie-addr-bar").value = "about:blank";
    ie_refresh();
}

function addr_bar_enter() {
    ie_refresh();
}

document.getElementById("ie-addr-bar").addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        addr_bar_enter();
    }
});
