<template>
  <div>
    <h2>Login</h2>
    <span class="login-message">
      Enter your username (or /register to create a new account)
    </span>
  </div>
</template>

<style>
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  computed: {
    isLogin() {
      return this.$route.name === 'login_page';
    },
  },
  methods: {
    login() {
      axios.post('/api/login', {
        username: this.username,
        password: this.password,
      }).then(() => {
        this.$router.push('/');
      }).catch((err) => {
        console.log(err); // eslint-disable-line no-console
      });
    },
    register() {
      axios.post('/api/register', {
        username: this.username,
        password: this.password,
      }).then(() => {
        this.$router.push('/');
      }).catch((err) => {
        console.log(err); // eslint-disable-line no-console
      });
    },
  },
};
</script>
