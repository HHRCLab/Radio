function updateIcons(iconStates) {
  for (var i = 0; i < iconStates.length; i++) {
    try{
      if (iconStates[i] == true) {
        document.getElementById("icon"+i).setAttribute("src", "static/Icons/100%.png");
      } else if (iconStates[i] == false) {
        document.getElementById("icon"+i).setAttribute("src", "static/Icons/25%.png");
      }
    }catch(TypeError){
      console.log("icon-null")
    }
  }
}



function iconf(){
  var xhttp1 = new XMLHttpRequest();

  xhttp1.open("GET", "/get_status", true);
  xhttp1.send();

  xhttp1.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var iconStates = JSON.parse(this.responseText);
      for(let i=0;i<2;i++){
        // document.getElementById("test"+i).innerText = iconStates[i];
        if(iconStates[i] == false){
          document.getElementById("icon"+i).setAttribute("src", "static/Icons/no connection2.png");
        }
      }
    }
  }
}

setInterval(iconf, 3000);

