<template>
	<div class="bordered w-75 mt-5" style="margin: auto;">
		<h4 class="font-weight-bold">Posts</h4>
		<div v-bind:key="post.id" v-for="post in posts" class="bordered flex-row w-100">
			<div class="flex-col" style="width: 110px;">
				<img src="http://placehold.it/100x100">
				<a v-bind:href="'/profile/'+post.author">{{ post.author }}</a>
			</div>
			<div class="w-100">
				<a v-bind:href="'/post/'+post.id" class="alert-warning p-1 font-weight-bold w-100">{{ post.title }}</a>
				<p>{{ post.content }}</p>
				<img v-if="post.contains_image" class="w-100" v-bind:src="post.image_url">
				<div class="reactions flex-row w-100">
					<button v-on:click="like_post(post.id)" class="likes p-1 alert-success">{{ post.likes }} Positive Reactions</button>
					<button v-on:click="dislike_post(post.id)" class="dislikes p-1 alert-danger">{{ post.dislikes }} Negative Reactions</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'UserAbout',
	props: ['posts'],
	data: function() {
		return {
			liked: false,
			disliked: false,
		}
	},
	methods: {
		like_post(post_id) {
			alert(post_id);
		},
		dislike_post(post_id) {
			alert(post_id);
		}
	}
};
</script>
