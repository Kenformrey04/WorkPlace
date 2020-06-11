let one = "Моя первая переменная!";

document.getElementsByClassName("myclass")[0].style.color = "white";
$(".myclass").css("background-color", "green");

// todo Массивы
// array = [1, 2, 3, 4, 5];
// console.log(array.concat("dfsdf")); //добавляем элемент в список
// console.log(array.slice(0, 3)); // показывает элементы в заданных промежутках
// console.log(array.splice(1, 2, "2", "3")) // заменяем 1 и 2 элементы на  "2", "3"
// array.push("23");// добавляем элемент в конец списка
// array.unshift("23");// добавляем элемент в начало списка
// array.pop();// возращает удаленное значение из конца списка
// array.shift();// возращает удаленное значение из начала списка
// array.join("-");// преобразуем массив в строку и делаем свой собственный разделитель
// array.sort();// сортирует массив
// todo Работа с массивами в циклах

// array = [1, 2, 3, 4, 5];
// for (i = 0; i < array.length; i++) {
//     console.log(array[i]);
// }

// todo Функции
// function mySumm(a,b) {
//     return a + b;
// }
// console.log(mySumm(2,4));

function mySumShow(a,b) {
    result = a + b;
    document.getElementsByClassName("myclass")[0].innerHTML = result
}

// mySumShow(2,6)

// todo другой вариант решения
function mySumShow(a,b) {
    document.getElementsByClassName("myclass")[0].innerHTML = mySumm(a,b);
}

mySumShow(15,6);

// todo События

let say = function () {
    alert('Привет!');
}
// test.addEventListener("click", say); // добавляем событие на лев кном мыш
// test.addEventListener("contextmenu", say); // добавляем событие на прав кноп мыш
// test.addEventListener("mouseover", say); // при наведении покажет событие
// test.addEventListener("mousemove", say); // при движении мыши
// test.removeEventListener("click", say); // убираем событие на элемент









