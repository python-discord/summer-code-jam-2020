<template>
<div v-if="ready">
  <fieldset>
    <legend>Post a new thread</legend>
        <div class="form-group">
          <label for="text">Title</label>
          <input v-model="title" id="text" name="itext" type="text" placeholder="Enter thread title" minlength="3" maxlength="120">
        </div>
        <div class="form-group">
          <label for="itext">Message</label>
          <textarea v-model="message" id="taera" cols="30" rows="5" name="tarea" placeholder="Enter thread title" minlength="3"></textarea>
        </div>
        <button v-on:click="newThread" class="btn btn-default">Make new thread</button>
  </fieldset>
</div>
</template>

<style>

p {
  margin-bottom: 2em;
}
</style>

<script>
import axios from 'axios';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


export default {
  data() {
    return {
      title: '',
      message: '',
      ready: true,
    };
  },

  methods: {
    newThread() {
      axios.post('/api/forum/post/thread', {
        title: this.title,
        message: this.message,
      }).then((res) => {
        console.log(res.data.thread_id);
        this.$router.push(`/forum/${res.data.thread_id}/`);
      }).catch((err) => {
        console.log(err); // eslint-disable-line no-console
      });
    },
  },
};
</script>