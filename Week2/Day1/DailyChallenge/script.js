// Exercise 1

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];


// Remove Banana from the array.
// Sort the array in alphabetical order.
// Add “Kiwi” to the end of the array.
// Remove “Apples” from the array. Don’t use the same method as in part 1.
// Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
// 1
let a = fruits.shift();
console.log(a);
console.log(fruits);

// 2
console.log(fruits.sort());

// 3
fruits.push("Kiwi");
console.log(fruits);

// 4
let b = fruits.splice(0,1);
console.log(a);
console.log(fruits);

// 5
console.log(fruits.reverse());




// Exercise 2
// Access and then console.log “Oranges”
let moreFruits = ["Banana", 
    [
    "Apples", 
        ["Oranges"],
     "Blueberries"
    ]
];

let c = moreFruits[1][1][0];
console.log(c);