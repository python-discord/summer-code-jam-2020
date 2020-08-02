<template>
  <div v-if="ready"> # this tells the page to not render until the page is ready
      # access objects directly with {{ myStuff.heading }} is the JS equivalent of {{ myStuff['heading'] }}

    <h2 class="some-heading">Hello and welcome to {{ myStuff.heading }}</h2>
    Here is how to do a list
    # if myStuff is a list, you can do a list rendering like so
    <ul>
      <li v-for="item in myStuff">
        My item name is: {{item}}
      </li>
    </ul>
    # Links can be done like this
    <router-link :to="{ name: 'some_page_name' }">Click Here</router-link>
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
  }
}
</script>