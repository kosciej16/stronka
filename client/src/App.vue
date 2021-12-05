<template>
	<div class="container">
		<router-link to="/kontakt">
			<Tile name="kontakt" />
		</router-link>
		<router-link to="/about">
			<Tile name="o mnie" />
		</router-link>
		<router-link to="/login">
			<Tile :name=loggedInfo />
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

export default {
	name: "App",
	components: {
		HelloWorld,
		Kontakt,
		About,
		Tile,
	},
	data() {
		return {
			var: 0,
		};
	},
    computed: {
        loggedInfo() {
            var som = localStorage.getItem("username", "zaloguj")
            if (som) {
                return som
            }
            return "zaloguj"
        }
    }
};
</script>

<style scoped>
.container {
	float: left;
	display: grid;
	grid-template-columns: auto auto;
	grid-template-rows: auto auto;
	column-gap: 2em;
	row-gap: 1em;
	margin-left: 10em;
}
.main {
	float: left;
	margin-left: 3em;
}
.vl {
    margin-left:3em;
	float: left;
	border-left: 6px solid green;
	height: 500px;
}
</style>
