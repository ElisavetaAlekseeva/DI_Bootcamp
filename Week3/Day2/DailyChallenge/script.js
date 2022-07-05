let form = document.forms[0]

form.addEventListener('click', function (event) {
    event.preventDefault()
    var noun = document.getElementById('noun').value
    var adjective = document.getElementById('adjective').value
    var verb = document.getElementById('verb').value
    var place = document.getElementById('place').value
    var person = document.getElementById('person').value
    if (noun.length > 0 && adjective.length > 0 && verb.length > 0 && place.length > 0 && person.length > 0) {
        story()

    }
})


function story () {
    let spn = document.getElementsByTagName('span')[0]
    let story = 'This story about ' + person.value + ' from ' + place.value + ' , that ' + verb.value + ' a ' + adjective.value + noun.value
    console.log(story);
}