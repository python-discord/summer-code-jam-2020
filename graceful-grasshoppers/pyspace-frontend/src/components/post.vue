<template>
  <div>
    <h4>{{ post.title }}</h4>
    <p>{{ post.content }}</p>
  </div>
</template>

<script>
import Post from '../models/post';
export default {
  name: 'Login',
  data() {
    return {
      post: new Post(),
      message: '',
    };
  },
  computed: {
  },
  created() {
  },
  methods: {
  }
};
</script>

<style>
</style>