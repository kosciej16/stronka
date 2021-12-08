<template>
	<div>
		<p class="header"><b>CZEŚĆ!</b></p>
		Wydarzyło się trochę nowości ostatnimi czasy, co sprawiło, że wstrzymałem
		swoje życie tułacza na dwa miesiące i postanowiłem wynająć mieszkanie w
		Warszawie do końca stycznia.
		<li>Czy znajdzie się miejsce do tańczenia? <b>Oczywiście i to dużo!</b></li>
		<li>
			Czy można tu grać i śpiewać?
			<b>Ile tylko dusza (i sąsiedzi?) zapragnie!</b>
		</li>
		<li>A planszówki? <b>Krzesła i duży stół czekają!</b></li>
		<li>
			A... można tu zrobić pokaz ognia? <b>Nie wiem... ale zrobimy!</b><br />
		</li>
		Czasu tak mało, a możliwości tak dużo... &#128512;<br />
		Dlatego specjalnie dla Was, harmonogram najbliższych wydarzeń, abyście mogli
		wybrać, co interesuje Was najbardziej.<br /><br />
		ALE!<br />
		To nie wszystko. Dodatkowo będziecie zdobywać
		<b>Kupony Odrocz(o)nej Tułaczki</b>, które następnie wymienicie na
		wspaniałe gadżety lub przeżycia.<br />
		Masz jakieś uwagi? Coś nie działa? Należy Ci się więcej KOT-ów, niż masz?
		<router-link to="/kontakt">Napisz</router-link>
	</div>
</template>

<script>
export default {
	name: "Home",
	data() {
		return {};
	},
};
</script>

<style scoped>
p {
	width: 10em;
}
</style>
