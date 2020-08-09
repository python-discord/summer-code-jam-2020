<template>
  <div v-if="ready">

    <router-link :to="{name: 'home_page'}"><h2 class="some-heading">Hello and welcome to Angry LLamas Forum</h2>
    </router-link>
    <div class="container">
      <h2 class="some-heading">Messages</h2>
      <button @click="$router.push('/messages/send/')" class="btn">New Message</button>
    </div>

    <ul>
      <li v-for="item in myStuff">
          <div v-if="item.from_user === ">Message from: {{ item.from_user }} on: {{ item.created_date | moment("DD.MM.YY, hh:mm") }}
          {{ item.created_by_id }}
          </div>
          <h2>Subject: {{item.subject}}</h2>
          <p>{{item.message}}</p>
      </li>
    </ul>
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