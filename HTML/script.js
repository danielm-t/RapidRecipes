console.log("aaaa") 
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