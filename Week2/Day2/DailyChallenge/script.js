// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”. 
// For example, “The movie is not that bad, I like it”.
// Create a variable called wordNot where it’s value is the first appearance (ie. the position) of the substring “not” (from the sentence variable).
// Create a variable called wordBad where it’s value is the first appearance (ie. the position) of the substring “bad” (from the sentence variable).
// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result. 
// For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.

let sentence = prompt('enter a string that contains the words “not” and “bad”');
let wordNot = sentence.indexOf('not');
let wordBad = sentence.indexOf('bad');
let str = sentence.substring(wordNot, wordBad+3);
let str1 = sentence.substring(0, wordNot+3);
let str2 = sentence.substring(wordBad, sentence.length);
let str3 = sentence.substring(wordNot+3, wordBad);


if (wordNot < 0){
    console.log(sentence);
} else if (wordBad > wordNot & str.length <= 7){
    console.log(sentence.replaceAll('not bad', 'good'));
} else if (wordBad > wordNot & str.length > 7){
    console.log(sentence.replaceAll(str, 'good')); 
} 