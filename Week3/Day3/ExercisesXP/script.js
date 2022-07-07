// 🌟 Exercise 1: Timer
// Instructions
// Using this HTML code:
// <!DOCTYPE html>
//     <html>
//     <head>
//         <style>
//         p {
//           background: yellow;
//           color: red;
//         }
//         </style>
//     </head>
//     <body>
//         <div id="container"></div>
//         <button id="clear">Clear Interval</button>
//     </body>
//     </html>
// Part I
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.

// let button = document.getElementById('clear')
// button.addEventListener('click',greating())
// function greating() {
//     let helloWorld = setTimeout(function() {
//         alert('Hello World')
//     }, 3000)
// }

// // Part II
// // In your Javascript file, using setTimeout, call a function after 2 seconds.
// // The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// let button = document.getElementById('clear')
// button.addEventListener('click',greating())
// function greating() {
//     let helloWorld = setTimeout(function() {
//         let paragraph = document.createElement('p')
//         let div = document.getElementById('container')
//         paragraph.innerText = 'Hello World'
//         div.appendChild(paragraph)
//     }, 3000)
// }



// // Part III
// // In your Javascript file, using setInterval, call a function every 2 seconds.
// // The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// // The interval will be cleared (ie. clearInterval), when the user will click on the button.
// // Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.


// let interval = setInterval(function() {
//     let paragraph = document.createElement('p')
//     let div = document.getElementById('container')
//     paragraph.innerText = 'Hello World'
//     div.appendChild(paragraph)
// }, 3000)

// let btn = document.getElementById('clear')
// btn.addEventListener('click', function() {
//     clearInterval(interval)
// })


// let sum = 0
//     let interval = setInterval(function() {
//         let paragraph = document.createElement('p')
//         let div = document.getElementById('container')
//         paragraph.innerText = 'Hello World'
//         div.appendChild(paragraph)
//         sum++
//         if (sum >= 5) {
//             clearInterval(interval)
//         }
//     }, 3000)

   


// // 🌟 Exercise 2 : Move The Box
// // Instructions
// // <!DOCTYPE html>
// //     <html>
// //     <head>
// //         <style>
// //         #container {
// //           width: 400px;
// //           height: 400px;
// //           position: relative;
// //           background: yellow;
// //         }
// //         #animate {
// //           width: 50px;
// //           height: 50px;
// //           position: absolute;
// //           background-color: red;
// //         }
// //         </style>
// //     </head>
// //     <body>
// //         <p><button onclick="myMove()">Click Me</button></p>
// //         <div id="container">
// //           <div id="animate"></div>
// //         </div>
// //     </body>
// //     </html>
// // Copy the code above, to a structured HTML file.
// // In your Javascript file, use setInterval to move the <div id="animate"> to the right side of the <div id="container">, when the button is clicked on.
// // The <div id="animate"> should move 1px to the right every milisecond, until it reaches the end of the <div id="container">.
// // Hint : use clearInterval as soon as the box reaches the right end side of the container
// // Hint : check out the demonstration in the Course Noted named JS Functions
// let btn = document.getElementsByTagName('button')[0]
// btn.addEventListener('click', myMove)
// function myMove() {
// let position = 0 
// let animateDiv = document.getElementById('animate')
// let interval = setInterval (function() {
//     if (position == 350){
//         clearInterval(interval)
//     } else {
//         position++
//         animateDiv.style.left = position + 'px'
//     }
// },5)
// }



// // 🌟 Exercise 3: Drag & Drop
// // Instructions
// // <!DOCTYPE html>
// //     <html>
// //     <head>
// //         <style>
// //         #target {
// //           width: 200px;
// //           height: 200px;
// //           position: relative;
// //           background: yellow;
// //         }
// //         #box {
// //           width: 50px;
// //           height: 50px;
// //           position: absolute;
// //           background-color: red;
// //         }
// //         </style>
// //     </head>
// //     <body>
// //         <div id="target"></div>
// //         <br>
// //         <div id="box"></div>
// //     </body>
// //     </html>
// // Copy the code above, to a structured HTML file.
// // In your Javascript file add the functionality which will allow you to drag the box and drop it into the target. Check out the Course Notes named DOM animations.

let box = document.getElementById('box')
let target = document.getElementById('target')

target.ondragover = allowDrop
function allowDrop(event) {
    event.preventDefault()
}

box.ondragstart = drag
function drag(event) {
    event.dataTransfer.setData('id', event.target.id)
}

target.ondrop = drop
function drop(event) {
    let itemId = event.dataTransfer.getData('id')
    console.log(itemId);
    event.target.append(document.getElementById(itemId))
}

