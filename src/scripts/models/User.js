class User {
    constructor(username, password) {
        this.username = username;
        this.password = password;
    }

    getUsername() {
        return this.username;
    }

    setPassword(password) {
        this.password = password;
    }

    getPassword() {
        return this.password;
    }
}