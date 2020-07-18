"use strict"

function insert(num) {
    document.querySelector(".textview").value += num
}

function clean() {
    document.querySelector(".textview").value = "";
}

function back() {
    let exp = document.querySelector(".textview").value
    document.querySelector(".textview").value = exp.substr(0, exp.length - 1);
}

function equal() {
    let exp = document.querySelector(".textview").value;
    if (exp) {
        document.querySelector(".textview").value = eval(exp);
    }
}