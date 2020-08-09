<template>
	<div class="bordered w-75 m-5 p-4" style="margin: auto;">
		<Post class="mt-5 bordered" v-bind:post="post" />
		<UserProfile class="alert-warning" v-bind:logged_in="loggedIn" v-bind:user="author" />
	</div>
</template>

<script>
import PostModel from '@/models/post';
import User from '@/models/user';
import Post from '@/components/post';
import UserProfile from '@/components/user-profile'
import axios from "../http-common.js";

export default {
	data: function() {
		return {
			postId: this.$route.params.postId,
			post: new PostModel({}),
			author: new User({}),
			loggedIn: (localStorage.getItem('user') != null),
		}
	},
	methods: {
		init() {
			axios
			.get(`/posts/?post=${this.postId}`)
			.then((response) => {
				Object.assign(this.post, response.data.posts[0]);
				console.log(this.post)
			})
			.then(() => {
				axios
				.get(`/users/?username=${this.post.author}`)
				.then((response) => {
					Object.assign(this.author, response.data[0]);
				})
			})
		},
	},
	components: {
		Post,
		UserProfile,
	},
	mounted: function() {
		this.init();
	}
}
</script>