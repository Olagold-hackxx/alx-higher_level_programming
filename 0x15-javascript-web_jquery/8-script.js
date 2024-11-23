$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function (data) {
  const results = data.results;
  for (let movie of results) {
	const item = $('<li></li>').text(movie.title);
	$('ul#list_movies').append(item);
  }
});
