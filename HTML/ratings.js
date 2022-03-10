document.addEventListener('DOMContentLoaded',rating)
const ratings = {
    gallery : 2.8}
function rating(){
    const starTotal = 5;
 
for(const rating in ratings) {  
  // 2
  const starPercentage = (ratings[rating] / starTotal) * 100;
  // 3
  const starPercentageRounded = `${(Math.round(starPercentage / 10) * 10)}%`;
  // 4
  document.querySelector(`.${rating} .stars-inner`).style.width = starPercentageRounded; 
  console.log("aaaa")
} 
}