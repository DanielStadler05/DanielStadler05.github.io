var el = document.getElementById("email");
var addr = "email";
addr = addr + "@" + "danielstadler.se";
el.href = "mailto:" + addr;
el.innerText = addr;
