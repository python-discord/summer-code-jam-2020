function dragElement(elmnt_class, elmnt_index) {

    elmnt = document.getElementsByClassName(elmnt_class)[elmnt_index];
    elmnt_header = document.getElementsByClassName(elmnt_class+"-header")[elmnt_index];

    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;

    elmnt_header.onmousedown = dragMouseDown;

    function dragMouseDown(e) {

        e = e || window.event;
        e.preventDefault();

        // get the mouse cursor position at startup:
        pos3 = e.clientX;
        pos4 = e.clientY;

        document.onmouseup = closeDragElement;

        // call a function whenever the cursor moves:
        document.onmousemove = elementDrag;
    }

    function elementDrag(e) {

        e = e || window.event;
        e.preventDefault();

        // calculate the new cursor position:
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;

        // set the element's new position:
        elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
        elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";

    }

    function closeDragElement() {

        /* stop moving when mouse button is released:*/
        document.onmouseup = null;
        document.onmousemove = null;

    }
}

function loadDraggableElements(class_name) {
    elements = document.getElementsByClassName(class_name);

    for (var n = 0; n < elements.length; n++) {

        dragElement(class_name, n);

    }

}
