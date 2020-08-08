<template>
	<div class="bordered w-75 m-5 p-4" style="margin: auto;">
		<Post v-bind:post="post" />
	</div>
</template>

<script>
import PostModel from '@/models/post';
import Post from '@/components/post';
import axios from "../http-common.js";

export default {
	data: function() {
		return {
			postId: this.$route.params.postId,
			post: new PostModel({}),
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
		},
	},
	components: {
		Post,
	},
	mounted: function() {
		this.init();
	}
}
</script>