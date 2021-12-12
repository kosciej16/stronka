<template>
	<div class="container">
		<router-link v-if="!username" to="/login">
			<Tile name="Zaloguj" />
		</router-link>
		<a id="logout" v-else :onclick="logout">
			<Tile name="Wyloguj" />
		</a>
		<router-link to="/">
			<Tile name="główna" />
		</router-link>
		<router-link to="/points">
			<Tile name="punktacja" />
		</router-link>
		<router-link to="/event">
			<Tile name="wydarzenia" />
		</router-link>
		<router-link to="/ranking">
			<Tile name="ranking" />
		</router-link>
		<router-link to="/kontakt">
			<Tile name="kontakt" />
		</router-link>
		<router-link to="/about">
			<Tile name="o mnie" />
		</router-link>
	</div>
	<div class="vl"></div>
	<div class="main">
		<p id="user_header" v-if="username">Witaj {{ username }}</p>
		<router-view v-on:login="login" />
	</div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import Kontakt from "./components/Kontakt.vue";
import About from "./components/About.vue";
import Tile from "./components/Tile.vue";
import Events from "./components/Events.vue";
import { signedUser } from "./utils/auth";

export default {
	name: "App",
	components: {
		HelloWorld,
		Kontakt,
		About,
		Tile,
		Events,
	},
	data() {
		return {
			username: null,
		};
	},
    mounted() {
        var user = signedUser()
        if (user){
            this.username = user.username
        }
        else  {
            this.username = null
        }
    },
	computed: {
		loggedInfo() {
			if (this.username == null) {
				return "Zaloguj";
			}
			return "Wyloguj";
		},
	},
	methods: {
		login(username) {
			console.log("WORK");
			this.username = username;
		},
		logout() {
			localStorage.removeItem("user");
			this.username = null;
		},
	},
};
</script>

<style scoped>
.container {
	width: 15em;
	float: left;
	display: grid;
	grid-template-columns: auto auto;
	grid-template-rows: auto auto;
	column-gap: 2em;
	row-gap: 1em;
	margin-left: 10em;
}
.main {
	margin-left: 30em;
}
.vl {
	margin-left: 3em;
	float: left;
	border-left: 6px solid green;
	height: 500px;
	width: 0;
}
#user_header {
	font-family: Cursive;
	position: absolute;
	right: 4em;
	top: 1em;
}
#logout {
	cursor: pointer;
}
</style>
