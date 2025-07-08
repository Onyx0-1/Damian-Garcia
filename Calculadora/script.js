const display = document.getElementById('display');
const buttons = document.querySelectorAll('.buttons button');

buttons.forEach(btn => {
  btn.addEventListener('click', () => {
    const val = btn.textContent;

    if (val === 'AC') {
      display.textContent = '';
    } else if (val === 'DEL') {
      display.textContent = display.textContent.slice(0, -1);
    } else if (val === '=') {
      calculate();
    } else {
      if (display.textContent === '0' || display.textContent === 'Error') {
        display.textContent = val;
      } else {
        display.textContent += val;
      }
    }
  });
});

function calculate() {
  let expr = display.textContent
    .replace(/x/, '*')
    .replace(/÷/, '/')
    .replace(/\^/, '**')
    .replace(/√(\d+(\.\d+)?)/g, 'Math.sqrt($1)')
    .replace(/cos(\d+(\.\d+)?)/g, 'Math.cos($1)')
    .replace(/tan(\d+(\.\d+)?)/g, 'Math.tan($1)')
    .replace(/(\d+(\.\d+)?)%/g, '($1/100)')


  try {
    const result = eval(expr);
    display.textContent = isFinite(result) ? result : 'Error';
    display.classList.add('result');
    setTimeout(() => display.classList.remove('result'), 400);
  } catch {
    display.textContent = 'Error';
  }
}