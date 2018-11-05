//star rating
var rating = 4.36;
const starTotal = 5;
const starPercentage = (rating/starTotal)*100;
const starPercentageRounded = `${(Math.round(starPercentage / 10) * 10)}%`;
document.querySelector(".stars-inner").style.width = starPercentageRounded; 



//progress bar
    console.clear();
    var meters = document.querySelectorAll('svg[data-value] .meter');
    
    meters.forEach(function (path) {
      var m;
      var length = path.getTotalLength();
      var value = parseInt(path.parentNode.getAttribute('data-value'));
      if(value<=1){
        m=1;}
      else{
        m=10;}
      var to = length * ((m - value) / m);
      path.getBoundingClientRect();
      path.style.strokeDashoffset = Math.max(0, to);
      //document.getElementById("Cumulative-Score").innerHTML = "4";
    });