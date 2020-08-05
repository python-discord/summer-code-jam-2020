import Home from './home-page.vue';
import Forum from './thread-list.vue';
import Thread from './thread-view.vue';
import PostThread from './new-thread.vue';

const routes = [
  {
    path: '/home',
    alias: '/',
    name: 'home_page',
    component: Home,
  },
  {
    path: '/forum',
    alias: '/for',
    name: 'forum',
    component: Forum,
  },
  {
    path: '/forum/new',
    alias: '/new-thread',
    name: 'new-thread',
    component: PostThread,
  },
  {
    path: '/forum/:id',
    alias: '/thread-view',
    name: 'thread-view',
    component: Thread,
  },

];

export default routes;
