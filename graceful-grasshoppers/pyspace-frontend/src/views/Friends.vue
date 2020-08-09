<template>
	<div class="home mt-5" style="margin: auto;">
		<FriendsList v-bind:logged-in-user="false" v-bind:user="user" />
	</div>
</template>

<script>
	import FriendsList from '@/components/user-friends';
	import User from '@/models/user';
	import axios from "../http-common.js";

	import authHeader from "@/services/auth-header";

	export default {
		name: 'Friends',
		data: function() {
			return {
				userId: this.$route.params.userId,
				user: new User({}),
			}
		},
		methods: {
			init() {
				if (this.userId == null) {
					axios
					.get("/users/self/", { headers: authHeader() })
						.then((response) => {
							Object.assign(this.user, response.data);
						})
					}
				}
			},
			mounted() {
				this.init();
			},
			components: {
				FriendsList,
			}
		}
	</script>
