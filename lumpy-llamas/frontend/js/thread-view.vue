<template>
  <div v-if="ready">

    <h2 class="some-heading">Thread Title</h2>

    <h2 class="some-heading">Messages</h2>
    <div v-for="item in myStuff">
        <h3 class="message-heading">Message by {{item.user_id}} on {{item.date | moment("DD/MM/YY/hh:mm")}}</h3>
        <p>{{item.message}}</p>
    </div>
  </div>
</template>

<style>
.some-heading {
  font-size: xx-large;
  color: pink;
}

.message-heading {
  color: aquamarine;
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
  methods: {
    getData() {
      axios.get(`/api/forum/${this.$route.params.id}/`).then((response) => {
        this.myStuff = response.data;
        this.ready = true;
      });
    },

  },

}
</script>