<template>
<div v-if="ready">
  <div class="home-grid">
    <legend>Go chat with some random people!</legend>
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
      message: null,
      errorCallback: undefined,
    };
  },
  mounted() {
    this.errorCallback = this.$cmd.onUnknown(this.enterChatroomName);
    this.$cmd.on('/join <name>', () => undefined, 'Enter chatroom <name>');
  },
  methods: {
    enterChatroomName(command) {
      if (command.startsWith('/join ')) {
        this.goToChatRoom(command.split(' ')[1]);
      } else {
        this.errorCallback(command);
      }
    },
    goToChatRoom(roomName) {
      axios.post('/api/chat/checkname/', { roomName }).then((response) => {
        if (response.data.valid) {
          this.message = null;
          this.$router.push({ name: 'chatroom_page', params: { roomId: roomName } });
        } else {
          this.message = response.data.message;
        }
      }, (error) => {
        console.log(error);
      });
    },
  },
};
</script>
