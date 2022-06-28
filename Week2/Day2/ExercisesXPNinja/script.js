// Exercise 1 : Age Difference
// Instruction
// Given the years two people were born, find the date when the younger one is exactly half the age of the older.
// Notes: The dates are given in the format YYYY

let user1 = prompt('Enter your birth year');
let user2 = prompt('Enter your birth year');
let age1 = user1 + (user2 - user1);
let age2 = user2 + (user1 - user2);
if (user > user2){
    alert(age2);
} else if (user < user2){
    alert(age1);
}




// Exercise 2 : Zip Codes
// Instruction
// Harder exercise
// Hint : This exercise has 2 parts. First, do this exercise without Regular Expressions, then do it using Regular Expressions
// While working in a Post Office you must have the clients’ zip code in order to send them their letters.
// Ask the client for their zip code and console.log “success” or “error” based on the following rules.
// Zip codes consists of 5 numbers
// Must only contain numbers
// Must not contain any whitespace (spaces)
// Must not be greater than 5 digits in length

// 1
let client1 = prompt('enter your zip code');
let lngth = client1.toString().length;

if (client1.indexOf(' ') < 0 && lngth < 6 && !(isNaN(client1))){
    console.log('ok');
} else{
    console.log('error');
}



//2
// let client = Number(prompt('enter your zip code'));
// let order = /^d.+{0,5}.+\S.$/;
// if (client == order){
//     console.log('success');
// } else {
//     console.log('error');
// }
// 5 numbers
// only numbers  /^d+$/
// without space /^\S+$/
// max 5 numbers {0,5}$/







// Exercise 3 : Secret Word
// Instruction
// Harder exercise
// Hint : Use Regular Expressions
// Prompt the user for a word and save it to a variable.
// Delete all the vowels of the word and console.log the result.
// Bonus: Replace the vowels with another character and console.log the result
let user = prompt('Enter a word');
let a =  user.replace(/[aA]/g, 1).replace(/[eE]/g, 2).replace(/[iI]/g, 3).replace(/[oO]/g, 4).replace(/[uU]/g, 5);
console.log(a);
