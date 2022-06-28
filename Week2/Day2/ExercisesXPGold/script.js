// Exercise 1 : The World Translator
// Instructions
// Hint: Use Switch Case
// Ask the user which language they speak.
// Convert the user’s answer to lowercase, so that all the user’s inputs will be accepted in the if statement. For example “english” or “English” or “ENGlish” ect…”
// Create a few conditions 
// If the user speaks French : display “Bonjour”
// If the user speaks English : display “Hello”
// If the user speaks Hebrew : display “Shalom”
// If the user doesn’t speak any of these 3 languages: display ‘01110011 01101111 01110010 01110010 01111001’

let lang = prompt('enter a language you speak').toLowerCase();
console.log(lang);

switch (lang) {
    case 'french':
        alert('Bonjour');
        break;
    case 'english':
        alert('Hello');
        break;
    case 'hebrew':
        alert('Shalom');
        break;
    default:
        alert('01110011 01101111 01110010 01110010 01111001');
        break;
}


// Exercise 2 : The Grade Assigner
// Instructions
// Ask the user for their grade.
// If the grade is bigger than 90, console.log “A”
// If the grade is between 80 and 90 (included), console.log “B”
// If the grade is between 70(included) and 80 (included), console.log “C”
// If the grade is lower than 70, console.log “D”

let user = prompt('Enter your grade from 0-100');
 if (user > 90) {
     console.log('A');
 } else if (user > 80 & user <= 90) {
    console.log('B');
 }  else if (user >= 70 & user <= 80) {
    console.log('C');
 }   else if (user < 70 ) {
    console.log('D');
 }



 // Exercise 3 : Verbing
// Instructions
// Prompt the user for a string. It must be a verb.
// If the length of the string is at least 3 and the string doesn’t end with “ing”, add ‘ing’ to the end of the string.
// If the length of the string is at least 3 and the string ends with “ing” add “ly” to it’s end.
// If the length of the string is less than 3, leave it unchanged.
let verb = prompt('enter a verb');
if (verb.length >= 3 & verb.endsWith('ing') == false) {
    console.log(verb + 'ing');
} else if (verb.length >= 3 & verb.endsWith('ing') == true) {
    console.log(verb + 'ly');
} else  if(verb.length <= 3 ) {
    console.log(verb);
}

