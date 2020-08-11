<template>
	<div class="user-friends flex-col">
		<p class="alert-info font-weight-bold">Profile Comments</p>
		<div class="friend flex-row" v-for="comment in post.comments" :key="comment.content">
				<div class="comment-user alert-info" style="width: 110px;">
					<a href="#">{{ comment.user }}</a>
					<img src="http://placehold.it/100x100">
				</div>
				<div class="comment-content alert-warning">
					<p>{{ comment.content }}</p>
				</div>
		</div>
 </div>
</template>

<script>
export default {
	name: 'PostComments',
	props: ['post'],
	components: {
	}
};

</script>
