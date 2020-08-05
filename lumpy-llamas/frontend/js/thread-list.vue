<template>
  <div v-if="ready">

    <h2 class="some-heading">Hello and welcome to Angry LLamas Forum</h2>
    <div class="container">
      <h2 class="some-heading">Threads</h2>
      <button class="btn">New thread</button>
    </div>

    <ul>
      <li v-for="item in myStuff">
        <router-link :to="{ name: 'thread-view', params: {id:item.id}}">{{ item.title }} - Posted:
          {{ item.created_date | moment("DD MM YY, hh:mm")  }} by {{item.created_by_id}}
        </router-link>
      </li>
    </ul>
    # Links can be done like this
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
      axios.get('/api/forum').then((response) => {
        this.myStuff = response.data;
        this.ready = true;
      });
    },
  }
}
</script>