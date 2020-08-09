<template>
<div v-if="ready">
  <div class="home-grid">
    <fieldset>
    <legend>Go chat with some random people!</legend>
        <div class="form-group">
          <label for="text">Chatroom Name</label>
          <input v-model="roomName" id="text" name="itext" type="text" 
            placeholder="(Alphanumeric and 1 and 20 characters long)" 
            minlength="1" maxlength="20">
        </div>
        <button v-on:click="goToChatRoom" class="btn btn-default">Enter Chatroom</button>
        <p>{{ message }}</p>
    </fieldset>
  </div>
</div>
</template>

<style>
::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: pink;
  opacity: 1; /* Firefox */
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
