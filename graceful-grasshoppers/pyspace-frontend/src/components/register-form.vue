<template>
  <div>
    <form @submit.prevent="onSubmit">
      <fieldset id="input-group-1" label="Username:" label-for="input-1">
        <input
          id="input-1"
          v-model="user.username"
          type="text"
          required
          placeholder="Enter username"
        >
      </fieldset>

      <fieldset id="input-group-2" label="Email:" label-for="input-2">
        <input
          id="input-2"
          v-model="user.email"
          type="email"
          required
          placeholder="Enter email"
        >
      </fieldset>

      <fieldset id="input-group-3" label="Password:" label-for="input-3">
        <input
          id="input-3"
          v-model="user.password"
          type="password"
          required
          placeholder="Enter password"
        >
      </fieldset>

      <fieldset id="input-group-4" label="Confirm Password:" label-for="input-4">
        <input
          id="input-4"
          v-model="confirmPassword"
          type="password"
          required
          placeholder="Confirm password"
        >
      </fieldset>

      <div class="fieldset">
        <button class="">
          <span>Register</span>
        </button>
      </div>
      <div class="fieldset">
        <div v-if="message" class="alert alert-danger" role="alert">{{message}}</div>
      </div>
    </form>
  </div>
</template>

<script>
import User from '../models/user';
export default {
  name: 'Register',
  data() {
    return {
      user: new User('', ''),
      confirmPassword: "",
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
        if (this.user.password === this.confirmPassword) {
          this.$store.dispatch('auth/register', this.user, this.confirmPassword).then(
          (response) => {
            this.message = "Succesfully registered!";
            console.log(response);
            // this.$router.push('/');
          },
          error => {
            this.message = error;
          });
        } else {
          this.message = "Passwords dont match";
        }
      }
    }
  }
};
</script>

<style>
</style>