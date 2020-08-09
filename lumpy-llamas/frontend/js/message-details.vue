<template>
  <div v-if="ready">
    <router-link :to="{ name: 'list-messages'}"><h2>Back to message list</h2></router-link>
    <h3 class="some-heading">{{myStuff[0].subject}} </h3>
    <div class="terminal-timeline">
    <div class="terminal-card" v-for="item in myStuff">
      <header id="card-header">{{item.from_user_id}} on {{item.created_date | moment("DD/MM/YY/HH:MM")}}</header>
      <div>
        {{item.message}}
      </div>
    </div>
    </div>
       <textarea v-model="message" id="taera" cols="30" rows="5" name="tarea" placeholder="Enter your message" minlength="3"></textarea>
        <button v-on:click="newMessage" class="btn btn-default">Reply</button>
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
      axios.get(`/api/mail/${this.$route.params.id}/`).then((response) => {
        this.myStuff = response.data;
        this.ready = true;
      });
    },
    newMessage() {
     console.log(this.selectedUserName)
     axios.post('/api/mail/post/message/', {
      to_user: this.myStuff[0].from_user_id,
      subject: this.myStuff[0].subject,
      message: this.message,
    }).then((res) => {
      console.log(res.data.message);
      this.$router.push('/messages/');
    }).catch((err) => {
      alert(err.response.data.error)
      console.log(err); // eslint-disable-line no-console
    });
  },
}
}
</script>