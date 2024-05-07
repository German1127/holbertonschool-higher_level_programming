$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});