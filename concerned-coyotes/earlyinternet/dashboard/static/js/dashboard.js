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

updateClock();
setInterval(() => {
  updateClock(); 
 }, 1000);
