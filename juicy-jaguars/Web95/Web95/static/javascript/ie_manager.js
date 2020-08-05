function addr_bar_enter() {
    //document.getElementById("ie-iframe").src = "https://test.com/";
    document.getElementById("ie-iframe").src = "/page/"+encodeURIComponent(document.getElementById("ie-addr-bar").value);
    console.log("/page/"+encodeURI(document.getElementById("ie-addr-bar").value));
}

document.getElementById("ie-addr-bar").addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        addr_bar_enter();
    }
});
