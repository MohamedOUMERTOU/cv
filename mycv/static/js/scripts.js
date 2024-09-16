// scripts.js

// Example: Alert message when a button is clicked
document.addEventListener('DOMContentLoaded', function () {
    const alertButton = document.querySelector('.btn');

    if (alertButton) {
        alertButton.addEventListener('click', function () {
            alert('Button clicked!');
        });
    }
});

// Example: Smooth scrolling effect for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
