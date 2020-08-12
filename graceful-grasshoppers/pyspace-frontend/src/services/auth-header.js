export default function authHeader() {
  let user = JSON.parse(localStorage.getItem("user"));

  if (user && user.key) {
    return { Authorization: "Token " + user.key };
  } else {
    return {};
  }
}
