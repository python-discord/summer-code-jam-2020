function get_window_list (class_name) {
    var windows = document.getElementsByClassName(class_name);

    var window_titles = [];
    var window_ids = [];
    var titlebar;

    for (var i = 0; i < windows.length; i++) {
        titlebar = windows[i].getElementsByClassName(class_name+"-header")[0];
        window_titles[i] = [].reduce.call(titlebar.childNodes, function(a, b) { return a + (b.nodeType === 3 ? b.textContent : ''); }, '').trim();
        window_ids[i] = windows[i].id
    }

    return [window_titles, window_ids];
}

function create_window_btn (navbar, name, windowid) {
    var btn = document.createElement("li");
    btn.classList = ["nav-item"];

    var link = document.createElement("a");
    link.classList = ["nav-link"];
    link.onclick = "wm_restore(" + windowid + ")"

    var span = document.createElement("span");
    span.classList = ["nav-link-inner-text"];
    span.appendChild(document.createTextNode(name));

    link.appendChild(span);
    btn.appendChild(link);
    navbar.appendChild(btn);
}

function create_buttons(navbar, class_name) {
    var windowsinfo = get_window_list(class_name);
    var window_titles = windowsinfo[0]
    var window_ids = windowsinfo[1]

    for (var i = 0; i < window_titles.length; i++) {
        create_window_btn(navbar, window_titles[i], window_ids[i]);
    }
}

console.log(get_window_list("draggable"));

// <li class="nav-item">
//     <a href="#" class="nav-link" role="button">
//         <span class="nav-link-inner-text">
//             <img src="{% static 'images/start.svg' %}" height="20px" margin=auto>
//             Start
//         </span>
//     </a>
// </li>
