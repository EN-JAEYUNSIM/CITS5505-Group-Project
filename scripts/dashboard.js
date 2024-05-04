// Change user status 
$(document).ready(function() {
    $.get('/user-status', function(response) {
        if (response.logged_in) {
            $('#user-links').html('<a href="/my-account">My Account</a>');
        } else {
            $('#user-links').html('<a href="/login">Log In</a> <a href="/signup">Sign Up</a>');
        }
    });
});

// Videos/Trending/Waitforanswering tags
function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className  += " active";
}

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('.tablink[onclick*="Trending"]').click();
});

