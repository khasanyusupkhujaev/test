var publications = 0;
var groups = 0;
document.getElementById("publications").innerHTML = "<b>" + publications + "</b>" + " publications";
document.getElementById("groups").innerHTML = "<b>" + groups + "</b>" + " groups";

var x = document.getElementById("change");
x.addEventListener("mouseover", function(){
  x.style.color = "rgb(118,118,118)";
  x.style.textDecoration = "none";
})
var y = document.getElementById("change1");
y.addEventListener("mouseover", function(){
  y.style.color = "rgb(118,118,118)";
  y.style.textDecoration = "none";
})

var modal = document.getElementById("myModal");
var btn = document.getElementById("settingsbtn");
var span = document.getElementsByClassName("closee")[0];

btn.onclick = function() {
  modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}