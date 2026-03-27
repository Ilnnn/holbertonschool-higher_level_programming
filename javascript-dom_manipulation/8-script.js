window.addEventListener('DOMContentLoaded', (event) => {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const displayElement = document.getElementById('hello');

  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      displayElement.textContent = data.hello;
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
      displayElement.textContent = 'Error loading translation.';
    });
});