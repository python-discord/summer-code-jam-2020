<template>
  <div>
    <div>
      <div v-for="message in messages">
        <span>{{ message }}</span>
      </div><br>
      <input id="chat-message-input" v-model="msg" type="text" size="100"><br>
      <button id="chat-message-submit" @click="sendMessage">Send message</button> 
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      socket: undefined,
      messages: [],
      msg: ''
    }
  },
  beforeMount() {
    this.initSockets();
  },
  methods: {
    handleNewMessage(ev) {
      var new_msg = JSON.parse(ev.data);
      this.messages.push(new_msg.message);
    },
    sendMessage(msg) {
      if (msg) {
        this.socket.send(JSON.stringify({
          message: this.msg,
        }));
        this.msg = '';
      };  
    },
    initSockets() {
      const socketUrl = `ws://${window.location.host}/ws/chat/room/${this.$route.params.roomId}/`
      this.socket = new WebSocket(socketUrl);
      this.socket.onmessage = this.handleNewMessage;
    }
  }
}
</script>