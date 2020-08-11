function createWindowIds(class_name) {
    windows = document.getElementsByClassName(class_name);
    var children;

    for (var i = 0; i < windows.length; i++) {
        windows[i].id = "window"+i.toString();
        windows[i].style.zIndex = i*2;

        children = windows[i].children;
        for (var j = 0; j < children.length; j++) {
            children[j].style.zIndex = (i*2)+1;
        }
    }
}
