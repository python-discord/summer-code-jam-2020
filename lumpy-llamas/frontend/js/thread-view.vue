<template>
  <div v-if="ready" class="forum-thread">
    <router-link :to="{ name: 'forum'}"><h2>Back to forum list</h2></router-link>
    <h3 class="some-heading">{{myStuff[0].title}} </h3>
    <div class="terminal-timeline">
      <div class="terminal-card" v-for="item in myStuff">
        <header id="card-header">{{item.user}} on {{item.date | moment("DD/MM/YY/HH:MM")}}</header>
        <div>
          {{item.message}}
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.forum-thread {
  overflow-y: auto;
}
.some-heading {
  font-size: xx-large;
  color: pink;
}

#card-header {
  color: whitesmoke;
}

p {
  margin-bottom: 2em;
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      myStuff: null,
      ready: false,
    };
  },
  beforeMount() {
    this.getData();
  },
  mounted() {
    this.errorCallback = this.$cmd.onUnknown(this.replyThread);
    this.$cmd.on('/reply <message>', () => undefined, 'Reply to thread with <message>');
    this.$cmd.on('/exit', () => this.$router.push('/forum'), 'Return to thread list');
  },
  methods: {
    replyThread(command) {
      console.log(command);
      if (command.startsWith('/reply ')) {
        const cmd = command.split(' ');
        cmd.shift();
        this.newMessage(cmd.join(' '));
      } else if (command !== '/exit') {
        this.errorCallback(command);
      }
    },
    getData() {
      axios.get(`/api/forum/${this.$route.params.id}`).then((response) => {
        this.myStuff = response.data;
        this.ready = true;
      });
    },
    newMessage(message) {
      console.log('replying', message);
      axios.post('/api/forum/post/message', {
        message,
        thread_id: this.$route.params.id,
      }).then((res) => {
        this.getData();
        console.log(res.data.thread_id); // eslint-disable-line no-console
      }).catch((err) => {
        console.log(err); // eslint-disable-line no-console
      });
    },
  },
};
</script>
