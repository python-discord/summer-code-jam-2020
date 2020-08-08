import Home from './home-page.vue';
import Newsfeed from './news-feed.vue'
import Login from './login.vue';


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
  {
    path: '/login',
    name: 'login_page',
    component: Login,
  },

];

export default routes;
