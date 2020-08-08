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
	import authHeader from '@/services/auth-header';

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
				const query_url = this.userId == null ? '/users/self/' : `/users/?username=${this.userId}`;
				console.log(query_url)
				axios
				.get(query_url, { headers: authHeader() })
				.then((response) => {
					Object.assign(this.user, response.data);
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