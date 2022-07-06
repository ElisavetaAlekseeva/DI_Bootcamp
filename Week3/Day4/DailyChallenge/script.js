let listTasks = []
let btn = document.getElementsByTagName('button')[0]
let divListTasks = document.getElementsByClassName('listTasks')[0]



function addTask() {
    btn.addEventListener('click', function(event) {
    let usersText = document.getElementsByTagName('input')[0]
        event.preventDefault()
        if (usersText.value.length > 0){
            listTasks.push(usersText.value)
            let div = document.createElement('div')
            let span = document.createElement('span')
            span.textContent = usersText.value

            let checkBoxbtn = document.createElement('input')
            checkBoxbtn.setAttribute('type', 'checkbox')
            let btnX = document.createElement('button')
            let icon = document.createElement('i')
            icon.setAttribute('class','fa-regular fa-circle-xmark')
            btnX.style.border = 'none'
            btnX.style.backgroundColor = 'inherit'
            btnX.appendChild(icon)
            div.appendChild(btnX)
            div.appendChild(checkBoxbtn)
            div.appendChild(span)

            divListTasks.appendChild(div)
            
                btnX.addEventListener('click',function() {
                    span.style.textDecoration = 'line-through'
                })

        }
        usersText.value = ''

    })
}
addTask()
console.log(listTasks);

