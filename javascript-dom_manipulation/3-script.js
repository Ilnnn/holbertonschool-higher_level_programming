const toggleBtn = document.querySelector('#toggle_header');
const header = document.querySelector('header');

if (toggleBtn && header) {
  toggleBtn.addEventListener('click', () => {
    if (header.classList.contains('red')) {
      header.classList.replace('red', 'green');
    } else {
      header.classList.replace('green', 'red') || header.classList.add('red');
    }
  });
}