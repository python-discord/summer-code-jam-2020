<template>
<div v-if="ready">
  <fieldset>
    <legend>Post a new thread</legend>
        <div class="form-group">
          <label for="text">Title</label>
          <input v-model="title" id="text" name="itext" type="text" placeholder="Enter thread title" minlength="3" maxlength="120">
        </div>
      <div class="form-group">
        <label for="select">To user:</label>
        <select v-model="selectedUserName" id="select"  name="select">
          <option v-for="user in usernames" v-bind:value="user.username"> {{user.username}} </option>
        </select>
      </div>
      <div class="form-group">
          <label for="itext">Message</label>
          <textarea v-model="message" id="taera" cols="30" rows="5" name="tarea" placeholder="Enter thread title" minlength="3"></textarea>
        </div>
        <button v-on:click="newMessage" class="btn btn-default">Make new thread</button>
  </fieldset>
</div>
</template>

<style>

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
      usernames: null,
      subject: '',
      message: '',
      ready: true,
      selectedUserName: null
    };
  },
 beforeMount() {
    this.getUsers();
  },
  methods: {
     getUsers() {
      axios.get('/api/mail/usernames/').then((response) => {
        this.usernames = response.data;
        this.ready = true;
      });
    },
    newMessage() {
       console.log(this.selectedUserName)
       axios.post('/api/mail/post/message/', {
        to_user: this.selectedUserName,
        subject: this.title,
        message: this.message,
      }).then((res) => {
        console.log(res.data.message);
        this.$router.push('/messages/');
      }).catch((err) => {
        alert(err.response.data.error)
        console.log(err); // eslint-disable-line no-console
      });
    },
  },
};
</script>