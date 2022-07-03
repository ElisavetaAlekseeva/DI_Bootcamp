// What We Will Learn:
// Variables
// Conditionnals
// Loops
// Functions
// Make A Complete Calculator In Javascript.
// Introduction:
// Today we will be creating a fully functional calculator. In order to do this, we must have our HTML and Javascript files interact with each other. 
// We will be using Javascript to dynamically calculate the outcome of the buttons that were clicked on the HTML. 
// We will be adding an attribute called onclick to each button. The onclick attribute allows us to call a function from our Javascript file when the button is clicked.
// For example, if you click on the number 2 on the calculator (ie. seen below in the assets), the function number(2) will be called. The argument is the value of the button.
// Use HTML CSS for the visual.
// Instructions:
// Create a HTML file for your calculator and a JS file for the calculator’s functionality.
// You must create 3 functions in the js file:
// number(num)
// operator(operator)
// equal()
// Hint : you can use the eval() method to help with your calculations.
// Before coding, take your time to understand all the parts to the exercise and their process. You can write it down somewhere if it helps (recommended).
// Bonus : create the RESET and CLEAR buttons.
let firstNumber = '0';
let secondNumber = '0';
let isWithOperator = false;
let typeOfOperator = undefined;
let result = undefined;

function number(number) {
    if (firstNumber != '0' && !isWithOperator) {
        firstNumber += number;
        document.getElementById('number').innerHTML = firstNumber;
    } else if (!isWithOperator) {
        firstNumber = String(number);
        document.getElementById('number').innerHTML = firstNumber;
    } else if (secondNumber != '0') {
        secondNumber += number;
        document.getElementById('number').innerHTML = secondNumber;
    } else {
        secondNumber = String(number);
        document.getElementById('number').innerHTML = secondNumber;
    }
    
}

function operator(operator) {
    if (operator == '+') {
        isWithOperator = true;
        typeOfOperator = '+';
    } else if (operator == '-') {
        isWithOperator = true;
        typeOfOperator = '-';
    } else if (operator == '*') {
        isWithOperator = true;
        typeOfOperator = '*';
    } else if (operator == '/') {
        isWithOperator = true;
        typeOfOperator = '/';
    }
}

function equal() {
    if (typeOfOperator == '+') {
        result = Number(firstNumber) + Number(secondNumber);
        document.getElementById('number').innerHTML = result;
    } else if (typeOfOperator == '-') {
        result = Number(firstNumber) - Number(secondNumber);
        document.getElementById('number').innerHTML = result;
    } else if (typeOfOperator == '*') {
        result = Number(firstNumber) * Number(secondNumber);
        document.getElementById('number').innerHTML = result;
    } else if (typeOfOperator == '/') {
        result = Number(firstNumber) / Number(secondNumber);
        document.getElementById('number').innerHTML = result;
    } 
} 

function cl() {
    firstNumber = '0';
    secondNumber = '0';
    isWithOperator = false;
    typeOfOperator = undefined;
    result = undefined;
    document.getElementById('number').innerHTML = firstNumber;
}
