// Instructions
// In this exercise we will be creating a webpage with a black background as the universe and we will fill the universe with planets and their moons.
// We will provide the HTML page.
// You only have to work with a JS file.
// Create an array which value is the planets of the solar system.
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
// Each planet should have a different background color. (Hint: you could add a new class to each planet - each class containing a different background-color).
// Finally append each div to the <section> in the HTML (presented below).
// Bonus: Do the same process to create the moons.
// Be careful, each planet has a certain amount of moons. How should you display them?
// Should you still use an array for the planets ? Or an array of objects ?

let solarSistem = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
let sec = document.getElementsByTagName('section')
function divFun() {
let x = 1
    for (let i = 0; i < solarSistem.length; i++) {
        var divs = document.createElement('div');
        document.body.appendChild(divs);
        divs.className = 'planet'
        divs.setAttribute('id', x)
        x++
    }
    let mercury = document.getElementById(1).style.background = 'red';
    let venus = document.getElementById(2).style.background = 'orange';
    let earth = document.getElementById(3).style.background = 'yellow';
    let mars = document.getElementById(4).style.background = 'green';
    let jupiter = document.getElementById(5).style.background = 'lightblue';
    let saturn = document.getElementById(6).style.background = 'blue';
    let uranus = document.getElementById(7).style.background = 'purple';
    let neptune = document.getElementById(8).style.background = 'white';
}

console.log(divFun());