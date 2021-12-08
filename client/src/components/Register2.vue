<template>
	<div id="register2">
		<p>user <input v-model="user" /></p>
		<p>name: <input v-model="name" /></p>
		<p>ema <input v-model="ema" /></p>
		<p>il: <input v-model="il" /></p>
		<p>h <input v-model="p" /></p>
		<p>asło: <input v-model="ass" /></p>
        <div v-if="error">
            <p> {{ error[0] }} </p>
            <div v-for="e in error.slice(1)" :key="e">
                <p v-if="e[1]" style="color:red;"> {{ e[0] }} </p>
                <p v-if="!e[1]" style="color:green;"> {{ e[0] }} </p>
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
			user: null,
			name: null,
			ema: null,
			il: null,
			p: null,
            ass: null,
            result: null,
            error:null,
		};
	},
    mounted() {
        var el = document.getElementById("register2")
        var a = Array.from(el.children)
        a.forEach(function(item) {
            item.style.position = "absolute"
            item.style.left = `${Math.random() * 30 + 30}em`
            item.style.bottom = `${Math.random() * 30 + 10}em`
        })
        this.randomize(el, "RE")
        this.randomize(el, "JE")
        this.randomize(el, "STR")
        this.randomize(el, "AC")
        this.randomize(el, "JA")
        this.with_button(el, "Zał", this.re)
        this.with_button(el, "óż", this.gi)
        this.with_button(el, " kon", this.st)
        this.with_button(el, " to", this.er)
        console.log("AAA")
    },
	methods: {
        randomize(el, text) {
            var x = document.createElement("span")
            x.style.position = "absolute"
            x.style.left = `${Math.random() * 30 + 30}em`
            x.style.bottom = `${Math.random() * 30 + 10}em`
            var t = document.createTextNode(text)
            x.appendChild(t)
            el.prepend(x)
        },
        with_input(el, model) {
            var p = document.createElement("p")
            p.style.position = "absolute"
            p.style.left = `${Math.random() * 30 + 30}em`
            p.style.bottom = `${Math.random() * 30 + 10}em`
            p.textContent = model
            var a = document.createElement("input")
            console.log(model)
            a.setAttribute("v-model",model)
            p.appendChild(a)
            el.appendChild(p)
        },
        with_button(el, text, fun) {
            var p = document.createElement("p")
            p.style.position = "absolute"
            p.style.left = `${Math.random() * 30 + 30}em`
            p.style.bottom = `${Math.random() * 30 + 10}em`
            p.textContent = text
            p.onclick = fun
            el.appendChild(p)
        },
		re() {
            this.result = "1"
		},
		gi() {
            this.result += "2"
		},
		st() {
            this.result += "3"
		},
		er() {
            this.result += "4"
            if (this.result == "1234" && this.name && (this.il || !this.ema) && this.ass) {
                var username = this.user + this.name
                var email = this.ema + this.il
                var password = this.p + this.ass
                axios_service.auth_register({username, email, password}).then(() => {
                    this.$router.push("/login");
            }).catch(error => {
                this.error = error.response.data.detail
            })

            }
            else {
                this.error = ["Coś jest ewidentnie źle wyklikane :("]
            }
		},
	},
};
</script>

<style scoped>
</style>

