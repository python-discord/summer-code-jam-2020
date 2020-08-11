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

// Function to display current time. Updates every .5 secs. 
// so feels like a normal digital clock.
function startTime() {
  var today = new Date();
  var h = today.getHours();
  var m = today.getMinutes();
  var s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('time').innerHTML = h + ":" + m + ":" + s;
  setTimeout(startTime, 500);
}

// add 0 padding for numbers less than 10.
function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}

