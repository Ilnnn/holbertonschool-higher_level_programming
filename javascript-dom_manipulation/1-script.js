const clickableItem = document.querySelector('#red_header');

clickableItem.addEventListener('click', function() {
    const header = document.querySelector('header');
    header.style.color = '#FF0000'; 
});