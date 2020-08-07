<template>
  <div class="posts" style="margin: auto;">
    <PostList />
  </div>
</template>

<script>
// @ is an alias to /src
import PostList from '@/components/post-list';

export default {
  name: 'Posts',
  components: {
  	PostList,
  }
}
</script>
