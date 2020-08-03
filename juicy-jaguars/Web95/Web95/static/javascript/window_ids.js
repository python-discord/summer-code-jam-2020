function createWindowIds(class_name) {
    windows = document.getElementsByClassName(class_name);

    for (var i = 0; i < windows.length; i++) {
        windows[i].id = "window"+i.toString();
    }
}
