<template>
  <div>
    <div class="chat-log">
      <div v-for="message in messages">
        <span>{{ message }}</span>
      </div>
    </div>
  </div>
</template>

<style>
.chat-log {
  /* height: 80vh; */
  overflow-y: auto;
}
.instructions {
  bottom: 0;
  display: grid;
  width: 100%;
  text-align: center;
  color: deeppink;
}
</style>

<script>
export default {
  data() {
    return {
      socket: undefined,
      messages: [],
    };
  },
  beforeMount() {
    this.initSockets();
  },
  mounted() {
    this.inputMessage();
    this.$cmd.on('/exit', () => this.$router.push('/chat'), 'Exit the chat');
  },
  methods: {
    handleNewMessage(ev) {
      const data = JSON.parse(ev.data);
      const messageToDisplay = `[${data.message.datetime}] ${data.message.user}: ${data.message.message}`;
      this.messages.push(messageToDisplay);
    },
    sendMessage(msg) {
      if (msg) {
        const now = new Date();

        this.socket.send(JSON.stringify({
          message: msg,
          datetime: now.toISOString(),
        }));
      }
    },
    initSockets() {
      const socketUrl = `ws://${window.location.host}/ws/chat/room/${this.$route.params.roomId}/`;
      this.socket = new WebSocket(socketUrl);
      this.socket.onmessage = this.handleNewMessage;
    },
    inputMessage() {
      this.$cmd.input('>>> ').then((msg) => { // ask for input
        if (msg === '/exit') {
          return;
        }
        this.sendMessage(msg); // send the message to django
        this.inputMessage(); // repeat listening
      });
    },
  },
};
</script>
