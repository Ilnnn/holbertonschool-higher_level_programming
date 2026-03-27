const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const movieList = document.querySelector('#list_movies');

if (movieList) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Erreur lors du chargement des films');
            }
            return response.json();
        })
        .then(data => {
            data.results.forEach(film => {
                const li = document.createElement('li');
                li.textContent = film.title;
                movieList.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Erreur :', error);
            const errorItem = document.createElement('li');
            errorItem.textContent = "Impossible de charger la liste des films.";
            movieList.appendChild(errorItem);
        });
}