<template>
  <div v-if="ready">
    <h2 class="some-heading">{{myStuff[0].title}} </h2>
    <div class="terminal-timeline">
    <div class="terminal-card" v-for="item in myStuff">
      <header>{{item.user}} on {{item.date | moment("DD/MM/YY/HH:MM")}}</header>
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

.message-heading {
  color: aquamarine;
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
        console.log(res.data.thread_id);
      }).catch((err) => {
        console.log(err); // eslint-disable-line no-console
      });
  },
  }}
</script>