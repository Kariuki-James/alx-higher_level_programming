$(function() {
    $.get("https://fourtonfish.com/hellosalut/?lang=fr", function(response, textStatus) {
        $('DIV#hello').text(response.hello);
    })
});