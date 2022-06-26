// Exercise 1: Your Favorite Food
// Store your favorite food into a variable.
// Store your favorite meal of the day into a variable (ie. breakfast, lunch or dinner)
// Console.log I eat <favorite food> at every <favorite meal>
let favFood = 'ice cream';
let favMeal = 'dinner';
console.log('I eat' + ' ' + favFood + ' ' + 'at every' + ' ' + favMeal);


// Exercise 2 : Series
// Using this array : let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
// Create a variable named myWatchedSeriesLength that is equal to the number of series in the myWatchedSeries array.
// Create a variable named myWatchedSeriesSentence, that is equal to a sentence describing the series you watched
// For example : black mirror, money heist, and the big bang theory
// Console.log a sentence using both of the variables created above
// For example : I watched 3 series : black mirror, money heist, and the big bang theory
// Change the series “the big bang theory” to “friends”. Hint : You will need to use the index of “the big bang theory” series.
// Add, at the end of the array, the name of another series you watched.
// Add, at the beginning of the array, the name of your favorite series.
// Delete the series “black mirror”.
// Console.log the third letter of the series “money heist”.
// Finally, console.log the myWatchedSeries array, to see all the modifications you’ve made.
let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength =  myWatchedSeries.length;
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
// Store a celsius temperature into a variable.
// Convert it to fahrenheit and console.log <temperature>°C is <temperature>°F.
// Hint : Should you create another variable to hold the temperature in fahrenheit? (ie. point 2)
// Hint: To convert a temperature from celsius to fahrenheit : Divide it by 5, then multiply it by 9, then add 32
let celsius = 25;
let fahrenheit = ( celsius / 5 ) * 9 + 32;
console.log(fahrenheit);




// Exercise 4 : Guess The Answers #1
// For each expression, predict what you think the output will be in a comment (//) without first running the command. 
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.
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

// Exercise 6 : Guess The Answers #3
console.log(5 + "34");
// Prediction: 534 not two numbers
// Actual:534

console.log(5 - "4");
// Prediction: 1 we use - only for subtractions, so 4 counts as a number
// Actual:1

console.log(10 % 5);
// Prediction: 0 because 10/5 = 2 without any residues
// Actual:0

console.log(5 % 10);
// Prediction: 5 
// Actual:5

console.log("Java" + "Script");
// Prediction: JavaScript its two strings without space
// Actual:JavaScript

console.log(" " + " ");
// Prediction:'  '. just space without any variables
// Actual:'  '

console.log(" " + 0);
// Prediction:' 0' - space and the number
// Actual:' 0'

console.log(true + true);
// Prediction: 2 true = 1 => 1 + 1 =2
// Actual:2

console.log(true + false);
// Prediction: 1 true=1, false=0
// Actual:1

console.log(false + true);
// Prediction: 1 true=1, false=0
// Actual:1

console.log(false - true);
// Prediction: -1 true=1, false=0
// Actual:-1

console.log(!true);
// Prediction: false ! its a logical negation
// Actual:false 1

console.log(3 - 4);
// Prediction: -1 
// Actual:-1

console.log("Bob" - "bill");
// Prediction:nan its two strings, not numbers
// Actual:nan

