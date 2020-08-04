<template>
<div v-if="ready">
  <div class="home-grid">
    <h2> Chat Lobby</h2>
    <div class="chat-input">
        <input v-model="roomName" placeholder="Enter alphanumeric chat room name here">
        <button v-on:click="goToChatRoom">Enter Chatroom</button>
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
        ready: true
    }
  },
  methods: { 
    goToChatRoom() {
        if (this.roomName) {
            window.location.pathname = '/chat/' + this.roomName + '/';
        }
    }
  }
}
</script>
