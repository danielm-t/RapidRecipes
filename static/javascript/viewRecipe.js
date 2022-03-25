function starPercentage(value_){
    const starTotal = 5;
    const starPercentage = (value_ / starTotal) * 100;
    return `${(Math.round(starPercentage / 10) * 10)}%`;
}

function getRatings(my_slug, rating, difficulty) {
    document.querySelector(`#${my_slug}-rating .stars-inner`).style.width = starPercentage(rating);
    document.querySelector(`#${my_slug}-difficulty .stars-inner`).style.width = starPercentage(difficulty);
}

function WHAT(){
    console.log("WGAT");
}