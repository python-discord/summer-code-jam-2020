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
	name: 'Profile',
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
			.get(`/users/?username=${this.userId}`, { Authorization: "Token " + authToken })
			.then((response) => {
				console.log(response)
				console.log(this.userId)
				Object.assign(this.user, response.data[0]);
			})
		}
	},
	mounted() {
		this.init();
	},
}
</script>
