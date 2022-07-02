// Exercise 1: Random Number
// Instructions
// Get a random number between 1 and 100.
// Console.log all even numbers from 0 to the random number.
let randomNumber = Math.floor(Math.random()*100);
console.log(randomNumber);
for (let i = 0; i < randomNumber; i++) {
    if (i % 2 == 0) {
        console.log(i);
    }
}



// Exercise 2: Capitalized Letters
// Instruction
// Create a function that takes a string as an argument.
// Have the function return:
// The string but all letters in even indexes should be capitalized.
// The string but all letters in odd indexes should be capitalized.
// Note:
// Index 0 will be considered even.
// The argument of the function should be a lowercase string with no spaces.
function evenLetter(str) {
    let strArray = str.split('');
    let word = ' ';
    for (let i = 0; i < strArray.length; i++) {
        if (i == 0 || i % 2 == 0) {
            word += strArray[i].toUpperCase();
        } else {
            word += strArray[i].toLowerCase();
        }
    }
    return(word);
}

function oddLetter(str) {
    let strArray2 = str.split('');
    let word2 = ' ';
    for (let k = 0; k < strArray2.length; k++) {
        if (k % 2 != 0) {
            word2 += strArray2[k].toUpperCase();
        } else {
            word2 += strArray2[k].toLowerCase();
        }
    }
    return(word2);
}

function capitalize(str) {
    console.log(evenLetter(str) + ' ' + oddLetter(str));
}

capitalize('abcdef');



// Exercise 3 : Is Palindrome?
// Instructions
// Write a JavaScript function that checks whether a string is a palindrome or not.
// Note A palindrome is a word, phrase or sequence that is spelled the same both backwards and forward, e.g., madam, bob or kayak.

// first solution
function palidrome(str) {
    let array = str.split('');
    let arrayReverse = array.reverse();
    let arrayReverseString = arrayReverse.join('');
    if (arrayReverseString == str){
        console.log('it is a palidrome');
    } else {
        console.log('it is not a palidrome');
    }
}
palidrome('madam');

// second solution
function isPalindrome(str) {
    let array = str.split('');
    let isPalindrome = true
    for (let i = 0; i < array.length / 2; i++) {
        if (array[i] !=  array[array.length - 1 - i]) {
            isPalindrome = false}
        }
    
        return isPalindrome;
}
console.log(isPalindrome('madam'));



// Exercise 4 : Biggest Number
// Instructions
// Create a function called biggestNumberInArray(arrayNumber) that takes an array as a parameter and returns the biggest number.
// Note : This function should work with any array;
function biggestNumberInArray(arrayNumber){
    let a;
    for (let i = 0; i < arrayNumber.length; i++) {
        for (let k = 1; k < arrayNumber.length; k++) {
            if (arrayNumber[i] < arrayNumber[k]) {
                a = arrayNumber[i];
                arrayNumber[i] = arrayNumber[k];
                arrayNumber[k] = a;
            }
        }
        return arrayNumber[0];
    }
}
console.log(biggestNumberInArray([-1,0,3,100, 99, 2, 99]));




// Exercise 5: Unique Elements
// Instructions
// Write a JS function that takes an array and returns a new array with only unique elements.
function unique(value, index, self) {
    return self.indexOf(value) === index;
}
const numbers = [1, 5, 4, 2, 3, 4, 5, 5];
const uniqueNumbers = numbers.filter(unique);
console.log(uniqueNumbers);