<template>
  <div>
    <h2 v-text="currentTitle"></h2>
    <ul>
      <li v-for="item in myData" :key="item.url">
        <a :href="item.url" target="_blank">{{item.title}}</a>
      </li>
    </ul>
  </div>
</template>

<style>
.news-button {
  background-color:  #262626;
  border: none;
  padding: 10px 24px;
  color: white;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 22px;
  transition-duration: 0.4s;
}

.news-button:hover {
  background-color: orange; /* Green */
  color: white;
}

</style>

<script>
import axios from 'axios';

export default {
  props: {
    currentMode: {
      type: String,
      default: 'new_news',
    },
  },
  data() {
    return {
      myData: [],
    };
  },
  beforeMount() {
    this.getData();
  },
  watch: {
    currentMode() {
      this.myData = [];
      this.getData();
    },
  },
  computed: {
    currentTitle() {
      return this.currentMode === 'new_news' ? 'News (New)' : 'News (Top)';
    },
  },
  methods: {
    getData() {
      axios.get(`/api/newsfeed/${this.currentMode}`).then((response) => {
        this.myData = response.data.news;
      });
    },
  },
};
</script>
