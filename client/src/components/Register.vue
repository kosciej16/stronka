<template>
	<div>
		<b>REJESTRACJA</b>
		<p>username: <input v-model="username" /></p>
		<p>
			email iiiiiii: <input v-model="email" /><Info
				msg="Czym jest to 'iiiiiii'? Nie wiedzieć dlaczego, bez tego wszystko się rozjeżdża. Zresztą <a href='/register2'> sprawdź sam</a>, jak nie wierzysz..."
			></Info>
		</p>
		<p>hasło iiiiiii: <input v-model="pass" /></p>
		<button @click="register">Załóż konto</button>
		<div v-if="error">
			<p>{{ error[0] }}</p>
			<div v-for="e in error.slice(1)" :key="e">
				<p v-if="e[1]" style="color: red">{{ e[0] }}</p>
				<p v-if="!e[1]" style="color: green">{{ e[0] }}</p>
			</div>
		</div>
	</div>
</template>

<script>
import axios_service from "../axios_service.js";
import Info from "./Info.vue";

export default {
	name: "Login",
	components: {
		Info,
	},
	data() {
		return {
			username: null,
			email: null,
			pass: null,
			error: null,
		};
	},
	methods: {
		register() {
			axios_service
				.auth_register({
					username: this.username,
					email: this.email,
					password: this.pass,
				})
				.then(() => {
					this.$router.push("/login");
				})
				.catch((error) => {
					this.error = error.response.data.detail;
				});
		},
	},
};
</script>

<style scoped>
</style>

