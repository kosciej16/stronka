<template>
	<div>
		<b>LOGOWANIE</b>
		<p>username: <input v-model="username" /></p>
		<p>hasło: <input id="pass" v-model="pass" /></p>
		<button @click="login">Logowanie</button><br /><br />
		<p>Nie masz konta? <router-link to="/register"> Załóż je </router-link></p>
        <p v-if="error">{{ error }}</p>
	</div>
</template>

<script>
import axios_service from "../axios_service.js";

export default {
	name: "Login",
	data() {
		return {
			error: null,
			username: null,
			pass: null,
		};
	},
	methods: {
		login() {
			axios_service
				.auth_login(this.username, this.pass)
				.then((data) => {
					localStorage.setItem(
						"user",
						JSON.stringify({
							username: this.username,
							user_id: data.data.user_id,
						})
					);
                    this.$emit("login", this.username)
					this.$router.push("/");
				}).catch(() => {
					this.error = "Coś nie pykło :("
				});
		},
		logout() {
            this.$emit("login", null)
            this.$router.push("/");
		},
	},
};
</script>

<style scoped>
#pass {
	margin-left: 2.9em;
}
</style>

