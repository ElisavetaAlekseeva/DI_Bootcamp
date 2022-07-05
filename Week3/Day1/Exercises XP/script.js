// Exercise 1 : Users
// Instructions
// <div id="container">Users:</div>
// <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
// </ul>
// <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
// </ul>
// Add the code above, to your HTML file
// Using Javascript:
// Retrieve the div and console.log it
// Change the name “Pete” to “Richard”.
// Change each first name of the two <ul>'s to your name.
// Delete the <li> that contains the text node “Sarah”.
// Bonus - Using Javascript:
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.
let div = document.getElementsByTagName('div')
console.log(div);

let john = document.querySelector('.list li')
let pete = john.nextElementSibling
pete.innerHTML = 'Richard'

let myNameFirstUl = document.querySelector('.list li')
console.log(myNameFirstUl.innerText = 'Lisa');
let secondUl = document. getElementsByTagName('ul')[1]
let myNamesecondUl = secondUl.firstElementChild
myNamesecondUl.innerText = 'Lisa'

let secondUlList = document.getElementsByTagName('ul')[1]
let sarah = secondUlList.getElementsByTagName('li')[1].remove() 

let ul = document.getElementsByTagName('ul')
ul[0].classList.add('student_list');
ul[1].classList.add('student_list');

ul[0].classList.add('university', 'attendance')



// 🌟 Exercise 2 : Users And Style
// Instructions
// <div>Users:</div>
// <ul>
//     <li>John</li>
//     <li>Pete</li>
// </ul>
// Add the code above, to your HTML file 
// Add a “light blue” background color and some padding to the <div>.
// Do not display the <li> that contains the text node “John”.
// Add a border to the <li> that contains the text node “Pete”.
// Change the font size of the whole body.
// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).
//2
let  divBG = document.getElementsByTagName('div')[0].style.background = "lightblue"
divBG.style.padding = '20px'
//3
let firstLi = document.getElementsByTagName('li')[0].style.display = 'none'
//4
let secondLi = document.getElementsByTagName('li')[1].style.border = "3px black solid"
//5
let fontSize = document.body.style.fontSize = '30px'





// 🌟 Exercise 3 : Change The Navbar
// Instructions
// <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>
// Add the code above, to your HTML file
// In the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.
// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (<li>).
// Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.
// Bonus
// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). Display the text of each link. (Hint: use the textContent property).
//2
let divChangeId = document.getElementById('navBar').setAttribute('id', 'socialNetworkNavigation')
//3
let newLi = document.createElement('li')
document.getElementsByTagName('ul')[0].appendChild(newLi)

let liTag = document.createTextNode('Logout')
document.getElementsByTagName('ul')[0].lastElementChild.appendChild(liTag)
console.log(liTag);
//4
let firstLi = document.getElementsByTagName('ul')[0].firstElementChild.textContent
let lastLi = document.getElementsByTagName('ul')[0].lastElementChild.textContent
console.log(firstLi + ' ' + lastLi);



// Exercise 4 : My Book List
// Instructions
// Take a look at this link for help.
// The point of this challenge is to display a list of two books on your browser.
// In the body of the HTML page, create an empty div: 
// <div class="listBooks"></div>
// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).
// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)
// Requirements : All the instructions below need to be coded in the js file:
// Using the DOM, render the books inside an HTML table (the HTML table must be added to the <div> created in part 1).
// For each book :
// You have to display the book’s title and the book’s author.
// Example: HarryPotter written by JKRolling.
// The width of the image has to be set to 100px.
// If the book is already read. Set the color of the book’s details to red.

// let allBooks = [
//     {
//         title:'HarryPotter',
//         author:'Rowling',
//         image:'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Harry_Potter_wordmark.svg/1920px-Harry_Potter_wordmark.svg.png'.width='100px',
//         alreadyRead: false
//     }, 
//     {
//         title: '1984',
//         author: 'Orwell',
//         image: 'https://images.gr-assets.com/authors/1588856560p5/3706.jpg'.width='100px',
//         alreadyRead: false
//     }
// ];


//     let tbl = document.createElement('table')
//     document.createElement('table')
//     document.getElementsByTagName('div')[0].appendChild(tbl)
//     tbl.style.width = '100px'
//     tbl.style.height = '100px'
//     tbl.style.border = '3px solid red'

 
//     for (let i = 0; i < allBooks.length; i++) {
//         let cell;
//         for (const key in allBooks[i]){
//             cell.innertext = value;
//         }
//         cell ++
//     }

//     console.log(tbl);


