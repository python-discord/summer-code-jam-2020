<template>
	<div class="bordered w-75 mt-5" style="margin: auto;">
		<h4 class="font-weight-bold">Posts</h4>
		<div v-for="post in posts" class="bordered flex-row">
			<div class="flex-col" style="width: 110px;">
				<img src="http://placehold.it/100x100">
				<a v-bind:href="'/profile/'+post.author">{{ post.author }}</a>
			</div>
			<div>
				<p class="alert-warning p-1 font-weight-bold">{{ post.title }}</p>
				<p>{{ post.content }}</p>
				<img v-if="post.contains_image" class="w-100" v-bind:src="post.image_url">
				<div class="reactions flex-row">
					<button class="likes p-1 alert-success">{{ post.likes }} Positive Reactions</button>
					<button class="dislikes p-1 alert-danger">{{ post.dislikes }} Negative Reactions</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'UserAbout',
	props: ['posts'],
};
</script>
