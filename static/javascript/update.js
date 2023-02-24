function updateRf() {
  // Send an AJAX request to the server to get the new value of "rf"
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  for (let i = 0; i < 2; i++) {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("rf"+i).innerHTML = JSON.parse(this.responseText)[i];
      }
    }
  };

  xhttp.open("GET", "/get_rf", true);
  xhttp.send();
}
console.log(document.getElementById("img").innerHTML)
if(status == 1){
  document.getElementById("img").setAttribute("src", "static/Img/Red.png")
  console.log(document.getElementById("img"))
}

// Update "rf" every 5 seconds
setInterval(updateRf, 5000);
