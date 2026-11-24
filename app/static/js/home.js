// Page Load Message
window.onload = function () {
    alert("Welcome to My Django Website!");
};

// Button Click
const button = document.querySelector("button");

button.addEventListener("click", function () {
    alert("Thanks for visiting our website!");
});

// Navigation Click
const links = document.querySelectorAll("nav a");

links.forEach(function(link) {
    link.addEventListener("click", function(event) {
        event.preventDefault();
        alert("You clicked on " + this.textContent);
    });
});

// Change Footer Year Automatically
const footer = document.querySelector("footer p");

footer.innerHTML = "&copy; " + new Date().getFullYear() + " My Django Website. All Rights Reserved.";