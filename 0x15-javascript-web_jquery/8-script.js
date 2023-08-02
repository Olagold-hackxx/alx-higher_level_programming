const url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (data) {
  const results = data.results;
  for (let movie of results) {
	const item = $('<li></li>').text(movie.title);
	$('ul#list_movies').append(item);
  }
});
