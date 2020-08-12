<template>
	<div class="user-friends flex-col">
		<p class="alert-info font-weight-bold">Profile Comments</p>
		<div class="comment flex-row" v-for="comment in user.profile_comments" :key="comment.content">
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
</template>

<script>
	import axios from "../http-common.js";
	import authHeader from "@/services/auth-header";
	export default {
		name: 'UserComments',
		props: ['user'],
		data: function() {
			return {
				content: "",
			}
		},
		methods: {
			submitComment() {
				console.log(authHeader())
				axios
				.post("/users/comment/", 
				{
					user_commented_on: this.user.username,
					content: this.content,
				},
				{
					headers: authHeader()
				})
				.then((response) => {
					console.log(response);
				})
			}
		}
	};
</script>