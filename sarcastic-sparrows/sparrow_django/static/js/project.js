// Project JS goes here

function updateColors() {
    let bg = document.getElementById("bg-color-picker");
    let fg = document.getElementById("fg-color-picker");
    let bgColor = bg.value.substr(1);
    let fgColor = fg.value.substr(1);

    const request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (request.readyState === 4 && request.status === 200)
            alert("Color successfully updated!");
            window.location.reload();
    };
    request.open("GET", `/api?action=color&fg=${bgColor}&bg=${fgColor}`, true);
    request.send(null);
}

function showColorSelector() {
    document.getElementById("select-color").style.display = "unset";
}


if (window.location.pathname === "/") {
    document.getElementsByTagName("body")[0].style = "margin:0;padding:0";

    setInterval(function(){
        let iframe = document.getElementById("main-iframe");
        if (iframe) {
            iframe.width = window.innerWidth;
            iframe.height = window.innerHeight - 12;
        }
    }, 100);
}
