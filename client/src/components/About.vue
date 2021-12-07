<template>
	<div>
		<p><b>O MNIE</b></p>
		Sam <span @click="send_comment">wyślij</span> wypowiedź &#128512;<br />
		Wiadomo, że gdybym to ja miał się opisać zrobiłbym to w samych
		superlatywach, dlatego to zadanie zostawiam Wam.
		<Info
			msg="Aby zapobiec nienawiści w internecie skomplikowany algorytm usuwa słowo . Choć w zasadzie jest on dość glupi... "
		></Info>
		<div v-if="signedUser()">
			<textarea
				class="user_comment"
				v-model="user_comment"
				placeholder="miejsce na Twój osąd"
			></textarea>
			<input type="checkbox" id="anonym" v-model="anonym" />
			<label for="anonym">Anonimowo</label>
		</div>
		<div v-else>
			<router-link to="/login">Zaloguj się</router-link>, aby móc dodawać opinie
		</div>
		<div id="all_comments" v-for="(comment, index) in comments" :key="index">
			<div class="box">
				<p class="author">
					&#128100; {{ comment.anomised }}
					<span
						@click="delete_comment(comment.comment_id)"
						v-if="is_mine(comment.author_name)"
						class="tick"
					>
						usuń
					</span>
				</p>
				<p class="comment">{{ comment.comment }}</p>
			</div>
			<Info
				v-if="is_mine(comment.author_name)"
				id="abc"
				msg="Po co się ograniczać, możesz usunąć dowolny komentarz! Wystarczy wysłać request DELETE na /comment/{comment_id}"
			></Info>
		</div>
	</div>
</template>

<script>
import axios_service from "../axios_service.js";
import { signedUser } from "../utils/auth";
import Info from "./Info.vue";
export default {
	name: "About",
	components: {
		Info,
	},
	data() {
		return {
			anonym: false,
			comments: [],
			user_comment: null,
		};
	},
	mounted() {
		this.refresh();
	},
	methods: {
		signedUser,
		is_mine(author_name) {
			return signedUser() && author_name === signedUser().username;
		},
		refresh() {
			this.user_comment = null;
			axios_service.get_comments().then(({ data }) => {
				this.comments = data;
			});
		},
		send_comment() {
			axios_service.send_comment(this.user_comment, this.anonym).then(() => {
				this.refresh();
			});
		},
		delete_comment(comment_id) {
			axios_service.delete_comment(comment_id).then(() => {
				this.refresh();
			});
		},
	},
};
</script>

<style scoped>
.author {
	margin-left: 1em;
	color: #1b521b;
	font-weight: bold;
}
.box {
	float: left;
	margin-top: 1em;
	border-style: solid;
	width: 30em;
}
.comment {
	margin-left: 1em;
}
.tick {
	cursor: pointer;
	float: right;
	margin-right: 2em;
}
.user_comment {
	margin-top: 3em;
	height: 4em;
	width: 40em;
}
#abc {
	float: left;
	position: relative;
	top: 1.5em;
}
#anonym {
	margin-left: 2em;
	transform: scale(1.5);
}
</style>
