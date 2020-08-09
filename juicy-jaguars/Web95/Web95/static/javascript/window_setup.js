function window_setup () {

    createWindowIds("draggable");

    loadDraggableElements("draggable");

    create_window_list("navbar-nav", "draggable");

    loadButtonEffects();

    setupWindowManagement("draggable");

    setup_start();

    document.body.onmousedown = unfocus_wins;
}
