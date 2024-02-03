const main = document.querySelector('.main');
main.style.width = '1000px';
main.style.height = '1000px';
main.style.backgroundColor = 'black';

const box = document.createElement('div');
const b = {x:50, y:0, w:40, h:40}
box.style.backgroundColor = 'green';
box.style.borderRadius = '50%';
box.style.width = '${b.w}px'
box.style.height = '${b.h}px'
box.style.position = 'relative';
box.style.left = '${b.x}px';
ball.style.top = '${b.y}px;';
