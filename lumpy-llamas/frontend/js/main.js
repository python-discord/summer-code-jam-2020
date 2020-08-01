import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import routes from './routes';

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
});

new Vue({
  router,
  store,
}).$mount('#app');
