<template>
  <div class="home-container">
    <h4 class="home-heading">COTLaQ BBS</h4>
    <span class="subtitle">Cofessions Of a Teenage Llama Queen</span>
    <div class="home-grid">
    <div class="home-newsfeed item">
      <newsfeed :current-mode="newsMode"></newsfeed>
    </div>
    <div class="home-menu item">
      <h2>Menu</h2>
      <ol class="home-menu-options">
        <li v-for="page in pages">
          <router-link :to="{ name: page.page }">{{page.title}}</router-link>
        </li>
      </ol>
    </div>
    </div>
  </div>
</template>

<style>
.home-heading {
  margin-bottom: 0;
}
.subtitle {
  font-style: italic;
  font-weight: lighter;
}
.home-grid .item {
  border-style: solid;
  border-width: 1px;
  padding: 0.5em;
}

.home-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.home-menu {
  /* grid-column: span 2; */
}

.home-menu-options li:before {
  content: "[" counters(item, ".") "] ";
  counter-increment: item;
}

</style>

<script>
import NewsFeed from './news-feed.vue';

const MENU_PAGES = [
  { title: 'Forum/Thread-list', page: 'forum' },
  { title: 'Chat Lobby', page: 'chatlobby_page' },
  { title: 'Play Tic Tac Toe', page: 'tictactoe_page' },
  { title: 'Electronic Mail', page: 'list-messages' },
];

export default {
  components: {
    newsfeed: NewsFeed,
  },
  data() {
    return {
      pages: MENU_PAGES,
      newsMode: 'new_news',
    };
  },
  beforeMount() {
    this.$cmd.on('1', this.goToForum);
    this.$cmd.on('2', this.goToChatLobby);
    this.$cmd.on('3', this.goToGame);
    this.$cmd.on('4', this.goToMessages);
    this.$cmd.on('/news new', this.setNewNews, 'Get newest articles');
    this.$cmd.on('/news top', this.setTopNews, 'Get top articles');
  },
  methods: {
    setNewNews() {
      this.newsMode = 'new_news';
    },
    setTopNews() {
      this.newsMode = 'best_news';
    },
    goToChatLobby() {
      this.$router.push({ name: 'chatlobby_page' });
    },
    goToForum() {
      this.$router.push({ name: 'forum' });
    },
    goToGame() {
      this.$router.push({ name: 'tictactoe_page' });
    },
    goToMessages() {
      this.$router.push({ name: 'list-messages' });
    },
  },
};
</script>
