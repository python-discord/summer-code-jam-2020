<template>
  <div>
    <form class="flex-col" @submit.prevent="onSubmit">
      <label for="input-1">Username</label>
      <input
        id="input-1"
        v-model="user.username"
        type="text"
        required
        placeholder="Enter username"
      >

      <label for="input-2">Email</label>
      <input
        id="input-2"
        v-model="user.email"
        type="email"
        required
        placeholder="Enter email"
      >

      <label for="input-3">Password</label>
      <input
        id="input-3"
        v-model="user.password"
        type="password"
        required
        placeholder="Enter password"
      >

      <label for="input-4">Confirm Password</label>
      <input
        id="input-4"
        v-model="user.confirm_password"
        type="password"
        required
        placeholder="Confirm password"
      >

      <input type="submit" value="Register" name="">
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
          if (this.user.password === this.user.confirm_password) {
            this.$store.dispatch('auth/register', this.user).then(
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