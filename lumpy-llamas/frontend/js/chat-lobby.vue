<template>
<div v-if="ready">
  <div class="home-grid">
    <h2> Chat Lobby</h2>
    <div class="chat-input">
        <input v-model="roomName" placeholder="Enter alphanumeric chat room name here">
        <button v-on:click="goToChatRoom">Enter Chatroom</button>
        <p>{{ message }}</p>
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
        message: null
    }
  },
  methods: { 
    goToChatRoom() {
        axios.post('/api/chat/checkname/', {'roomName': this.roomName}).then((response) => {
            if (response.data.valid) {
                this.message = null;
                window.location.pathname = '/chat/room/' + this.roomName + '/';
            }
            else {
                this.message = response.data.message
            }
        }, (error) => {
            console.log(error);
        })    
    }
  }
}
</script>
