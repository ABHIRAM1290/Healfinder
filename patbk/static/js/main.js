// Simulate loading for demonstration
document.addEventListener("DOMContentLoaded", function() {
    // Show loading indicator
    document.getElementById("loadingContainer").style.display = "block";

    // Simulate loading delay (3 seconds)
    setTimeout(function() {
        // Hide loading indicator
        document.getElementById("loadingContainer").style.display = "none";
        // Show main content
        document.getElementById("mainContent").style.display = "block";
    }, 2000);
});
