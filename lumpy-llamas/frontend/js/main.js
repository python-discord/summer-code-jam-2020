/* eslint no-param-reassign: "off" */
import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import createPersistedState from 'vuex-persistedstate';
import Cookie from 'js-cookie';
import axios from 'axios';
import routes from './routes';
import KeyboardInput from './input.vue';
import KeyboardHandler from './keyboard-handler';
import InstructionsPanel from './instructions.vue';

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.xsrfCookieName = 'csrftoken';

Vue.use(Vuex);
Vue.use(VueRouter);
Vue.use(require('vue-moment'));

const router = new VueRouter({
  mode: 'history',
  routes,
});

const store = new Vuex.Store({
  plugins: [createPersistedState({
    storage: {
      getItem: (key) => Cookie.get(key),
      setItem: (key, value) => Cookie.set(key, value, { expires: 3, secure: true }),
      removeItem: (key) => Cookie.remove(key),
    },
  })],
  state: {
    userId: null,
    username: null,
    instructions: [],
  },
  mutations: {
    login(state, payload) {
      state.userId = payload.id;
      state.username = payload.username;
    },
    logout(state) {
      state.userId = null;
      state.username = null;
    },
    setInstructions(state, payload) {
      state.instructions = payload;
    },
    addInstructions(state, payload) {
      state.instructions.push(payload);
    },
  },
  getters: {
    isLoggedIn(state) {
      return Boolean(state.userId);
    },
  },
});

Vue.use(KeyboardHandler, { router, store });

new Vue({
  router,
  store,
  components: {
    'bbs-input': KeyboardInput,
    instructions: InstructionsPanel,
  },
  mounted() {
    if (!this.$store.getters.isLoggedIn && this.$route.name !== 'login_page') {
      this.$router.push({ name: 'login_page' });
    }
  },
  created() {
    this.$router.beforeEach((to, from, next) => {
      if (!this.$store.getters.isLoggedIn && to.name !== 'login_page') {
        next({ name: 'login_page' });
        return;
      }
      this.$cmd.reset();
      next();
    });
  },
}).$mount('#app');
