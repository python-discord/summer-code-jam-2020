<template>
  <div>
    <form @submit.prevent="onSubmit" class="flex-col">
        <label for="input-1">Username</label>
        <input
          id="input-1"
          v-model="user.username"
          type="text"
          required
          placeholder="Enter username">

        <label for="input-2">Password</label>
        <input
          id="input-2"
          v-model="user.password"
          type="password"
          required
          placeholder="Enter password">

        <input type="submit" value="Login" class="form-group">
      <div class="form-group">
        <div v-if="message" class="alert-danger" role="alert">{{message}}</div>
      </div>
    </form>
  </div>
</template>

<script>
import User from '../models/user';
export default {
  name: 'Login',
  data() {
    return {
      user: new User('', ''),
      message: '',
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  created() {
    if (this.loggedIn) {
      this.$router.push('/')
    }
  },
  methods: {
    onSubmit() {
      if (this.user.username && this.user.password) {
        this.$store.dispatch('auth/login', this.user).then(
          () => {
            this.$router.push('/');
          },
          error => {
            this.message = error;
        });
      }
    }
  }
};
</script>

<style>
</style>