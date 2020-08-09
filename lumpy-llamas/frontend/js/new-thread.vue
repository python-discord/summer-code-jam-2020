<template>
<div v-if="ready">
  <fieldset>
    <legend>Post a new thread</legend>
    <div class="form-group">
      <label for="text">Title</label>
      <input v-model="title" id="text" name="itext" type="text" minlength="3" maxlength="120" :disabled="true">
    </div>
    <div class="form-group">
      <label for="itext">Message</label>
      <textarea v-model="message" id="taera" cols="30" rows="5" name="tarea" minlength="3" :disabled="true"></textarea>
    </div>
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

export default {
  data() {
    return {
      title: '',
      message: '',
      ready: true,
    };
  },
  mounted() {
    this.askForTitle();
  },
  methods: {
    askForTitle() {
      this.$cmd.input('Title: ').then((title) => {
        this.title = title;
        this.askForMessage();
      });
    },
    askForMessage() {
      this.$cmd.input('Body: ').then((body) => {
        this.message = body;
        this.newThread();
      });
    },
    newThread() {
      axios.post('/api/forum/post/thread', {
        title: this.title,
        message: this.message,
      }).then((res) => {
        this.$router.push(`/forum/${res.data.thread_id}/`);
      }).catch((err) => {
        alert(err.response.data.error);
        console.log(err); // eslint-disable-line no-console
      });
    },
  },
};
</script>
