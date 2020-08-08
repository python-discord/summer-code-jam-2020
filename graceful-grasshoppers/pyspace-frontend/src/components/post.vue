<template>
  <div>
    <h4>{{ post.title }}</h4>
    <p>{{ post.content }}</p>
  </div>
</template>

<script>
export default {
  props: ['post'],
};
</script>
<style>
</style>