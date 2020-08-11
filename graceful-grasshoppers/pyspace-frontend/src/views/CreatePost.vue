<template>
  <div class="container mt-5">
    <h3 style="text-align: center;">Create a new post!</h3>
    <CreatePostForm />
  </div>
</template>

<script>
import CreatePostForm from '@/components/create-post-form';
export default {
    name: 'CreatePost',
    components: {
        CreatePostForm
    }
}
</script>
