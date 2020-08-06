function ie_home() {
    document.getElementById("ie-addr-bar").value = "http://bing.com";
    ie_refresh();
}

function ie_refresh() {
    document.getElementById("ie-iframe").src = "/page/"+encodeURIComponent(document.getElementById("ie-addr-bar").value);
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
