<template>
  <div v-if="ready">
    <h2>New news:</h2>
    <ul>
      <li v-for="item in mynew_news">
        <a :href="item.url" target="_blank">{{item.title}}</a>
      </li>
    </ul>
    <h2>Best news:</h2>
    <ul>
      <li v-for="item in mybest_news">
        <a :href="item.url" target="_blank">{{item.title}}</a>
      </li>
    </ul>
    # Links can be done like this
    # <router-link :to="{ name: 'some_page_name' }">Click Here</router-link>
  </div>
</template>

<style>
.some-heading {
  font-size: xx-large;
  color: pink;
}
</style>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      mynew_news: null,
      mybest_news: null,
      ready: false,
    };
  },
  beforeMount() {
    this.getData();
  },
  methods: {
    getData() {
      axios.get('/api/newsfeed/new_news').then((response) => {
        this.mynew_news = response.data.new_news;
        this.ready = true;
      });
      axios.get('/api/newsfeed/best_news').then((response) => {
        this.mybest_news = response.data.best_news;
        this.ready = true;
      });
    },
  }
}
</script>