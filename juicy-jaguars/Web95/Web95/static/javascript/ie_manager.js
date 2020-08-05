function addr_bar_enter() {
    //document.getElementById("ie-iframe").src = "https://test.com/";
    document.getElementById("ie-iframe").src = "/page/"+encodeURI(document.getElementById("ie-addr-bar").value);
}

document.getElementById("ie-addr-bar").addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        addr_bar_enter();
    }
});
