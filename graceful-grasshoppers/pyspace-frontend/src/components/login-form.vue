<template>
  <div>
    <b-form @submit.prevent="onSubmit">
      <b-form-group id="input-group-1" label="Username:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="user.username"
          type="text"
          required
          placeholder="Enter username"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="user.password"
          type="password"
          required
          placeholder="Enter password"
        ></b-form-input>
      </b-form-group>

      <div class="form-group">
        <button class="btn btn-primary btn-block">
          <span>Login</span>
        </button>
      </div>
      <div class="form-group">
        <div v-if="message" class="alert alert-danger" role="alert">{{message}}</div>
      </div>
    </b-form>
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