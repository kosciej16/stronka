export function signedUser() {
    var user = localStorage.getItem("user")
    console.log(user)
    if (user) {
        return JSON.parse(user)
    }
    return user
}

export function checkPassword(pass) {
    error = ""
    if (pass.length > 2) {
        error += "Hasło nie może być dłuższe"
    }
}
