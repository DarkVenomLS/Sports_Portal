// Get all buttons with the class "openPopupBtn"
var openPopupBtns = document.querySelectorAll(".openPopupBtn");
var popup = document.getElementById("popupForm");
var closeBtns = document.querySelectorAll(".closeBtn");

// Loop through each button and add a click event listener
openPopupBtns.forEach(function(btn) {
    btn.addEventListener("click", function() {
        popup.style.display = "block"; // Open the popup
    });
});

// Close the popup when clicking on the close button
openPopupBtns.forEach(function(closeBtn) {
    closeBtn.addEventListener("click", function() {
        popup.style.display = "none"; // Close the popup
    });
});
closeBtn.onclick = function() {
    popup.style.display = "none";
};

// Close the popup when clicking outside the popup content
window.onclick = function(event) {
    if (event.target == popup) {
        popup.style.display = "none";
    }
};
