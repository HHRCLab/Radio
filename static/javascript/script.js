function updateIcons(iconStates) {
  for (var i = 0; i < iconStates.length; i++) {
    if (iconStates[i] == true) {
      document.getElementById("icon"+i).setAttribute("src", "static/Icons/100%.png");
    } else if (iconStates[i] == false) {
      document.getElementById("icon"+i).setAttribute("src", "static/Icons/25%.png");
    }
  }
}

function iconf(){
  var xhttp1 = new XMLHttpRequest();
  xhttp1.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var iconStates = JSON.parse(this.responseText);
      document.getElementById("test").innerHTML = this.responseText;
      console.log(this.responseText);
      updateIcons(iconStates);
    }
  };
  xhttp1.open("GET", "/get_status", true);
  xhttp1.send();
}

setInterval(iconf, 1000);

