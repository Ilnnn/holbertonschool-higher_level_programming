const updateBtn = document.querySelector('#update_header');
const header = document.querySelector('header');

updateBtn.addEventListener('click', () =>
{
    header.textContent = 'New Header!!!';
});