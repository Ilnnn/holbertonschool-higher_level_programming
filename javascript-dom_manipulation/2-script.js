const redHeaderTrigger = document.querySelector('#red_header');
const headerElement = document.querySelector('header');

if (redHeaderTrigger && headerElement) {
    redHeaderTrigger.addEventListener('click', () => {
        headerElement.classList.add('red');
    });
}