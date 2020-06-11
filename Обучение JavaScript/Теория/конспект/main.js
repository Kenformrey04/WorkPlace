//todo Переменный
// var message; // a-z, A-Z, 0-9 $ _
// var myMessage;
// myMessage = 'Сообщение';

// var myNumber = 10.234;
// var myBoolean = true;
// var myNull = null; //переменная равна Ничему!!
// var myUNdefined = undefined; //значение отстутствует
// var myString = "Привет Вася"
// var myObject = {
//     name: 'Vasya',
//     age: 25
// };

//todo ЧИСЛА

// var result = 40+10;
// alert(result);

// console.log(50+myNumber);
// console.log(50-myNumber);
// console.log(50*myNumber);
// console.log(50/myNumber);

// myNumber += 12;
// myNumber ++;

// console.log(myNumber);
// console.log(Math.round(5.55));
// console.log(Math.ceil(5.1));// округляет в большую сторону
// console.log(Math.floor(5.1));// округляет в меньшую сторону

// var newNumber = 2.454;
// console.log( newNumber.toFixed(1));// число округляет до 1 цифры после запятой


//todo СТРОКИ
// console.log('40' + myNumber);
// console.log(myString +" Как дела?");
// console.log(myString.toLowerCase());
// console.log(myString.toUpperCase());

//todo МАССИВЫ
// var names = ["Vasya","Petya","Jenya"];
// console.log(names[1].toUpperCase());//берем 1 элемент списка и ставим в upper

// names[0] = 'Masha';
// console.log(names[0]);

// names.push("Sveta");// добавляет в конец массива Sveta
// console.log(names[3]);// смотрим 3 элемент массива

// console.log(names);// выводим весь массив

//todo УСЛОВИЯ
// (&& это логическое "И"")  (|| это логическое "ИЛИ")

// if (4 <5){
// 	console.log('Условие выполнилось');
// }

// if ("Вася"!=="Петя" && myNumber < 20){
// 	console.log("Успех");
// }

// if (myNumber < 20) {
// 	console.log("Число меньше 20!")

// }else{
// 	console.log("Число больше 20!")
// }

//todo ЦИКЛЫ
// names.length это длинна массива

// for (var i = 0; i <10 ; i++){
// 	if (i == 5) {
// 		continue;
// 	}

// 	console.log(i);
// }

// for (var j = 0; j < names.length; j++){
// 	console.log(names[j]);
// }

// var i = 0;
// while (i < 10) {
// 	console.log(i);
// 	i++;
// }

//todo ФУНКЦИИ

// function sum(x,y) {
// 	return x + y ;
// }

// var result = sum(10,56);

// console.log(sum(56,74));

//todo ОБЪЕКТЫ

// var myObject = {
//     name: 'Vasya',
//     surname: " Vasyin",
//     age: 25,
//     getFullName: function () {
//         return this.name + this.surname;
//     }
// };

// myObject.name = "Petya"
// // console.log(myObject.name)
// console.log(myObject.getFullName())



let user = {
    name: "John",
    age: 30
};

let key = prompt("Что вы хотите узнать о пользователе?", "name");

// доступ к свойству через переменную
alert(user[key]); // John (если ввели "name")
