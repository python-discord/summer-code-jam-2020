import Axios from 'axios';

const axios = Axios.create({
    baseURL: 'http://localhost:8000/api/',
    timeout: 5000,
    headers: {
        'Authorization': "JWT " + localStorage.getItem('access_token'),
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }
});

// Implement automatic Access Token refreshing
axios.interceptors.response.use(
    response => response,
    error => {
        const origin = error.config;

        if (error.response.status === 401 && error.response.statusText === "Unauthorized") {
            return axios.post('/token/refresh/', {refresh: localStorage.getItem('refresh_token')})
                .then((response) => {
                    localStorage.setItem('access_token', response.data.access);
                    axios.defaults.headers['Authorization'] = "JWT " + response.data.access;
                    origin.headers['Authorization'] = "JWT " + response.data.access;

                    return axios(origin);
                })
                .catch(err => {
                    console.log(err);
                    localStorage.removeItem('access_token');
                    localStorage.removeItem('refresh_token');
                    localStorage.removeItem('username');
                });
        }

        return Promise.reject(error);
    }
);

export default axios;
