function updateClock() {
  let currentDate = new Date();

  // Get Minutes / Hours with leading zeros
  let hours = currentDate.getHours() < 10 ? "0" : "";
  hours += currentDate.getHours();

  let minutes = currentDate.getMinutes() < 10 ? "0" : "";
  minutes += currentDate.getMinutes();

  let timeString = `${hours}:${minutes}`;
  let dateString = currentDate.toLocaleDateString("en", {weekday: "long",  year: "numeric", month: "long", day: "numeric"});

  document.getElementById("time").innerText = timeString;
  document.getElementById("date").innerText = dateString;
}

function getLocation() {
  if (navigator.geolocation) {
    return navigator.geolocation
  } else {
    alert("Geolocation is not supported by this browser.");
  }
}

function updateLocationBtnClicked() {
  let url = document.getElementsByClassName("update-location-btn")[0].getAttribute("href");
  getLocation().getCurrentPosition((position) => {
    // Create url parameters with coordinates
    let params = new URLSearchParams();
    params.append("latitude", position.coords.latitude.toString());
    params.append("longitude", position.coords.longitude.toString());

    // url to redirect to
    let newUrl = `${url}?${params.toString()}`;
    window.location = newUrl;
  });

  return false;  
}

updateClock();
setInterval(() => {
  updateClock(); 
 }, 1000);
