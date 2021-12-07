<template>
	<div>
		<b>LOGOWANIE</b>
		<p>username: <input v-model="username" /></p>
		<p>hasło: <input id="pass" v-model="pass" /></p>
		<button @click="login">Logowanie</button><br><br>
        <p> Nie masz konta? <router-link to="/register"> Załóż je </router-link></p>
	</div>
</template>

<script>
import axios_service from "../axios_service.js"


export default {
	name: "Login",
	data() {
		return {
            username: null,
            pass: null};
	},
	methods: {
		login() {
            axios_service.auth_login(this.username, this.pass).then(() => {
                this.$router.push("/home")
            })
		},
	},
};
</script>

<style scoped>
#pass {
    margin-left: 2.9em
}
</style>

