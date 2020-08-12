import Home from './home-page.vue';
import ChatLobby from './chat-lobby.vue';
import ChatRoom from './chat-room.vue';
import Login from './login.vue';
import TicTacToe from './tic-tac-toe.vue';
import Forum from './thread-list.vue';
import Thread from './thread-view.vue';
import PostThread from './new-thread.vue';
import ListMessages from './list-messages.vue';

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
  {
    path: '/logout',
    name: 'logout_page',
    component: Login,
  },
  {
    path: '/games/tictactoe',
    name: 'tictactoe_page',
    component: TicTacToe,
  },
  {
    path: '/forum',
    name: 'forum',
    component: Forum,
  },
  {
    path: '/forum/new',
    name: 'new-thread',
    component: PostThread,
  },
  {
    path: '/forum/:id',
    name: 'thread-view',
    component: Thread,
  },
  {
    path: '/messages/',
    name: 'list-messages',
    component: ListMessages,
  },


];

export default routes;
