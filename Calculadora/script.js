const display = document.getElementById('display');
const buttons = document.querySelectorAll('.buttons button');

buttons.forEach(btn => {
  btn.addEventListener('mousedown',   () => btn.classList.add('pressed'));
  btn.addEventListener('touchstart',  () => btn.classList.add('pressed'));
  btn.addEventListener('mouseup',     () => btn.classList.remove('pressed'));
  btn.addEventListener('mouseleave',  () => btn.classList.remove('pressed'));
  btn.addEventListener('touchend',    () => btn.classList.remove('pressed'));
  
  btn.addEventListener('click', () => {
    const val = btn.textContent;

    if (val === 'AC') {
      display.textContent = '';
    } 
    else if (val === 'DEL') {
      display.textContent = display.textContent.slice(0, -1);
    } 
    else if (val === '=') {
      calculate();
    } 
    else {
      display.textContent += val;
    }
  });
});

function calculate() {
  let expr = display.textContent
    .replace(/x/g, '*')
    .replace(/÷/g, '/')
    .replace(/\^/g, '**')
    .replace(/√/g, 'Math.sqrt')
    .replace(/cos/g, 'Math.cos')
    .replace(/tan/g, 'Math.tan');

  try {
    const result = eval(expr);
    if (typeof result === 'number' && isFinite(result)) {
      display.textContent = result;
      display.classList.add('result');
      setTimeout(() => display.classList.remove('result'), 400);
    } else {
      display.textContent = 'Error';
    }
  } catch {
    display.textContent = 'Error';
  }
}
