<template>
  <div v-if="ready">

    <router-link :to="{name: 'home_page'}"><h2 class="some-heading">Hello and welcome to Angry LLamas Forum</h2>
    </router-link>
    <div class="container">
      <h2 class="some-heading">Messages</h2>
      <button @click="$router.push('/messages/send/')" class="btn">New Message</button>
    </div>

    <ul>
      <li v-for="item in myStuff.query">
          <div class="from" v-if="item.from_user === myStuff.current_user">Message sent by you on: {{ item.created_date | moment("DD.MM.YY, hh:mm") }} to:
          {{ item.to_user }}

          <h2>Subject: {{item.subject}}</h2>
          <p>{{item.message}}</p>
          </div>

          <div v-else>
            Message sent by {{ item.from_user }} on: {{ item.created_date | moment("DD.MM.YY, HH:MM") }}

          <h2>Subject: {{item.subject}}</h2>
          <p>{{item.message}}</p>
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

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

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
  methods: {
    getData() {
      axios.get('/api/mail/').then((response) => {
        this.myStuff = response.data;
        this.ready = true;
      });
    },
  }
}
</script>