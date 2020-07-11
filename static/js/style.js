
// transparent navbar turns white when scrolling down
// And returns transparent when is at the top of the screen
$(function () {
    $(window).on('scroll', function () {
        if ( $(window).scrollTop() > 10 ) {
            $('.navbar').addClass('active');
        } else {
            $('.navbar').removeClass('active');
        }
    });
});

// for message time on screen
// will delete image


setTimeout(function() {
  let delete_message = document.getElementById("message_container");
  delete_message.style.display = "none";
}, 3000);
