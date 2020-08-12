<template>
	<div>
		<div>
			<p class="alert-warning font-weight-bold">About Me :</p>
			<p>{{ user.about }}</p>
		</div>
		<div>
			<p class="alert-warning font-weight-bold">{{ user.username }}'s latest post :</p>
			<p class="font-weight-bold">{{ user.latest_post.title }}</p>
			<p>{{ user.latest_post.content }}</p>
			<a v-if="user.latest_post.date_posted" v-bind:href="'/post/' + user.latest_post.id">Read full post...</a>
			<p v-else>{{ user.username }} has no posts</p>
			<a v-if="user.latest_post.date_posted" v-bind:href="'/posts/' + user.username">See all of {{ user.username }}'s posts</a>
		</div>
	</div>
</template>

<script>
export default {
	name: 'UserAbout',
	props: ['user'],
};
</script>
