<template>
	<span class="info">
        <img src="src/assets/info-16.ico">
        <div class="info_border">
		<span class="info_text" v-html=msg></span>
        </div>
	</span>
</template>

<script>
export default {
	name: "Info",
  props: {
    msg: String
  },
	data() {
		return {
		};
	},
}
</script>

<style scoped>
.info_text {
    color: green;
}
.info:hover div {
    visibility: visible;
}
.info {
    margin-left: 0.5em
}
.info_border {
    width: 20em;
    border: solid;
    visibility: hidden;
    color: green;
}
</style>
