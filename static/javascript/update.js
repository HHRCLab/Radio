function updateRf() {
  // Send an AJAX request to the server to get the new value of "rf"
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  for(let i=0;i<2;i++) {
    if(this.readyState == 4 && this.status == 200){
      document.getElementById("rf"+i).innerHTML = JSON.parse(this.responseText)[i];

      }
    }
  }
  
  try {
    xhttp.open("GET", "/get_rf", true);
    xhttp.send();
  } catch(Error) {
    console.log("Error during AJAX request:", Error);
  }
}

// Update "rf" every 5 seconds
setInterval(updateRf, 5000);