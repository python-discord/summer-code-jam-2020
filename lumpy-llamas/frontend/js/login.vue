<template>
  <div>
    <h2>Login</h2>
    <div v-if="mode === null">
      <span class="login-message">
        Would you like to login or register?
        <ol class="home-menu-options">
          <li>Login</li>
          <li>Register</li>
        </ol>
      </span>
    </div>
    <div v-else-if="stage===1">
      Enter Username
    </div>
    <div v-else-if="stage===2">
      <span class="username">Username: {{username}}</span>
      Enter Password
    </div>
    <div v-else-if="stage===3">
      Please wait
    </div>
  </div>
</template>

<style>
</style>

<script>
import axios from 'axios';

const START_STAGE = 0;
const USERNAME_STATE = 1;
const PASSWORD_STAGE = 2;
const PROCESS_STAGE = 3;

export default {
  data() {
    return {
      username: '',
      password: '',
      mode: null,
      stage: START_STAGE,
    };
  },
  computed: {
    isLogin() {
      return this.$route.name === 'login_page';
    },
  },
  beforeMount() {
    this.addStartingKeybindings();
  },
  methods: {
    addStartingKeybindings() {
      this.$cmd.on('1', this.goToLogin);
      this.$cmd.on('2', this.goToRegister);
    },
    goToLogin() {
      this.stage = USERNAME_STATE;
      this.mode = 'login';
      this.$cmd.reset();
      this.inputUsername();
    },
    goToRegister() {
      this.stage = USERNAME_STATE;
      this.mode = 'register';
      this.$cmd.reset();
      this.inputUsername();
    },
    inputUsername() {
      this.$cmd.input('username: ').then((username) => {
        this.username = username;
        this.stage = PASSWORD_STAGE;
        this.$cmd.reset();
        this.inputPassword();
      });
    },
    inputPassword() {
      this.$cmd.input('password: ', true).then((password) => {
        this.password = password;
        this.stage = PROCESS_STAGE;
        this.$cmd.reset();
        this.loginOrRegister();
      });
    },
    loginOrRegister() {
      if (this.mode === 'register') {
        this.register();
      } else {
        this.login();
      }
    },
    login() {
      axios.post('/api/login', {
        username: this.username,
        password: this.password,
      }).then((res) => {
        this.$store.commit('login', res.data.id, res.data.username);
        this.$router.push('/');
      }).catch((err) => {
        this.stage = START_STAGE;
        console.log(err); // eslint-disable-line no-console
      });
    },
    register() {
      axios.post('/api/register', {
        username: this.username,
        password: this.password,
      }).then((res) => {
        this.$store.commit('login', res.data.id, res.data.username);
        this.$router.push('/');
      }).catch((err) => {
        this.stage = START_STAGE;
        console.log(err); // eslint-disable-line no-console
      });
    },
  },
};
</script>
