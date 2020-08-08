<template>
  <div>
    <div>
      <div>
        <div class="chat-log">
          <div v-for="message in messages">
            <span>{{ message }}</span>
          </div>
        </div>
        <div class="instructions">
          <p>To send a message, type it out and hit "Enter"</p><br>
          <p>To exit a chat, send "/exit"</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.chat-log {
  height: 80vh;
  overflow-y: scroll;
}
.instructions {
  bottom: 0;
  display: grid; 
  width: 100%; 
  text-align: center;
  color:deeppink;
}
</style>

<script>
export default {
  data() {
    return {
      socket: undefined,
      messages: []
    }
  },
  beforeMount() {
    this.initSockets();
  },
  mounted () {
    this.inputMessage()
  },
  methods: {
    handleNewMessage(ev) {
      var data = JSON.parse(ev.data);
      var message_to_display = `[${data.message.datetime}] ${data.message.user}: ${data.message.message}`
      this.messages.push(message_to_display);
    },
    sendMessage(msg) {
      if (msg) {
        var now = new Date()

        this.socket.send(JSON.stringify({
          message: msg,
          datetime: now.toISOString()
        }));
      };  
    },
    initSockets() {
      const socketUrl = `ws://${window.location.host}/ws/chat/room/${this.$route.params.roomId}/`
      this.socket = new WebSocket(socketUrl);
      this.socket.onmessage = this.handleNewMessage;
    },
    inputMessage() {
      this.$cmd.input('>>> ').then((msg) => { // ask for input
        this.$cmd.reset(); // clear message box
        if (msg === '/exit') {
            this.$router.push('/chat') // check if command is exit, if so, leave
        } else {
            this.sendMessage(msg); // send the message to django
            this.inputMessage(); // repeat listening
        }
      });
    }
  }
}
</script>