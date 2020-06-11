"use strict";
let a = 7;
let b = 9;

console.log(a);

let inputIn = document.querySelector(".input-in");//input
let button  = document.querySelector("button"); // button
let div = document.querySelector(".out");

button.onclick = function() {
    //кнопка будет нажата
    console.log("Работает");
    console.log(inputIn.value);// value - то что введено в INPUT\
    let b = +inputIn.value;// + позволяет перевести в число
    console.log(a*b);
    div.innerHTML = b;// передаем блоку div значение которе мы ввели
    inputIn.value = "";// очищает поле ввода
}



















