<script>
	import axios from "../http-common.js";
	export default {
		name: 'Random',
		mounted: function() {
			axios
			.get("/users/?random=1")
			.then((response) => {
				this.$router.push('/profile/' + response.data[0].username);
			})
		}
	}
</script>