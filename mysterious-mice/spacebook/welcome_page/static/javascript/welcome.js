function pan_up() {
    var stars = document.getElementById("star_holder");
    var button_zoom = document.getElementsByClassName("button_zoom");
    var button_size = 100;
    var star_width = 0;
    var id = setInterval(frame, 5);

    function frame() {
        if (star_width >= 100) {
            clearInterval(id);
            window.location.replace("/home");
        } else {
            star_width += 5;
            button_size -= 5;
            stars.style.width = star_width + '%';
            stars.style.height = star_width + '%';
            for (i = 0; i < button_zoom.length; i++) {
                button_zoom[i].style.scale = button_size + "%";
                button_zoom[i].style.zoom = button_size + "%";
                if (button_size == 0) {
                    button_zoom[i].style.visibility = "hidden";
                }
            }

        }
    }
}
