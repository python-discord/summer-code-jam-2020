<template>
  <div v-if="ready">
    <router-link :to="{name: 'home_page'}"><h2 class="some-heading">Hello and welcome to Angry LLamas Forum</h2></router-link>
    <div class="container">
      <h2 class="some-heading">Threads</h2><button class="btn" @click="$router.push('/forum/new')">New thread</button>
    </div>

    <ul>
      <li v-for="item in myStuff">
        <router-link :to="{ name: 'thread-view', params: {id:item.id}}">{{ item.title }} - Posted:
          {{ item.created_date | moment("DD.MM.YY, hh:mm")  }} by {{item.created_by_id}}
        </router-link>
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
      axios.get('/api/forum/').then((response) => {
        this.myStuff = response.data;
        this.ready = true;
      });
    },
  },
};
</script>
