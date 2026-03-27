const updateBtn = document.querySelector('#update_header');
const headerTitle = document.querySelector('header h1'); 

if (updateBtn && headerTitle) {
    updateBtn.addEventListener('click', () => {
        headerTitle.textContent = 'New Header!!!';
    });
}