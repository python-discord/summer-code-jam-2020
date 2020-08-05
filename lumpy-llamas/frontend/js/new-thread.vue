<template>
<div v-if="ready">
  <div class="home-grid">
    <h2>Post a new thread</h2>
        <input v-model="title" placeholder="Enter thread title">
        <button v-on:click="newThread">Make new thread</button>
        <p>{{ title }}</p>
  </div>
</div>
</template>

<style>

p {
  margin-bottom: 2em;
}
</style>

<script>
import axios from 'axios';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

export default {
  data() {
    return {
      title: '',
      user: '',
      ready: true,
    };
  },

  methods: {
    newThread() {
      axios.post('/api/forum/post/thread', {
        title: this.title,
        user: this.user,
      }).then(() => {
        console.log(response);
      }).catch((err) => {
        console.log(err); // eslint-disable-line no-console
      });
    },
  },
};
</script>