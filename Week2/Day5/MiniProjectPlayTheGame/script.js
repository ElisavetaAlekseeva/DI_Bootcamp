
// Exercise 1 : Play A Guessing Game
// Instructions
// Create a new folder on your computer.
// Clone or Download the index.html and style.css files from this github link.
// Follow the steps written below
// Steps
// Explanation of the game : the point of the game is to guess the number that the computer has in “mind”.
// First Part
// Create a JS file and link it to the index.html file.
// Take a look at your html file, you should have a button with an “onclick” event. This event is equal to the function playTheGame(). It means that when you will click on the button, the function playTheGame() will be called. 
// We will learn more about events next week ;)
// Now let’s create the function:
// In the JS file, create a function called playTheGame() that takes no parameter.
// In the function, start by asking the user if they would like to play the game (Hint: use the built-in confirm() function).
// If the answer is false, alert “No problem, Goodbye”.
// If his answer is true, follow these steps:
// Ask the user to enter a number between 0 and 10 (Hint: use the built-in prompt() function). You then have to check the validity of the user’s number :
// If the user didn’t enter a number (ie. if he entered another data type) alert “Sorry Not a number, Goodbye”.
// If the user didn’t enter a number between 0 and 10 alert “Sorry it’s not a good number, Goodbye”.
// Else (ie. he entered a number between 0 and 10), create a variable named computerNumber where the value is a random number between 0 and 10 (Hint: Use the built-in Math.random() function). Make sure that the number is rounded.



function playTheGame() {
    let user = confirm('Press "ok" if you would like to play the game');
    if (user == true){
        var userNumber = prompt('enter a number between 0 and 10');
        checkNumber(userNumber);
    } else {
        alert ('No problem, Goodby');
    }
}

function  checkNumber(userNumber) {
    if (isNaN(userNumber) == true) {
        alert ('Sorry Not a number, Goodbye');
        return;
    } else if (10 < userNumber || userNumber < 0) {
        alert ('Sorry it’s not a good number, Goodbye');
        return;
    } else if (0 <= userNumber && userNumber <= 10) {
        var computerNumber = Math.trunc(Math.random()*10);
        console.log(computerNumber);
        compareNumbers(userNumber,computerNumber);
    }
}

function compareNumbers(userNumber,computerNumber)  {
    let chances = 1
    do {
        if (userNumber == computerNumber){
            alert ('WINNER!');
            return;
        } else if (userNumber > computerNumber){
            userNumber =  Number(prompt('Your number is bigger then the computer’s, guess again!'));
        } else if (userNumber < computerNumber){
            userNumber =  Number(prompt('Your number is smaller then the computer’s, guess again!'));
        }
        chances++
    } while (chances < 3)
    alert('Out of chances! Sorry');
}

playTheGame();
