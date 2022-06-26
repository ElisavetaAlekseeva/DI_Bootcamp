// Exercise 1: Your Favorite Food
let favFood = 'ice cream';
let favMeal = 'dinner';
console.log('I eat' + ' ' + favFood + ' ' + 'at every' + ' ' + favMeal);


// Exercise 2 : Series
let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength =  myWatchedSeries.length;
// let myWatchedSeriesSentence = myWatchedSeries.splice(1, 1) + ' and';
let myWatchedSeriesSentence = myWatchedSeries [0]+ ', ' +myWatchedSeries[1]+ ', and ' +myWatchedSeries[2];
console.log(myWatchedSeriesSentence);
console.log('i watched' + ' ' + myWatchedSeriesLength + ' ' + 'series:' + ' ' + myWatchedSeriesSentence);

myWatchedSeries[2] = 'friends';
myWatchedSeries.push('Simpsons');
myWatchedSeries.unshift('Bridgerton');
myWatchedSeries.splice(1,1);
console.log(myWatchedSeries[1] [2]);
console.log(myWatchedSeries);


// Exercise 3 : The Temperature Converter
let celsius = 25;
let fahrenheit = ( celsius / 5 ) * 9 + 32;
console.log(fahrenheit);




// Exercise 4 : Guess The Answers #1
let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction: it will output 55, because A and B are variables that include numbers
// Actual: 55

a = 2;

console.log(a+b) //second expression
// Prediction: it will output 23, becasue A isnt a constanta and we can change its value and after that use a new value
// Actual:23

// What will be the outcome of a + b in the first expression ? 55
// What will be the outcome of a + b in the second expression ? 23
// What is the value of c? undefined

console.log(3 + 4 + '5');
// Prediction: 75 because 3 and 4 are nubers and we can sum them. but '5' ia a string, so we cant do with it any math manipulation
// Actual: 75




// Exercise 5 : Guess The Answers #2
console.log(typeof(15));
// Prediction: number. its a number. it hasnt quotes
// Actual: number

console.log(typeof(5.5));
// Prediction: number its still a number. it hasnt quotes
// Actual: number

console.log(typeof(NaN));
// Prediction: number nan = mot a number, but it has type of number
// Actual: number

console.log(typeof("hello"));
// Prediction: string because its in quotes
// Actual:string

console.log(typeof(true));
// Prediction: boolean 
// Actual:boolean

console.log(typeof(1 != 2));
// Prediction: boolean because there is a comparison
// Actual: boolean

console.log("hamburger" + "s");
// Prediction: hamburgers combining two lines 
// Actual: hamburgers

console.log("hamburgers" - "s");
// Prediction: --
// Actual: nan

console.log("1" + "3");
// Prediction: 13  two strings, not numbers
// Actual: 13

console.log("1" - "3");
// Prediction: nan
// Actual: -2   

console.log("johnny" + 5);
// Prediction: johnny5 we cant sum a string a a number
// Actual:nan

console.log("johnny" - 5);
// Prediction: nan we cant subtract a string a a number
// Actual:nan

console.log(99 * "hello");
// Prediction: nan we cant multiply a string a a number
// Actual:nan

console.log(1 != 1);
// Prediction: false because 1 = 1 - its true. and here != that means 1 not equal 1 
// Actual:false

console.log(1 == "1");
// Prediction: true here isnt strictly equal
// Actual:true

console.log(1 === "1");
// Prediction: false strictly equal and here compare string and number
// Actual:false

console.log(6666);

// Exercise 6 : Guess The Answers #3
console.log(5 + "34");
// Prediction: 534 not two numbers
// Actual:

console.log(5 - "4");
// Prediction: 1
// Actual:

console.log(10 % 5);
// Prediction: 2 ???????
// Actual:

console.log(5 % 10);
// Prediction: 0.5 ????????
// Actual:

console.log("Java" + "Script");
// Prediction: JavaScript
// Actual:

console.log(" " + " ");
// Prediction:'  '. 
// Actual:

console.log(" " + 0);
// Prediction:' 0'
// Actual:

console.log(true + true);
// Prediction: 2
// Actual:

console.log(true + false);
// Prediction: 1
// Actual:

console.log(false + true);
// Prediction: 1
// Actual:

console.log(false - true);
// Prediction: -1
// Actual:

console.log(!true);
// Prediction: false
// Actual:

console.log(3 - 4);
// Prediction: -1
// Actual:

console.log("Bob" - "bill");
// Prediction:nan
// Actual:

