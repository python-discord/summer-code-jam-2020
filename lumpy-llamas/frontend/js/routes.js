import Home from './home-page.vue';
import Forum from './thread-list.vue';
import Thread from './thread-view.vue';

const routes = [
  {
    path: '/home',
    alias: '/',
    name: 'home_page',
    component: Home,
  },
  {
    path: '/forum',
    alias: '/forum',
    name: 'forum',
    component: Forum,
  },
  {
    path: '/forum/view:id',
    alias: '/thread-view',
    name: 'thread-view',
    component: Thread,
  },
];

export default routes;
