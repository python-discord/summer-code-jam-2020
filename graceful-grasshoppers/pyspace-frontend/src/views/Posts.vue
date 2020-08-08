<template>
  <div class="posts" style="margin: auto;">
    <PostList v-bind:posts="posts" />
  </div>
</template>

<script>
import PostList from '@/components/post-list';
import axios from '../http-common.js';
const authToken = JSON.parse(localStorage.getItem('user')).key;

export default {
	name: 'Posts',
	data: function() {
		return {
			posts: []
		}
	},
	components: {
		PostList,
	},
	methods: {
		init() {
			axios
			.get('/posts/')
			.then((response) => {
				this.posts = response.data.posts;
			})
		}
	},
	mounted() {
		this.init();
	},
}
</script>
