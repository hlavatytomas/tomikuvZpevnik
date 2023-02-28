window.onload = fillDropdown;

var list;

function onlyUnique(value, index, array) {
    return array.indexOf(value) === index;
}

function fillDropdown() {
    list = document.querySelectorAll('div.song_item');
    var owners = [];
    for (let i = 0; i < list.length; i++) {
        owners.push(list[i].getAttribute("owner"));
    }
    var unique = owners.filter(onlyUnique);
    document.getElementsByClassName("items")[0].innerHTML = "";
    unique.forEach(element => {
        document.getElementsByClassName("items")[0].innerHTML += '<li><input type="checkbox" onchange="toggleVisibility(this,'+"'"+element+"'"+')" checked/>' + element + '</li>'
    });
    var checkList = document.getElementById('list1');
    checkList.getElementsByClassName('anchor')[0].onclick = function (evt) {
        if (checkList.classList.contains('visible'))
            checkList.classList.remove('visible');
        else
            checkList.classList.add('visible');
    }

}


function toggleVisibility(obj,owner) {
    var owned = [...list].filter((value, index, array) => value.getAttribute("owner") == owner)
    if(obj.checked){
        owned.forEach(song => {
            song.setAttribute("style","")
        });
    }
    else {
        owned.forEach(song => {
            song.setAttribute("style", "display:none;")
        });
    }
}

