<template>
  <div>
      <button type="button" class="news-button" v-on:click="setNew()">[1] New news</button>
      <button type="button" class="news-button" v-on:click="setBest()">[2] Best news</button>
      <div>
        <h2 v-text="currentTitle"></h2>
        <ul>
          <li v-for="item in myData" :key="item">
            <a :href="item.url" target="_blank">{{item.title}}</a>
          </li>
        </ul>
      </div>
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
  data() {
    return {
      myData: [],
      currentMode: 'new_news',
      currentTitle: 'New news:',
    };
  },
  beforeMount() {
    this.getData();
  },
  methods: {
    setNew() {
      this.currentMode = 'new_news';
      this.currentTitle = 'New news:';
      this.getData();
    },
    setBest() {
      this.currentMode = 'best_news';
      this.currentTitle = 'Best news:';
      this.getData();
    },
    getData() {
      axios.get(`/api/newsfeed/${this.currentMode}`).then((response) => {
        this.myData = response.data.news;
      });
    },
  },
};
</script>
