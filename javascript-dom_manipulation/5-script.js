const updateBtn = document.querySelector('#update_header');
const headerElement = document.querySelector('header');

if (updateBtn && headerElement) {
    updateBtn.addEventListener('click', () => {
        headerElement.textContent = 'New Header!!!';
    });
}