let navBurger = document.getElementById("nav-burger");
let navMenu = document.getElementById("nav-menu");


navBurger.addEventListener("click", () => {
    navBurger.classList.contains("is-active") ? navBurger.classList.remove("is-active") : navBurger.classList.add("is-active")
    navMenu.classList.contains("is-active") ? navMenu.classList.remove("is-active") : navMenu.classList.add("is-active")
})