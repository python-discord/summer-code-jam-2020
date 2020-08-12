<template>
  <div v-if="ready">
    <h2 class="some-heading">Electronic Mail</h2>
    <div class="container">
      <h2 class="some-heading">Messages</h2>

    </div>

    <ul>
      <li v-for="item in myStuff.query">
        <div class="from" v-if="item.from_user === myStuff.current_user">Message sent by you on:
          {{ item.created_date | moment("DD.MM.YY, hh:mm") }} to:
          {{ item.to_user }}

          <h2>Subject: {{ item.subject }}</h2>
          <p>{{ item.message }}</p>
        </div>

        <div v-else>
          Message sent by {{ item.from_user }} on: {{ item.created_date | moment("DD.MM.YY, HH:MM") }}

          <h2>Subject: {{ item.subject }}</h2>
          <p>{{ item.message }}</p>
        </div>

      </li>
    </ul>
  </div>
</template>

<style>
.some-heading {
  font-size: xx-large;
  color: pink;
}

.from {
  color: cadetblue;
}
</style>

<script>
import axios from 'axios';

const START_STAGE = 0;
const USER_STAGE = 1;


export default {
  data() {
    return {
      myStuff: null,
      ready: false,
      subject: '',
      message: '',
      recipient: '',
    };
  },
  beforeMount() {
    this.getData();
    this.addStartingKeybindings();
  },
  methods: {
    addStartingKeybindings() {
      this.$cmd.on('/message', this.inputSubject, 'Send a message')
    },
    inputSubject() {
      this.$cmd.input('subject: ').then((subject) => {
        this.subject = subject;
        this.inputMessage();
      });
    },
    inputMessage() {
      this.$cmd.input('message: ').then((message) => {
        this.message = message;
        this.inputRecipient();
      });
    },
    inputRecipient() {
      this.$cmd.input('username').then((recipient) => {
        this.recipient = recipient;
        this.stage = USER_STAGE;
        this.newMessage();
      });
    },
    getData() {
      axios.get('/api/mail/').then((response) => {
        this.myStuff = response.data;
        this.ready = true;
      });
    },
    newMessage() {
      //console.log(this.selectedUserName)
      axios.post('/api/mail/post/message/', {
        to_user: this.recipient,
        subject: this.subject,
        message: this.message,
      }).then((res) => {
        this.getData();
        this.cmd.reset();
      }).catch((err) => {
        this.stage = START_STAGE;
        console.log(err); // eslint-disable-line no-console
      });
    },
  },
}

</script>
