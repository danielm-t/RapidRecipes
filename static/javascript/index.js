function getRatings(my_rating, my_slug) {
    const starTotal = 5;
    const starPercentage = (my_rating / starTotal) * 100;
    const starPercentageRounded = `${(Math.round(starPercentage / 10) * 10)}%`;
    document.querySelector(`#${my_slug} .stars-inner`).style.width = starPercentageRounded;
}