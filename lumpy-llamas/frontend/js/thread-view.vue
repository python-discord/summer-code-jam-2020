<template>
  <div v-if="ready">

    <h2 class="some-heading">Hello and welcome to Angry LLamas Forum</h2>

    <h2 class="some-heading">Messages</h2>
    <ul>
      <li v-for="item in myStuff">
        {{item}} --
        {{item.message}} test
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
      axios.get(`/api/forum/${this.$route.params.id}/`).then((response) => {
        this.myStuff = response.data;
        this.ready = true;
      });
    },

  },

}
</script>