<template>
<div v-if="ready">
  <div class="home-grid">
    <h2> Chat Lobby</h2>
    <div class="chat-input">
        <input v-model="roomName" placeholder="Enter alphanumeric chat room name here">
        <button v-on:click="goToChatRoom">Enter Chatroom</button>
        <p>{{ error }}</p>
    </div>
  </div>
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
        roomName: '',
        ready: true,
        checkName: {},
        error: null
    }
  },
  methods: { 
    goToChatRoom() {
        axios.post('/api/chat/checkname/', {roomName: this.roomName}).then((response) => {
            this.checkName = response.data;
        })

        if (this.checkName.valid) {
            window.location.pathname = '/chat/' + this.roomName + '/';
        }
        else {
            this.error = this.checkName.message
        }
    
    }
  }
}
</script>
