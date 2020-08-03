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
      <button v-if="loggedIn" style="float: right;" v-on:click="logout">Logout</button>
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
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
</style>
