<template>
  <div class="posts" style="margin: auto;">
    <PostList v-bind:posts="posts" />
  </div>
</template>

<script>
import PostList from '@/components/post-list';
import axios from '../http-common.js';
// const authToken = JSON.parse(localStorage.getItem('user')).key;

export default {
	name: 'Posts',
	data: function() {
		return {
			userId: this.$route.params.userId,
			posts: [],
		}
	},
	components: {
		PostList,
	},
	methods: {
		init() {
			const query_url = this.userId == null ? '/posts/' : '/posts/?username='+this.userId;
			axios
			.get(query_url)
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
