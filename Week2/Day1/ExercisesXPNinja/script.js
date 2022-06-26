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
let person = prompt('enter a string of numbers separated by commas, please');
let sumPerson = person.trim();
let sumPerson1 = sumPerson.replace(/,/g, '+');
typeof(sumPerson1) == Number;
let a = sumPerson1;


