import axios from "../http-common";
import authHeader from "./auth-header";

class UserService {
  getUserBoard() {
    // example
    return axios.get("/user", { headers: authHeader() });
  }

  uploadPost(art) {
    return;
  }
}

export default new UserService();
