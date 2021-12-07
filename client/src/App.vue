<template>
	<div class="container">
		<router-link to="/login">
			<Tile :name="loggedInfo" />
		</router-link>
		<router-link to="/home">
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
		<router-view />
	</div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import Kontakt from "./components/Kontakt.vue";
import About from "./components/About.vue";
import Tile from "./components/Tile.vue";
import Events from "./components/Events.vue";

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
			var: 0,
		};
	},
	computed: {
		loggedInfo() {
			var som = JSON.parse(localStorage.getItem("user"));
			if (som == null) {
                return "zaloguj";
			}
            return "Witaj " + som["username"];
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
</style>
