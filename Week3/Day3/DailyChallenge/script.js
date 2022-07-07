



let body = document.getElementsByTagName('body')[0]
let inpt = document.createElement('input')
document.body.appendChild(inpt)

// let btn = document.createElement('button')
// btn.innerHTML = 'click me'
// document.body.appendChild(btn)
// btn.addEventListener('click', subFun)
// function subFun (event){
//     let inptVal = inpt.value
//     let newStr = inptVal.replace(/[^a-zA-Z]/g,"")
//     console.log(newStr);
// }

inpt.addEventListener('keyup',function(e) {
    this.value = this.value.replace(/[^a-zA-Z]/g,"")
})

