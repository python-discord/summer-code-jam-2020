// Project JS goes here

if (window.location.pathname === "/") {
    let body = document.getElementsByTagName("body")[0];
    body.style = "margin:0;padding:0"

    setInterval(function(){
        let iframe = document.getElementById("main-iframe")
        if (iframe) {
            iframe.width = window.innerWidth;
            iframe.height = window.innerHeight - 12;
        }
    }, 100);
}