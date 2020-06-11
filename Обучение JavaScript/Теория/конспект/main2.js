
//todo более простой метод
// function Fruit (color,shape) {
//     this.color = color;
//     this.shape = shape;
// }

// var melon = new Fruit('yellow','round');
// var melon = new Fruit('red','round');

//todo 1 вариант внизу
// var apple = new Object();
// apple.color = 'green';
// apple.shape = 'round';

// apple.describe = function() {
//     return 'An apple is ' + this.color;
// }
// document.write(apple.describe()+ '<br>');

//todo СОЗДАНИЕ ОБЬЕКТОВ 
// var person = {
//     firstName: 'Brad',
//     age: 45,
//     children: ['Liza','Petya'],
//     adress: {
//         street: "555 Some st",
//         city: 'Boston',
//         state: 'MA'
//     },
//     NameAge: function() {
//         return this.firstName + ',age iss -' + this.age;
//     }
// }
// document.write(person.firstName +'<br>');
// document.write(person.adress.city +'<br>');
// document.write(person.age);

//todo Функции 
// function summ(a,b){
//     return a + b;
// }

// document.write(summ(25,43));


//todo Операторы условий
// var num_1 = 23;
// var num_2 = 45;

// if (num_1 > num_2) {
//     document.write(num_1 + '>' + num_2);

// } else if (num_1 == num_2) {
//     document.write(num_1 + '=' + num_2);
// } else {
//     document.write(num_1 + '<' + num_2);
// }

// var res = 3;
// switch (res) {
//     case 1:
//         alert('res is 1');
//         break;
//     case 2:
//         alert('res is 2');
//         break;
//     case 3:
//         alert('res is 3');
//         break;
//     default:
//         break;
// }  


//todo Циклы  WHILE AND FOR

// var i = 20
// do {
//     document.write(i + "<br>");
// } while (i < 10);

// var i = 200;
// while (i >= 10) {
    // document.write(i + "<br>");
    // i /= 2;
// }

// var colors = new Array('Red', 'Blue', 'Green');
// for (var i = 0; i < colors.length; i++) {
    // document.write(colors[i] + '<br>');
// }

//todo Массивы
// var colors = new Array('Red', 'Blue', 'Green');
// colors.push('Grey');
// document.write(colors[0]);

//Можно и так записать
// var colors = ['Red','Blue',"Green"];

//todo Математические операции
// var firstNum = 12;
// var secondNum = 24;
// firstNum += 2;
// document.write(Math.floor(2.66) + "<br>");
// document.write('Результат:', + firstNum + secondNum);

// var num = 1.45;
// var Num = "String";
// var bool = true;
// console.log(Num);

// var name = prompt("Как вас зовут?"); // ЭТО ТИПА INPUT IN PYTHON
// console.log('Ваше имя ' + name);
