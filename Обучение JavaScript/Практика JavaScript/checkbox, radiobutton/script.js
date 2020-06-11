// todo function for checkbox
function fun1() {
    let first = document.getElementById("one");
    if (first.checked) {
        alert("Выбран");
    } else {
        alert("Не выбран");
    }
}

function fun2() {
    let radi= document.getElementsByName("r1");
    for (let i = 0; i < radi.length; i++) {
        if (radi[i].checked) {
            alert("Выбран " + i + " Элемент");
        }

    }
}