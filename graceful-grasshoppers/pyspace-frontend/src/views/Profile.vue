<template>
  <div class="container mt-5 mb-5" style="display: flex;">
    <UserProfile v-bind:user="user" />
    <UserContent v-bind:user="user" />
  </div>
</template>

<script>
	import UserProfile from '@/components/user-profile';
	import UserContent from '@/components/user-content';
	import User from '@/models/user';
	import axios from '../http-common.js';
	const authToken = JSON.parse(localStorage.getItem('user')).key;

	export default {
		name: 'Profile',
		data: function() {
			return {
				userId: this.$route.params.id,
				user: new User({}),
			}
		},
		components: {
			UserProfile,
			UserContent,
		},
		methods: {
			init() {
				axios
				.get(`/users/?username=${this.userId}`, { Authorization: "Token " + authToken })
				.then((response) => {
					console.log(response)
					console.log(this.userId)
					Object.assign(this.user, response.data[0]);
				})
			}
		},
		mounted() {
			this.init();
		},
	}
</script>

<style>
</style>