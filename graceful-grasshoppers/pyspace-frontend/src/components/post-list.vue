<template>
	<div class="bordered w-75 mt-5" style="margin: auto;">
		<h4 class="font-weight-bold">Posts</h4>
		<div v-for="post in posts" class="bordered flex-row">
			<div class="flex-col" style="width: 110px;">
				<img src="http://placehold.it/100x100">
				<a href="#">{{ post.author.name }}</a>
			</div>
			<div>
				<p class="alert-warning p-1 font-weight-bold">{{ post.title }}</p>
				<p>{{ post.content }}</p>
				<img class="w-100" src="http://www.mandysam.com/img/random.jpg">
				<div class="reactions flex-row">
					<button class="likes p-1 alert-success">{{ post.likes }} Positive Reactions</button>
					<button class="dislikes p-1 alert-danger">{{ post.dislikes }} Negative Reactions</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
// @ is an alias to /src

// import axios from "../http-common";
import axios from "axios";
// const authToken = JSON.parse(localStorage.getItem('user')).key;

export default {
	name: 'UserAbout',
	props: ['posts'],
};

</script>
