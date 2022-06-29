//  Exercise 1 : List Of People
// Instructions
// Part I - Review About Arrays
// Write code to remove “Greg” from the people array.
// Write code to replace “James” to “Jason”.
// Write code to add your name to the end of the people array.
// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this let people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method
// Write code that gives the index of “Foo”. Why does it return -1 ?
// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?
let people = ["Greg", "Mary", "Devon", "James"];
people.splice(0,1);
people.splice(2, 1, 'Jason');
people.push('Lisa')
console.log(people.indexOf('Mary'));
console.log(people);
console.log(people.indexOf('Foo')); // it will return -1 because Foo does not exist in array people
let last = people[people.length-1];
console.log(last);


for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
}
for (let i = 0; i < people.length; i++) {
    if (people[i] == 'Jason') {
        break;
    }
    console.log(people[i]);
}






//  Exercise 2 : Your Favorite Colors
// Instructions
// Create an array called colors where the value is a list of your five favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus
let colors = ['Blue', 'Red', 'Yellow', 'Orange'];
let a = 0;
for (let i = 0; i < colors.length; i++) {
    a ++;
    console.log('My choice number ' + a + ' is ' + colors[i] );
}



//  Exercise 3 : Repeat The Question
// Instructions
// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)
// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?

let user = Number(prompt('Enter a number'));
if (user < 10) {
    prompt('Enter a new number');
} else {
    alert('ok')
}
// or
do {
    let user = Number(prompt('Enter a new number'));
} while (user < 10);



// Exercise 4 : Building Management
// Review About Objects
// Copy and paste the above object to your Javascript file.
// Console.log the number of floors in the building.
// Console.log how many apartments are on the floors 1 and 3.
// Console.log the name of the second tenant and the number of rooms he has in his apartment. 
// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.
let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}
console.log(building.numberOfFloors);
let a = building.numberOfAptByFloor.firstFloor;
let b = building.numberOfAptByFloor.thirdFloor;
console.log(a+b);
console.log(building.nameOfTenants[1] + ' : ' + building.numberOfRoomsAndRent.dan[0])
let sara = building.numberOfRoomsAndRent.sarah[1];
let david = building.numberOfRoomsAndRent.david[1];
let dan = building.numberOfRoomsAndRent.dan[1];
let sum = sara + david;
if (sum > dan){
    dan = dan + 1200;
}
console.log(dan);



// Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.

let family = {
    father : 'Artem',
    mother : 'Sheila',
    sister : 'Masha'
}
// for( let key in family){
//     console.log(key);
// }
for( let k in family){
    console.log(family[k]);
}



// Exercise 6
// Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”
let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
let str = ''
for (let key in details){
str += key + ' ' + details[key] + ' ';
}
console.log(str);




// Exercise 7 : Secret Group
// Instructions
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”