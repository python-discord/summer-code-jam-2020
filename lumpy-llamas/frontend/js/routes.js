import Home from './home-page.vue';
import Newsfeed from './news-feed.vue'

const routes = [
  {
    path: '/home',
    alias: '/',
    name: 'home_page',
    component: Home,
  },
  {
    path: '/newsfeed',
    alias: '/',
    name: 'news_feed',
    component: Newsfeed,
  },
];

export default routes;
