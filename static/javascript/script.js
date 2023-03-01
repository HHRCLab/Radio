function iconf(){
  for (var i = status.length - 1; i >= 0; i--) {
      if (status == true) {
        document.getElementById("icon").setAttribute("src", "static/Icons/100%.png");
      } else {
        document.getElementById("icon").setAttribute("src", "static/Icons/50%.png");
      }
  }
    
}

setInterval(iconf, 1000);