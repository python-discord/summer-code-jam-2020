<template>
  <div v-if="ready">
    <router-link :to="{ name: 'forum'}"><h2>Back to forum list</h2></router-link>
    <h3 class="some-heading">{{myStuff[0].title}} </h3>
    <div class="terminal-timeline">
    <div class="terminal-card" v-for="item in myStuff">
      <header id="card-header">{{item.user}} on {{item.date | moment("DD/MM/YY/HH:MM")}}</header>
      <div>
        {{item.message}}
      </div>
    </div>
    </div>
       <textarea v-model="message" id="taera" cols="30" rows="5" name="tarea" placeholder="Enter your message" minlength="3"></textarea>
        <button v-on:click="newMessage" class="btn btn-default">Post a new message</button>
    </div>




</template>

<style>
.some-heading {
  font-size: xx-large;
  color: pink;
}

#card-header {
  color: whitesmoke;
}

p {
  margin-bottom: 2em;
}
</style>

<script>
import axios from 'axios';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export default {
  data() {
    return {
      myStuff: null,
      ready: false,
    };
  },
  beforeMount() {
    this.getData();
  },
  methods: {
    getData() {
      axios.get(`/api/forum/${this.$route.params.id}/`).then((response) => {
        this.myStuff = response.data;
        this.ready = true;
      });
    },
    newMessage() {
      axios.post('/api/forum/post/message', {
        message: this.message,
        thread_id: this.$route.params.id
      }).then((res) => {
        this.getData();
        this.textarea = "";
        console.log(res.data.thread_id);
      }).catch((err) => {
        alert(err.response.data.message)
        console.log(err) // eslint-disable-line no-console
      });
  },
  }}
</script>