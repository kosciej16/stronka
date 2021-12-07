<template>
	<div class="square">
		<p class="text">{{ name }}</p>
	</div>
</template>

<script>
export default {
	name: "Tile",
	data() {
		return {};
	},
	props: {
		name: {
			type: String,
			required: true,
		},
	},
};
</script>

<style scoped>
.square {
	position: relative;
	height: 6.5em;
	width: 6.5em;
	border-style: solid;
}
.square .text {
	margin: 0;
	position: absolute;
	top: 50%;
	left: 50%;
	margin-right: -50%;
	transform: translate(-50%, -50%);
}
</style>
