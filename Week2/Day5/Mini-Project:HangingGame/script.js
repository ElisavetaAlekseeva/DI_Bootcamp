let user1Word = prompt('enter a word.The word must have a minimum of 8 letters.').split('');
let hided = '';
let sum = 0;


for (let i = 0; i < user1Word.length; i++) {
   hided += '*';
}
var hidedArray = hided.split('');

function hangman() {
    let user2Letter = prompt('enter a letter');
    let indexOfLetter = user1Word.indexOf(user2Letter);

    if (indexOfLetter != -1) {
        let temp = user1Word[indexOfLetter];
        user1Word[indexOfLetter] = hidedArray[indexOfLetter];
        hidedArray[indexOfLetter] = temp;
    }
    sum ++
    console.log(hidedArray);
}


do {
    hangman()
} while (sum<4);


