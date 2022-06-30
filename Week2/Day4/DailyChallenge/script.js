
function getMaxLength(arr) {
    let maxLenght = 0
    for(let i = 0; i < arr.length; i++) {
       if (arr[i].length > maxLenght) {
          maxLenght = arr[i].length
       }
    }
    return maxLenght
 }
 
 function addSpaces(str, number) {
    for (let i = 0; i < number; i++) {
       str += ' '
    }
    return str   
 }
 
 function printBoarder(number) {
    str = ''
    for (let i = 0; i < number; i++) {
       str += '*'
    }
    return str
 }
 
 
 function ThisIsFunction(str) {
    let array = str.split(', ')
    const maxLength = getMaxLength(array) * 2
    for (let i = 0; i < array.length; i++) {
       if (array[i].length < maxLength) {
          array[i] = addSpaces(array[i], maxLength - array[i].length)
       }
       array[i] = "*" + array[i] + "*"
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