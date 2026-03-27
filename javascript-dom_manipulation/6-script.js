window.addEventListener('DOMContentLoaded', () => {
    const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
    const characterElement = document.querySelector('#character');

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Erreur réseau');
            }
            return response.json();
        })
        .then(data => {
            characterElement.textContent = data.name;
        })
        .catch(error => {
            console.error('Erreur :', error);
            characterElement.textContent = 'Erreur de chargement';
        });
});