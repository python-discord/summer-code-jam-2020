// Functions for Interactive File Menu Bar 
// - Click Butoon to Open Dropdown
// - Clicking one dropdown closes all other
// - Clicking outside the file menu bar will close all the dropdown.

function open_dropdown(element_id) {
  console.log('Opening Dropdown:', element_id)
  close_all_dropdowns()
  document.getElementById(element_id).style.display = 'block';
}

// Close the dropdown if the user clicks outside of it
function close_dropdown(element) {
  console.log('I am closing dropdown:', element)
  element.style.display = 'none'
}

// Close all dropdowns.
function close_all_dropdowns() {
  var dropdowns = document.getElementsByClassName('dropdown-content')
  for (var i = 0; i < dropdowns.length; i++) {
    close_dropdown(dropdowns[i]);
  }
}

// Close all dropdowns when clicking outside.
window.onclick = function (e) {
  if (!e.target.matches('.dropbtn')) {
    close_all_dropdowns()
  }
}

