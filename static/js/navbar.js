window.onscroll = function() {navbar_stick()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function navbar_stick() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

function logindrop(){
  document.getElementById("logindropdown").classList.toggle("showlogindrop");
}


window.onclick = function(event){
  if(!event.target.matches('.logindropbtn')){
    var dropdowns = document.getElementsByClassName("logindropmenu");
    var i;
    for(i=0;i<dropdowns.length;i++){
      var openDropdown = dropdowns[i];
      if(openDropdown.classList.contains('showlogindrop')){
        openDropdown.classList.remove('showlogindrop');
    }
  }
}
}

window.open(url, '_blank');