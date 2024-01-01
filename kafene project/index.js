let loginCredentials = localStorage.getItem("loginStatus");
if(loginCredentials == "false" || loginCredentials == null){

}else{
    location.assign("./orders.html");
}

var userName = document.querySelector(".loginusername");
var userPassword = document.querySelector(".loginpassword");
let submitBtn = document.getElementById("submit");
let form = $("#login-form");
form.submit(function(e){
    e.preventDefault();

    const user = userName.value;
    const password = userPassword.value;
    var mObj = {
      username: user,
      password: password,
    };
    // // Checking the Username and password provided by user to meet the required condition -----
    if (user === password && user !== "" && password !== "") {
        alert("Login‌ ‌Successful");
        localStorage.setItem("loginStatus", JSON.stringify(mObj));
        location.assign("./orders.html");
    }
    else {
        alert("Please‌‌ enter‌ ‌valid‌ ‌credentials!");
    }
})

document.getElementById("sign-out").style.display = "none";