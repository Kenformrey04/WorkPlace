
//  let a = 16;

//  if (a>9) {
//      console.log("Yes");
//  }
//  else {
//      console.log("else");
//  }

// let button = document.querySelector("button");
const button = document.querySelector("button"); //todo не изменяется
const input = document.querySelector("age"); // то что мы вводим

//todo () => стрелочная функция
button.onclick = () => {
    let num = +input.value;
    if (num >= 16 && num < 60) {
        console.log("Welcome!!!");
    } else if (num > 60) {
        console.log("Ты точно сюда???");
    } else {
        console.log("Ты не пройдешь!!!");
    }
}