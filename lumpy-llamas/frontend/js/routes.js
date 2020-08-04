import Home from './home-page.vue';
import ChatLobby from './chat-lobby.vue';
import ChatRoom from './chat-room.vue'

const routes = [
  {
    path: '/home',
    alias: '/',
    name: 'home_page',
    component: Home,
  },
  {
    path: '/chat',
    alias: '/',
    name: 'chat_lobby',
    component: ChatLobby,
  },
  {
    path: '/chat',
    alias: '/room/', // Unsure how to do regex matching here for any room name
    name: 'chat_room',
    component: ChatRoom,
  },
];

export default routes;
