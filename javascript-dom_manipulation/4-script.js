const addItemBtn = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

if (addItemBtn && list) {
    addItemBtn.addEventListener('click', () => {
        const newItem = document.createElement('li');
        newItem.textContent = 'Item';

        list.appendChild(newItem);
    });
}