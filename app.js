const password = prompt ("Enter your password");
if (password.length >= 6 && password.indexOf('') === -1) {
    console.log("Valid PASSWORD")
} else {
    console.log("Incorrect Format For Password!")
}
