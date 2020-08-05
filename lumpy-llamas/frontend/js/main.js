/* eslint no-param-reassign: "off" */
import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import routes from './routes';
import KeyboardInput from './input.vue';
import KeyboardHandler from './keyboard-handler';

Vue.use(Vuex);
Vue.use(VueRouter);

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
}).$mount('#app');
