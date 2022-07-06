



let body = document.getElementsByTagName('body')[0]
let inpt = document.createElement('input')
let val = inpt.value 
document.body.appendChild(inpt)

let btn = document.createElement('button')
btn.innerHTML = 'click me'
document.body.appendChild(btn)
btn.addEventListener('click', subFun)
    function subFun (event){
        var inptVal = inpt.value
       console.log(inptVal);
    }

function removeNotLetters(inptVal) {
    let inptValArray = inptVal.split('')
    for (let i = 0; i < inptValArray.length; i++) {
        if (!(64 < inptValArray[i] <  93) || !(96 < inptValArray[i] <  123)){
            inptValArray = i.substring(0, i) + inptValArray.substring(i + 1)
            i--
        }
        console.log(inptValArray);
    }
}