let color_col = 3
let color_row = 8
let color_count = color_col * color_row

let main_col = 60
let main_rows = 50
let main_count = main_col * main_rows

let clicked = true

let btn = document.getElementById('clear')

let sidebar = document.getElementById('left-side')
let main = document.getElementById('canvas')
let divsStyleColor;
let mousedown = false;

document.body.addEventListener('mousedown',function(){
    mousedown = true
})
document.body.addEventListener('mouseup',function(){
    mousedown = false
})

for (let i = 0; i < color_count; i++) {
    let div = document.createElement('div')
    div.style.backgroundColor = generateRandomColor()
    // div.className = 'color'
    div.addEventListener('click', function(event){
        divsStyleColor = div.style.backgroundColor
        console.log(divsStyleColor);
   })

    sidebar.appendChild(div)
}

for (let i = 0; i < main_count; i++) {
    let div = document.createElement('div')
    // div.className = 'cell'
    div.addEventListener('mousedown', function () {
        if(mousedown)
        div.style.backgroundColor = divsStyleColor
            
    })
    div.addEventListener('mouseover', function () {
        if(mousedown){
            div.style.backgroundColor = divsStyleColor
        }
        btn.addEventListener('click', function() {
            div.style.backgroundColor = 'rgb(186, 186, 186)'
        })
    })
    main.appendChild(div)
}


function generateRandomColor() {
    let letters = '0123456789ABCDEF'
    let color = '#'
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random()*16)]
    }
    return color;
}


   
