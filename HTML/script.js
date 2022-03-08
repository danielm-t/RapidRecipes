function searchbar() {
    let input = document.getElementById('searchbar').value
    input=input.toLowerCase();
    //to be used later
    //let x = document.getElementsByClassName(x);
      
    for (i = 0; i < x.length; i++) { 
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].style.display="none";
        }
        else {
            x[i].style.display="list-item";                 
        }
    }
}
const ratings = {
    hotel_a : 2.8}
function rating(){
    const starTotal = 5;
 
for(const rating in ratings) {  
  // 2
  const starPercentage = (ratings[rating] / starTotal) * 100;
  // 3
  const starPercentageRounded = `${(Math.round(starPercentage / 10) * 10)}%`;
  // 4
  document.querySelector(`.${rating} .stars-inner`).style.width = starPercentageRounded; 
}

}