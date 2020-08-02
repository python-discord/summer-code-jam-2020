import axios from "../http-common";

class AuthService {
  login(user) {
    return axios
      .post("/rest-auth/login", {
        username: user.username,
        password: user.password,
      })
      .then((response) => {
        if (response.data.key) {
          localStorage.setItem("user", JSON.stringify(response.data));
        } else if (response.data.error) {
          return Promise.reject(response.data.error);
        }

        return response.data;
      });
  }

  logout() {
    // post request to logout
    localStorage.removeItem("user");
  }

  register(user, confirmPassword) {
    return axios
      .post("/rest-auth/registration", {
        username: user.username,
        email: user.email,
        password1: user.password,
        password2: confirmPassword,
      })
      .then((response) => {
        if (response.data.error) {
          return Promise.reject(response.data.error);
        }

        return response;
      });
  }
}

export default new AuthService();
