function updateRf() {
  // Send an AJAX request to the server to get the new value of "rf"
  var xhttp = new XMLHttpRequest();

  try {
    xhttp.open("GET", "/get_rf", true);
    xhttp.send();
  } catch(Error) {
    console.log("Error during AJAX request:", Error);
  }


  xhttp.onreadystatechange = function() {
  let rfList = JSON.parse(this.responseText);
  for(let i=0;i<2;i++) {
    if(this.readyState == 4 && this.status == 200){
      document.getElementById("rf"+i).innerHTML = rfList[i];
      console.log("fff");
      }

    if(rfList[i] < 11){
      document.getElementById("icon"+i).setAttribute("src","static/Icons/75%Y.png");
    }if(rfList[i] < 8){
      document.getElementById("icon"+i).setAttribute("src","static/Icons/50%Y.png");
    }if(rfList[i] < 5){
      document.getElementById("icon"+i).setAttribute("src","static/Icons/25%R.png");
    }if(rfList[i] > 11){
      document.getElementById("icon"+i).setAttribute("src","static/Icons/100%.png");
    }

    }
  }
}

// Update "rf" every 5 seconds
setInterval(updateRf, 2500);