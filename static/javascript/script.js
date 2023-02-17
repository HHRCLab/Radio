window.addEventListener('load', () => {
      let currentValue = document.getElementById('radio').innerHTML;  // get the initial value of the variable
  console.log('Initial value:', currentValue);

  setInterval(() => {
    let newValue = document.getElementById('radio').innerHTML;  // get the current value of the variable
    console.log('New value:', newValue);
    if (newValue == currentValue) {
      console.log('Value has not changed');
    } else {
      currentValue = newValue;
      document.getElementById('radio').innerHTML = currentValue;  // update the text of the HTML element
      console.log('Updated value:', currentValue);
    }
  }, 1000);
});


