$(function() {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(response, textStatus) {
        for (const film of response.results) {
            $('UL#list_movies').append('<li>' + film.title + '</li>');
        }
    })
});