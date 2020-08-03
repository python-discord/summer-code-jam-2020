function dragElement(elmnt_class, elmnt_index) {

    elmnt = document.getElementsByClassName(elmnt_class)[elmnt_index];
    elmnt_header = document.getElementsByClassName(elmnt_class+"-header")[elmnt_index];

    var deltaX = 0, deltaY = 0, mouseX = 0, mouseY = 0;

    elmnt_header.onmousedown = dragMouseDown;

    function dragMouseDown(e) {

        e = e || window.event;
        e.preventDefault();

        if ( e.target.classList.contains(elmnt_class+"-header") ) {

            // get the mouse cursor position at startup:
            mouseX = e.clientX;
            mouseY = e.clientY;

            document.onmouseup = closeDragElement;

            // call a function whenever the cursor moves:
            document.onmousemove = elementDrag;

        }
    }

    function elementDrag(e) {

        e = e || window.event;
        e.preventDefault();

        if ( e.target.classList.contains(elmnt_class+"-header") ) {

            // calculate the new cursor position:
            deltaX = e.clientX - mouseX;
            deltaY = e.clientY - mouseY;
            mouseX = e.clientX;
            mouseY = e.clientY;

            // set the element's new position:
            e.target.parentElement.style.left = (e.target.parentElement.offsetLeft + deltaX) + "px";
            e.target.parentElement.style.top = (e.target.parentElement.offsetTop + deltaY) + "px";

        }

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
