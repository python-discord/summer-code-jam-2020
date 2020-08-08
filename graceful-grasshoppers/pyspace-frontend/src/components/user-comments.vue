<template>
	<div class="user-friends flex-col">
		<p class="alert-info font-weight-bold">Profile Comments</p>
		<div class="comment flex-row" v-for="comment in user.profile_comments" :key="comment.content">
			<div class="comment-user alert-info" style="width: 110px;">
				<a href="#">{{ comment.user }}</a>
				<img src="http://placehold.it/100x100">
			</div>
			<div class="comment-content alert-warning">
				<p>{{ comment.content }}</p>
			</div>
		</div>
		<div class="w-100">
			<form @submit.prevent="submitComment" class="flex-col">
				<textarea placeholder="Add a comment..."></textarea>
				<input type="submit" value="Comment">
			</form>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'UserComments',
		props: ['user'],
		methods: {
			submitComment() {
				console.log(this.user);
				console.log(this.content);
			}
		}
	};
</script>
