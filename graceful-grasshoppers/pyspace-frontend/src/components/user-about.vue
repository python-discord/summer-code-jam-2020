<template>
	<div>
		<div>
			<p class="alert-warning font-weight-bold">{{ user.username }}'s latest post :</p>
			<p class="font-weight-bold">{{ user.latest_post.title }}</p>
			<p>{{ user.latest_post.content }}</p>
			<a href="#">Read full post...</a>
			<a href="#">See all of {{ user.name }}'s posts</a>
		</div>
		<div>
			<p class="alert-warning font-weight-bold">About Me :</p>
			<p>{{ user.about }}</p>
		</div>
	</div>
</template>

<script>
export default {
	name: 'UserAbout',
	props: ['user'],
};
</script>
