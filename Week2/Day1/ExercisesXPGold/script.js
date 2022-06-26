// Exercise 1 : Favorite Color
let sentence = ["my","favorite","color","is","blue"];
console.log(sentence.join(' '));


// Exercise 2 : Mixup
let str1 = "mix";
let str2 = "pod";
str1 = str1.replace(/mi/i, 'po')
console.log(str1);
str2 = str2.replace(/po/i, 'mi')
console.log(str1, str2);


// Exercise 3 : Calculator

let num1 = prompt('Enter the first number');
let num2 = prompt('Enter the second number');
alert(parseInt(num1) + parseInt(num2));