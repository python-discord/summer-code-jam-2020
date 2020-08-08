/* eslint no-param-reassign: "off" */
import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
// import Cookie from 'js-cookie';
import axios from 'axios';
import routes from './routes';
import KeyboardInput from './input.vue';
import KeyboardHandler from './keyboard-handler';

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.xsrfCookieName = 'csrftoken';
// const csrftoken = Cookie.get('csrftoken');

Vue.use(Vuex);
Vue.use(VueRouter);
Vue.use(require('vue-moment'));

const router = new VueRouter({
  mode: 'history',
  routes,
});

const store = new Vuex.Store({
  state: {
    userId: null,
    username: null,
  },
  mutations: {
    login(state, userId, username) {
      state.userId = userId;
      state.username = username;
    },
  },
});

Vue.use(KeyboardHandler, { router });

new Vue({
  router,
  store,
  components: {
    'bbs-input': KeyboardInput,
  },
  created() {
    this.$router.beforeEach((to, from, next) => {
      this.$cmd.reset();
      next();
    });
  },
}).$mount('#app');
