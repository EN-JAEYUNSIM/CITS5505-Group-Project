// For index page: add bookmark function
function addBookmark() {
    alert('Press ' + (navigator.userAgent.toLowerCase().indexOf('mac') != -1 ? 'Cmd' : 'Ctrl') + '+D to bookmark this page.');
}

// For profile page: edit profile in the same page
$(document).ready(function() {
    $('#edit-profile-button').click(function() {
        $('#edit-profile-form').toggle();
    });

    $('#edit-form').submit(function(event) {
        event.preventDefault();  // 防止默认表单提交
        var aboutMeText = $('textarea[name="about_me"]').val();
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: function(response) {
                $('#about-me-text').text(aboutMeText);
                $('#edit-profile-form').hide();
            },
            error: function(error) {
                console.error('Error updating profile:', error);
            }
        });
    });
});



