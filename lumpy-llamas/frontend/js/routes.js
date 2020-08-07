import Home from './home-page.vue';
import Login from './login.vue';

const routes = [
  {
    path: '/home',
    alias: '/',
    name: 'home_page',
    component: Home,
  },
  {
    path: '/login',
    name: 'login_page',
    component: Login,
  },
];

export default routes;
