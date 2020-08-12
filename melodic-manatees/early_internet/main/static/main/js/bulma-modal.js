let button = document.getElementById('journal-btn');
let modal = document.getElementById('journal-modal');
let closeX = document.getElementById('close-x');
let cancelButton = document.getElementById('cancel-btn');

function openModal() {
    modal.classList.add('is-active');
}
function closeModal() {
    modal.classList.remove('is-active');
}

button.onclick = openModal;

closeX.onclick = closeModal;

cancelButton.onclick = closeModal;

window.onclick = function (event) {
    if (event.target.className == 'modal-background') {
        closeModal();
    }
}
