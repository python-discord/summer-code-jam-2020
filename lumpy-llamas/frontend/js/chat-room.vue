<template>
  <div>
    <div>
      <div v-for="message in messages">
        <span>{{ message }}</span>
      </div><br>
      <input id="chat-message-input" type="text" size="100"><br>
      <input id="chat-message-submit" type="button" value="Send">
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      socket: undefined,
      messages: [],
    }
  },
  beforeMount() {
    this.initSockets();
  },
  methods: {
    handleNewMessage(ev) {
      this.messages.push(ev.data);
    },
    sendMessage(msg) {
      this.socket.send(msg);
    },
    initSockets() {
      var socket_url =  'ws://' + window.location.host + '/ws' + window.location.pathname;
      this.socket = new WebSocket(socket_url);
      this.socket.onmessage = this.handleNewMessage;
    }
  }
}
</script>