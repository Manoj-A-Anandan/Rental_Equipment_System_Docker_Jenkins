// rentals/static/rentals/js/scripts.js

document.addEventListener("DOMContentLoaded", function() {
    // Add any interactive JavaScript functionality here
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            const daysInput = this.querySelector('input[name="days"]');
            if (daysInput.value <= 0) {
                event.preventDefault();
                alert("Please enter a valid number of days.");
            }
        });
    });
});
