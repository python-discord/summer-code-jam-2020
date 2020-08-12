function get_window_list (class_name) {
    var windows = document.getElementsByClassName(class_name);

    var window_titles = [];
    var window_ids = [];
    var titlebar;

    for (var i = 0; i < windows.length; i++) {
        titlebar = windows[i].getElementsByClassName(class_name+"-header")[0];
        window_titles[i] = [].reduce.call(titlebar.childNodes, function(a, b) { return a + (b.nodeType === 3 ? b.textContent : ''); }, '').trim();
        window_ids[i] = windows[i].id;
    }

    return [window_titles, window_ids];
}

function create_window_list_btn (navbar, name, windowid) {
    var btn = document.createElement("li");
    btn.classList = ["nav-item"];
    btn.id = windowid+"-lstbtn";

    var link = document.createElement("a");
    link.classList = ["nav-link"];

    var span = document.createElement("span");
    span.classList = ["nav-link-inner-text"];
    span.appendChild(document.createTextNode(name));

    if (document.getElementById(windowid).getElementsByClassName("header-icon").length > 0) {
        var icon = document.getElementById(windowid).getElementsByClassName("header-icon")[0].cloneNode(true);
        icon.classList = ["nav-link-icon"];
        link.appendChild(icon);
    }

    link.appendChild(span);
    btn.appendChild(link);
    navbar.appendChild(btn);

    wl_setup(link, windowid);
}

function create_window_list(navbar_class, class_name) {
    var navbar = document.getElementsByClassName(navbar_class)[0];

    var windowsinfo = get_window_list(class_name);

    var window_titles = windowsinfo[0];
    var window_ids = windowsinfo[1];

    for (var i = 0; i < window_titles.length; i++) {
        create_window_list_btn(navbar, window_titles[i], window_ids[i]);
    }
}
