// Exercise 1 : Is_Blank
// Instructions
// Write a program to check whether a string is blank or not.
// console.log(isBlank('')); --> true
// console.log(isBlank('abc')); --> false

function Is_Blank(string) {
    if (string === '') {
        console.log('true');
    } else{
        console.log('false');
    }
}
let str = prompt('enter sting');
Is_Blank(str);



// Exercise 2 : Abbrev_name
// Instructions
// Write a JavaScript function to convert a string into an abbreviated form.
// console.log(abbrevName("Robin Singh")); --> "Robin S."
let usersName = prompt('Enter your name and surname').split(' ');
function abbrevName(fullNameArray) {
    let firstName = fullNameArray[0];
    let surnameArray = fullNameArray[1].split('');
    var firstLetter = surnameArray[0];
    var fullAbbrevName = firstName + ' ' + firstLetter + '.';
    return fullAbbrevName;
}
console.log(abbrevName(usersName));


// ????? spaces?
// Exercise 3 : SwapCase
// Instructions
// Write a JavaScript function which takes a string as an argument and swaps the case of each character. 
// For example :
// if you input 'The Quick Brown Fox' 
// the output should be 'tHE qUICK bROWN fOX'.

function checkCase(str) {
    let stringArray = str.split(' ');
    var fullString = '';
    var fullWord = '';
    for (let i = 0; i < stringArray.length; i++) {
      let wordArray = stringArray[i].split('');
      for (let k = 0; k < wordArray.length; k++) {
          var letter = wordArray[k];
          if (letter == letter.toUpperCase()) {
                fullWord = letter.toLowerCase();
          } else {
                fullWord = letter.toUpperCase();
          }
          fullString += fullWord;
      }
      fullString += ' ';
    }
    console.log(fullString);
}

console.log(checkCase('The Quick Brown Fox'));




// Exercise 4 : Omnipresent Value
// Instructions
// Create a function that determines whether an argument is omnipresent for a given array.
// A value is omnipresent if it exists in every subarray inside the main array.
// To illustrate:
// [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
// // 3 exists in every element inside this array, so is omnipresent.
// Examples
// isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ true
// isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ false
function isOmnipresent(array, val) {
    for (let i = 0; i < array.length; i++) {
        let a = array[i];
        if (!a.includes(val)) {
            return false;
        }
    } return true;
}


 console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1));