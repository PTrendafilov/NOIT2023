document.querySelector('#payment-type-hour').addEventListener('click', function() {
    document.querySelector('#textBoxDivFirst').style.display = 'block';
    document.querySelector('#textBoxDivSecond').style.display = 'none';
    document.querySelector('#payment-type-hour-input').focus();

  });
  
  document.querySelector('#payment-type-project').addEventListener('click', function() {
    document.querySelector('#textBoxDivFirst').style.display = 'none';
    document.querySelector('#textBoxDivSecond').style.display = 'block';
    document.querySelector('#payment-type-project-input').focus();
  });