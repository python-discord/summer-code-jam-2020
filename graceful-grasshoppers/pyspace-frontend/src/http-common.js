import axios from "axios";

const server = {
  host: "localhost",
  port: "8000",
};

export default axios.create({
  baseURL: `http://${server.host}:${server.port}/api/v1`,
  headers: {
    "Content-type": "application/json",
  },
});
