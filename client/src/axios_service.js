import axios from 'axios'

const instance = axios.create({
    // baseURL: 'http://127.0.0.1:8002/',
    baseURL: 'http://176.119.35.227:8002/',
    timeout: 1000,
    headers: {'Content-Type': 'application/json'},

});

export default {
	auth_login(username, pass) {
        return instance.post("/login", {"username": username, "password": pass}).then((data) => {
            localStorage.setItem("user", JSON.stringify({"username": username, "user_id": data.data.user_id}))
        }).catch(error => {
            console.log(error)
        })
	},
	auth_register(data) {
        console.log(data)
        return instance.post("/register", data)
	},
	get_events() {
        return instance.get("/event")
	},
	get_comments() {
        return instance.get("/comment")
	},
	event_signin(event_id) {
        var user_id = JSON.parse(localStorage.getItem("user")).user_id
        return instance.post(`/event/${event_id}`, user_id)
	},
	send_comment(comment, anonym) {
        var username = JSON.parse(localStorage.getItem("user")).username
        return instance.post("/comment", {"comment": comment, "author_name": username, anonym})
	},
	delete_comment(comment_id) {
        return instance.delete(`/comment/${comment_id}`)
	},
	event_signoff(event_id) {
        var user_id = JSON.parse(localStorage.getItem("user")).user_id
        return instance.delete(`/event/${event_id}?user_id=${user_id}`)
	},
}

