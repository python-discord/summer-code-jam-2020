import Home from './home-page.vue';
import ChatLobby from './chat-lobby.vue';
import ChatRoom from './chat-room.vue';
import Login from './login.vue';

const routes = [
  {
    path: '/home',
    alias: '/',
    name: 'home_page',
    component: Home,
  },
  {
    path: '/chat',
    name: 'chatlobby_page',
    component: ChatLobby,
  },
  {
    path: '/chat/room/:roomId',
    name: 'chatroom_page',
    component: ChatRoom,
  },
  {
    path: '/login',
    name: 'login_page',
    component: Login,
  },
];

export default routes;
