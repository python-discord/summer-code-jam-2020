<template>
<div id="app">
  <div id="nav" class="alert-dark">
    <p class="alert-info m-0 font-weight-bold">pyspace.net</p>
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
      <router-link to="/friends">Friends</router-link>|
    </div>
    <div style="display: inline-block;" v-if="loggedIn">
      <router-link to="/random">Random</router-link>|
    </div>
    <div style="display: inline-block;" v-if="loggedIn">
      <router-link to="/editprofile">Edit Profile</router-link>|
    </div>
    <div style="display: inline-block;" v-if="loggedIn">
      <router-link to="/posts">Posts</router-link>|
    </div>
    <div style="display: inline-block;" v-if="loggedIn">
      <router-link to="/create-post">New Post</router-link>
    </div>
    <button type="submit" v-if="loggedIn" style="width: 100px; float: right;" v-on:click="logout">Logout</button>
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
* {
  margin: 2px;
}
body {
  background: #ccc;
}
#app {
  font-family: 'DejaVu Sans';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0;
}
#nav {
  margin: 0 !important;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
}
.flex-col {
  display: flex;
  flex-direction: column;
}
.flex-row {
  display: flex;
  flex-direction: row;
}
.bordered {
  border: 1px solid black;
}
input {
  margin: 2px 0 !important;
}
button {
  border: 1px solid black;
  padding: 5px;
  width: 100%;
  margin: 5px 0 !important;
}
li {
  list-style: none;
}
</style>