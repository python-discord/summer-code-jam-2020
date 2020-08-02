import Home from './home-page.vue';
import Forum from './thread-list.vue';

const routes = [
  {
    path: '/home',
    alias: '/',
    name: 'home_page',
    component: Home,
  },
  {
    path: '/forum',
    alias: '/f',
    name: 'forum',
    component: Forum,
  },
];

export default routes;
