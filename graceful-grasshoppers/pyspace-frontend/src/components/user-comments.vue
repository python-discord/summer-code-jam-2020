<template>
	<div class="user-friends flex-col">
		<p class="alert-info font-weight-bold">Profile Comments</p>
		<div class="friend flex-row" v-for="comment in user.profileComments" :key="comment.content">
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
// @ is an alias to /src

// import axios from "../http-common";
import axios from "axios";
import User from "../models/user";
// const authToken = JSON.parse(localStorage.getItem('user')).key;

export default {
	name: 'UserFriends',
	data: function() {
		return {
			user: new User({}),
		};
	},
	methods: {
		init() {
			axios
			.get('http://www.json-generator.com/api/json/get/bUZiRPcslK?indent=2')
			.then((response) => {
				Object.assign(this.user, response.data[0]);
			})
		}
	},
	mounted() {
		this.init();
	},
	components: {
	}
};

</script>
