<template>
<div v-if="ready">
    <h2>Post a new thread</h2>
        <input v-model="title" placeholder="Enter thread title">
        <input v-model="message" placeholder="Enter your message">
        <button v-on:click="newThread">Make new thread</button>
        <p>{{ title }}</p>
        <p>{{message}}</p>
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
      message: '',
      ready: true,
    };
  },

  methods: {
    newThread() {
      axios.post('/api/forum/post/thread', {
        title: this.title,
        message: this.message,
      }).then(() => {
        console.log(response);
      }).catch((err) => {
        console.log(err); // eslint-disable-line no-console
      });
    },
  },
};
</script>