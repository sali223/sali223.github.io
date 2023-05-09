const form = document.querySelector('#add-taco-form');
const input = document.querySelector('#taco-input');
const list = document.querySelector('#taco-list');

form.addEventListener('submit', function(event) {
  event.preventDefault();
  const task = input.value;
  if (task === '') return;
  const listItem = document.createElement('li');
  listItem.innerText = task;
  list.appendChild(listItem);
  input.value = '';
});

list.addEventListener('click', function(event) {
  if (event.target.tagName === 'LI') {
    event.target.classList.toggle('completed');
  }
});
