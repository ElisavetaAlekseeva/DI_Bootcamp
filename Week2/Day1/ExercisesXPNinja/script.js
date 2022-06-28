// Exercise 1 : Evaluation

console.log(5 >= 1);
// Prediction: true
 // Actual:true

console.log(0 === 1);
// Prediction:false
// Actual:false

console.log(4 <= 1);
// Prediction: false
// Actual:false

console.log(1 != 1);
// Prediction: false
// Actual:false

console.log("A" > "B");
// Prediction: false
// Actual:false

console.log("B" < "C");
// Prediction:true
// Actual:true

console.log("a" > "A");
// Prediction: true
// Actual:true

console.log("b" < "A");
// Prediction: false
 // Actual:false

console.log(true === false);
// Prediction:false
// Actual:false

console.log(true != true);
// Prediction: true   false????
// Actual:false



// Exercise 2 : Ask For Numbers
// Ask the user for a string of numbers separated by commas
// Console.log the sum of the numbers.
// Hint: use some string methods
let person = prompt('enter a string of numbers separated by commas, please');
let sumPerson = person.trim().split(",");
// const result = sumPerson.reduce((a, b) => Number(a) + Number(b), 0);
let result = 0
for (let i = 0; i < sumPerson.length; i++) {
    result += Number(sumPerson[i]);
};
console.log(result);



// Exercise 3 : Find Nemo
// Instructions
// Hint: if statement (tomorrow’s lesson)
// Ask the user to give you a sentence containing the word “Nemo”. For example "I love the movie named Nemo"
// Find the word “Nemo”
// Console.log a string as follows: "I found Nemo at [the position of the word Nemo]".
// If you can’t find Nemo, console.log “I can’t find Nemo”.

let a = prompt('enter a sentence containing the word “Nemo”');
    // b = a.indexOf('Nemo');
    // alert("I found Nemo at" + " " + b);
let b = a.split(" ");
let find = false;
for (let k = 0; k < b.length; k++){
    if (b[k].trim() === "Nemo"){
        alert("I found Nemo at" + " " + k);
        find = true;
    } 
}
if(!find){
    alert('~Nemo not found')
}






// Exercise 4 : Boom
// Instructions
// Hint: if statement (tomorrow’s lesson)
// Prompt the user for a number. Depending on the users number you will return a string of the word “Boom”. Follow the rules below:
// If the number given is less than 2 : return “boom
// If the number given is bigger than 2 : the string should include n number of “o”s (n being the number given)
// If the number given is evenly divisible by 2, add a exclamation mark to the end.
// If the number given is evenly divisible by 5, return the string in ALL CAPS.
// If the number given is evenly divisible by both 2 and 5, return the string in ALL CAPS and add an exclamation mark to the end.

let user = Number(prompt('enter a number'));
let str = '';
if (user < 2) {
    str = 'boom'
} else {
    for (let i = 0; i < user; i++) {
        str += 'o' 
    }
}  
if (user % 2 == 0){
    str += '!';
}  
if(user % 5 == 0){
    str = str.toUpperCase();
}

alert(str);
