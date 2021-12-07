<template>
	<div>
		<p><b>PUNKTACJA</b></p>
        <p> Punktacja za eventy </p>
        <li>Za uczestniczenie w evencie +1 KOT</li>
        <li>Za bycie niespóźnionym +1 KOT </li>
        <li>Za bycie w spódnicy lub sukience +1 KOT </li>
        <li>Za zapisanie się i nieprzyjście na event z limitem miejsc -5 KOT-ów</li>
        <li>Dodatkowo w zależności od eventu</li>
        <p> Punktacja jednorazowa </p>
        <li>Za dostanie się tutaj kodem bez niczyjej pomocy +3 KOT-y</li>
        <li>Za pomyślne skorzystanie z rozjechanego formularza rejestracji +3 KOT-y</li>
        <li>Za wysłanie sensownej treści w zakładce <b>o mnie</b> +1 KOT</li>
        <li>Za wysłanie "pustego" komentarza tamże +3 KOT-y</li>
        <li>Za zapisanie się na event w parze (jeszcze niemożliwe)</li>
        <li>Za podjęcie i zrealizowanie <router-link to="/event/piramida">wyzwania piramidy</router-link> +5 KOT-ów</li>
        <li>Więcej (prawdopdoobnie) się pojawi niedługo</li>
	</div>
</template>

<script>
import axios_service from "../axios_service.js"


export default {
	name: "Login",
	data() {
		return {
            username: null,
            email: null,
            pass: null};
	},
	methods: {
		register() {
            axios_service.auth_register(this.username)
            this.$router.push("/login")
		},
	},
};
</script>

<style scoped>
</style>

