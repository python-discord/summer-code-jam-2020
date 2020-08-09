<template>
	<div class="bordered w-75 m-5 p-4" style="margin: auto;">
		<Post class="mt-5 bordered" v-bind:post="post" />
		<div class="user-friends flex-col">
			<p class="alert-info font-weight-bold">Post Comments</p>
			<div class="comment flex-row" v-for="comment in post.comments" :key="comment.content">
				<div class="comment-user alert-info" style="width: 110px;">
					<a v-bind:href="'/profile/'+comment.user">{{ comment.user }}</a>
					<img src="http://placehold.it/100x100">
				</div>
				<div class="w-100 comment-content alert-warning">
					<p>{{ comment.content }}</p>
				</div>
			</div>
			<div class="w-100">
				<form @submit.prevent="submitComment" class="flex-col">
					<textarea v-model="content" placeholder="Add a comment..."></textarea>
					<input type="submit" value="Comment">
				</form>
			</div>
		</div>
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
				content: "",
			}
		},
		methods: {
			init() {
				axios
				.get(`/posts/?post=${this.postId}`)
				.then((response) => {
					Object.assign(this.post, response.data.posts[0]);
					console.log(this.post.comments)
				})
				.then(() => {
					axios
					.get(`/users/?username=${this.post.author}`)
					.then((response) => {
						Object.assign(this.author, response.data[0]);
					})
				})
			},
			submitComment() {
				console.log(authHeader())
				axios
				.post("/posts/comment/"+this.post.id+"/", 
				{
					content: this.content,
				},
				{
					headers: authHeader()
				})
				.then((response) => {
					console.log(response);
				})
			}
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