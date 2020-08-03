function window_setup () {
    createWindowIds("draggable");

    loadDraggableElements("draggable");

    create_window_list("navbar-nav", "draggable");

    loadButtonEffects();

    setupWindowButtons("draggable");
}
