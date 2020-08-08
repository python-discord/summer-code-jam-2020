import Home from './home-page.vue';
import Newsfeed from './news-feed.vue'
import Login from './login.vue';
import TicTacToe from './tic-tac-toe.vue';


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

  {
    path: '/games/tictactoe',
    name: 'tictactoe_page',
    component: TicTacToe,
  },

];

export default routes;
