// 🌟 Exercise 1 : Change The Article
// Instructions
// Copy the code below, into a structured HTML file:
// <article>
//     <h1> Some Facts </h1>
//     <h2> The Chocolate </h2>
//     <h3> History of the chocolate </h3>
//     <p> Chocolate is made from tropical Theobroma cacao tree seeds. 
//     Its earliest use dates back to the Olmec civilization in Mesoamerica.</p>
//     <p> After the European discovery of the Americas, chocolate became 
//     very popular in the wider world, and its demand exploded. </p>
//     <p> Chocolate has since become a popular food product that millions enjoy every day, 
//     thanks to its unique, rich, and sweet taste.</p> 
//     <p> But what effect does eating chocolate have on our health?</p> 
// </article>
// Using a DOM property, retrieve the h1 and console.log it.
// Using DOM methods, remove the last paragraph in the <article> tag.
// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)
// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)



//1
let h1 = document.getElementsByTagName('h1')[0]
console.log(h1);
//2
let paragraph = document.querySelector('article').lastElementChild
paragraph.remove()
//3
document.getElementsByTagName('h2')[0].addEventListener('click', h2Click)
function h2Click() {
    document.getElementsByTagName('h2')[0].style.background = 'red'
}
//4
let h3 = document.getElementsByTagName('h3')[0].addEventListener('click', h3Click)
function h3Click(){
    document.getElementsByTagName('h3')[0].style.display = 'none'
}
//5
let btn = document.createElement('button')
btn.innerHTML = 'click me'
document.body.appendChild(btn)
btn.addEventListener('click', btnClick)
function btnClick() {
    document.body.style.fontWeight = 'bold'
}

//6
h1 = document.getElementsByTagName('h1')[0].addEventListener('mouseover', h1Hover)
function h1Hover(){
    document.body.style.fontSize =  Math.floor(Math.random()*100) + 'px'
}

//7
let p2 = document.getElementsByTagName('p')[1].addEventListener('mouseover', p1Hover)
function p1Hover(){
    document.getElementsByTagName('p')[1].style.display = 'none'
}




// 🌟 Exercise 2 : Work With Forms
// Instructions
// Copy the code below, into a structured HTML file:
// <form>
//   <label for="fname">First name:</label><br>
//   <input type="text" id="fname" name="fname"><br>
//   <label for="lname">Last name:</label><br>
//   <input type="text" id="lname" name="lname"><br><br>
//   <input type="submit" value="Submit" id="submit">
// </form> 
// <ul class="usersAnswer"></ul>
// Retrieve the form and console.log it.
// Retrieve the inputs by their id and console.log them.
// Retrieve the inputs by their name attribute and console.log them.
// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.
//1
let form = document.forms[0]
let form1 = document.getElementsByTagName('form')[0]
console.log(form1);
//2
let fname = document.getElementById('fname')
console.log(fname);
let lname = document.getElementById('lname')
console.log(lname);
let submit = document.getElementById('submit')
console.log(submit);
//3
let name1 = document.getElementsByName('fname')
let name2 = document.getElementsByName('lname')
//4
let ul = document.getElementsByClassName('usersAnswer')[0]
console.log(ul);
let formF = document.getElementsByTagName('form')[0]
formF.addEventListener('click', function(event){
    event.preventDefault()
    let inpt1 = document.getElementsByTagName('input')[0].value
    let inpt2 = document.getElementsByTagName('input')[1].value
    if (inpt1.length > 0  && inpt2.length > 0) {
    console.log(inpt1 + ' ' + inpt2);
    let li1 = document.createElement('li')
    let li2 = document.createElement('li')
    li1.innerText = inpt1
    li2.innerText = inpt2
     ul.appendChild(li1)
     ul.appendChild(li2)
    }
})


// 🌟 Exercise 3 : Transform The Sentence
// Instructions
// Add this sentence to your HTML file then follow the steps :
// <p><strong>Hello</strong> I hope you are enjoying <strong>this</strong> class. At the
// <strong>end</strong> you <strong>will</strong> be great Developers!
// <strong>Enjoy</strong> the <strong>JavaScript </strong> lessons</p>
// In the JS file:
// Declare a global variable named allBoldItems.
// Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.
// Create a function called highlight() that changes the color of all the bold text to blue. 
// Create a function called return_normal() that changes the color of all the bold text back to black. 
// Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example

//1
var allBoldItems = ' '
//2
function getBold_items(){
    for (let i = 0; i < 6; i++) {
        let strng = document.getElementsByTagName('strong')[i].innerText
        allBoldItems += strng + ' '
    }
    console.log(allBoldItems);
}
getBold_items()
//3
function highlight() {
    for (let i = 0; i < 6; i++) {
        let strng1 = document.getElementsByTagName('strong')[i].innerText
        document.getElementsByTagName('strong')[i].style.color = 'blue'
    }
}
highlight()

//4
function return_normal() {
    for (let i = 0; i < 6; i++) {
        let strng2 = document.getElementsByTagName('strong')[i].innerText
        document.getElementsByTagName('strong')[i].style.color = 'black'
    }
}

return_normal()

//5
function ex5() {
    let pr = document.getElementsByTagName('p')[0].addEventListener('mouseover', highlight)
    function highlight() {
        for (let i = 0; i < 6; i++) {
            let strng1 = document.getElementsByTagName('strong')[i].innerText
            document.getElementsByTagName('strong')[i].style.color = 'blue'
        }
    }
    
    pr = document.getElementsByTagName('p')[0].addEventListener('mouseout', return_normal)
    function return_normal() {
        for (let i = 0; i < 6; i++) {
            let strng2 = document.getElementsByTagName('strong')[i].innerText
            document.getElementsByTagName('strong')[i].style.color = 'black'
        }
    }
    
}
ex5()







// 🌟 Exercice 4 : Volume Of A Sphere
// Instructions
// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:
let form = document.forms[0]
let btn = document.getElementById('submit')
let vol = document.getElementById('volume')
let volume
btn.addEventListener('click', function(event) {
    event.preventDefault()
    let radius = document.getElementById('radius').value
    if (!isNaN(radius) && radius > 0) {
        let pow = Math.pow (radius, 3)
        volume = (4 * Math.PI * pow) / 3 
        console.log(volume);
        vol.value = volume
    }
})





// Exercise 5 : Event Listeners
// Instructions
// Add many events listeners to one element on your webpage. Use the click, mouseover, mouseout and dblclick events.
// Each listener should do a different thing, for instance - change position x, change position y, change color, change the font size… and more.
let prgrph = document.getElementsByTagName('p')[0].addEventListener('click', clickPrgrph)
function clickPrgrph() {
    document.getElementsByTagName('p')[0].style.fontSize = '60px'
}
 prgrph = document.getElementsByTagName('p')[0].addEventListener('mouseover', mouseoverPrgrph)
 function mouseoverPrgrph() {
    document.getElementsByTagName('p')[0].style.color = 'lightblue'

}
 prgrph = document.getElementsByTagName('p')[0].addEventListener('mouseout', mouseoutPrgrph)
 function mouseoutPrgrph() {
    document.getElementsByTagName('p')[0].style.color = 'black'
}
 prgrph = document.getElementsByTagName('p')[0].addEventListener('dblclick', dblclickPrgrph)
 function dblclickPrgrph() {
    document.getElementsByTagName('p')[0].style.display = 'none'
}




// 🌟 Exercice 4 : Volume Of A Sphere
// Instructions
// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base: