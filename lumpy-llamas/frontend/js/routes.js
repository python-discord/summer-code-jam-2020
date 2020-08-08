import Home from './home-page.vue';
import Newsfeed from './news-feed.vue'

const routes = [
  {
    path: '/home',
    alias: '/',
    name: 'home_page',
    component: Home,
  },
];

export default routes;
