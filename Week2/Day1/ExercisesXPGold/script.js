// Exercise 1 : Favorite Color
// Write some simple Javascript code that will join all the items in the array above, and console.log the result.
let sentence = ["my","favorite","color","is","blue"];
console.log(sentence.join(' '));


// Exercise 2 : Mixup
// Create 2 variables. The values should be strings. 
// 2. Slice out and swap the first 2 characters of the two strings from part 1.
// 3. Create a third variable where the value is the concatenation of the two strings from the part 1 (separated by a space).
// 4. Finally console.log the new concatenated string.
let str1 = "mix";
let str2 = "pod";
str1 = str1.replace(/mi/i, 'po')
str2 = str2.replace(/po/i, 'mi')
console.log(str1 + " " + str2);


// Exercise 3 : Calculator
// Prompt the user for the first number.
// Store the first number in a variable called num1. 
// Hint : console.log the type of the variable num1. What should you do to convert it to a number ?
// Prompt the user for the second number.
// Store the second number in a variable called num2.
// Create an Alert where the value is the SUM of num1 and num2.
// BONUS: Make a program that can subtract, multiply, and also divide!
let num1 = prompt('Enter the first number');
let num2 = prompt('Enter the second number');
alert(parseInt(num1) + parseInt(num2));