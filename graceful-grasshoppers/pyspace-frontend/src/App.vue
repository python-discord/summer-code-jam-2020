<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>|
      <div style="display: inline-block;" v-if="!loggedIn">
        <router-link to="/register">Register</router-link>|
      </div>
      <div style="display: inline-block;" v-if="!loggedIn">
        <router-link to="/login">Login</router-link>
      </div>
      <div style="display: inline-block;" v-if="loggedIn">
        <router-link to="/profile">Profile</router-link>|
      </div>
      <div style="display: inline-block;" v-if="loggedIn">
        <router-link to="/create-post">New Post</router-link>
      </div>
      <input type="submit" v-if="loggedIn" style="float: right;" v-on:click="logout" value="Logout">
    </div>
    <router-view />
  </div>
</template>

<script>
// import UserService from './services/user.service';
export default {
  name: 'app',
  data() {
    return {}
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  mounted() {
    if (this.loggedIn) {
      // check if already authorized...
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('auth/logout');
    }
  }
}
</script>

<style>
body {
  background: #eee;
}

#app {
  font-family: 'Times New Roman';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.flex-col {
    display: flex;
    flex-direction: column;
    max-width: 300px;
}

input {
  margin: 2px 0 !important;
}

button {
  border: 1px solid black;
  border-radius: 4px !important;
  padding: 5px;
  margin: 5px 0 !important;
}

</style>
