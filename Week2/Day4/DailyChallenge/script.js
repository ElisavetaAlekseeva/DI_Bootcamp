
function getMaxLength(arr) {
    let maxLenght = 0;
    for(let i = 0; i < arr.length; i++) {
       if (arr[i].length > maxLenght) {
          maxLenght = arr[i].length;
       }
    }
    return maxLenght;
 }
 function addSpaces(str, number) {
    for (let i = 0; i < number; i++) {
       str += ' ';
    }
    return str   
 }
 function printBoarder(number) {
    str = ''
    for (let i = 0; i < number; i++) {
       str += '*';
    }
    return str
 }
 function ThisIsFunction(str) {
    let array = str.split(', ');
    const maxLength = getMaxLength(array) * 2;
    for (let i = 0; i < array.length; i++) {
       if (array[i].length < maxLength) {
          array[i] = addSpaces(array[i], maxLength - array[i].length);
       }
       array[i] = "*" + array[i] + "*";
    }
    let resultString = ''
    resultString += printBoarder(maxLength) + '\n'
    for (let i = 0; i < array.length; i++) {
       resultString += array[i] + '\n';
    }
    resultString += printBoarder(maxLength) + '\n'
    console.log(resultString);
 }
  ThisIsFunction('Hello, World, in, a, frame');


//Ziv's solution
//   let words = ["Hello", "World", "in", "a", "frame"];

// function longestWordLength(arr) {
//   let len = arr[0].length;
//   for (let i = 1; i < words.length; i++) {
//       if(arr[i].length > len){
//         len = arr[i].length;
//       }
//   }
//   return len;
// }

// function addSpaces(word,len){
//   if(word.length == len){
//     return "";
//   }
//   return " ".repeat(len-word.length);
// }

// function stars () {
//   let len = longestWordLength(words);
//   console.log("*".repeat(len+4));
//   for(x in words){
//     console.log('* ' + words[x] + addSpaces(words[x],len) + ' *');
//   }
//   console.log("*".repeat(len+4));
// }
// stars();