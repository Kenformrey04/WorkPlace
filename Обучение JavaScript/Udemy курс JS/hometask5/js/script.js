let menu = document.getElementsByClassName('menu'),
    item = document.getElementsByClassName('menu-item'),
    body = document.getElementsByTagName("body"),
    div = document.createElement("li"),
    column = document.getElementsByClassName('column'),
    title = document.getElementsByClassName('title'),
    adv = document.getElementsByClassName('adv'),
    answer = prompt("Как вы относитесь к технике Apple?"),
    Output = document.getElementById("prompt");

Output.innerHTML = answer;
document.body.style.backgroundImage = "url('img/apple_true.jpg')";
menu[0].insertBefore(item[2], item[1]);
column[1].removeChild(adv[0]);
title[0].innerHTML = " Мы продаем только подлинную технику Apple"
div.classList.add("menu-item");// dd div with class black
menu[0].appendChild(div); a
div.innerHTML = "Пятый пункт";// add text in element

// item[2].style.backgroundColor = 'blue';
// column[1].removeChild(title[0]);



