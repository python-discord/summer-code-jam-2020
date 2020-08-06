<template>
	<div>
		<div>
			<p class="alert-warning font-weight-bold">{{ user.name }}'s latest post :</p>
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
// @ is an alias to /src

// import axios from "../http-common";
import axios from "axios";
import User from "../models/user";
// const authToken = JSON.parse(localStorage.getItem('user')).key;

export default {
	name: 'UserAbout',
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
