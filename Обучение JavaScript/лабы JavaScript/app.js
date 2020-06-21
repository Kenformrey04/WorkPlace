//! 1 часть 4 лаба
// arr = [1,3,44,4,43,6,7,8,9];

// let min = Math.min.apply(null, arr);
// let max = Math.max.apply(null, arr);

// let indexMin = arr.indexOf(min);
// let indexMax = arr.indexOf(max);

// arr[indexMin] = max;// минимальное число меняем на максимальное
// arr[indexMax] = min;// максимальное число меняем на минимальное

// console.log(arr);

// arr.sort( (a, b) => a - b );// сортировка по возрастанию

//? Даны два массива действительных чисел по 12 элементов в каждом. Заменить
//? нулями те элементы первого массива, которые есть во втором.

// let a = [0,1,2,3,4,5,6,7,8,9,10,11];
// let b = [1,97,79,29,21,45,25,53,8,9,10,11];

// let aArr = [...new Set(a)];
// let bArr = [...new Set(b)];

// console.log(`[1 massiv] ${aArr}     [2 massiv] ${bArr}`);

// for (let i = 0; i < a.length; i++) {
//     for (let j = 0; j < b.length; j++) {
//         if (aArr[i] === bArr[j]) {
//             aArr[i] = 0;
//         }
//     }
// }
// console.log(`1 massiv after ${aArr}`);

//! Nice lifehack
//todo dynamic variable

// const dynamic = "engine2";
// const engval = "3.2"

// let car = {
//     name:"Honda",
//     [dynamic]: engval
// };

// console.log(car);

//todo  short if

// const cond = true;

// function sayhello(){
//     console.log("hello");
// }

//  cond && sayhello()

//todo replace string

//const txt = "javascript javascript"
//console.log(txt.replace(/java/gi, "script"))

//const arr = [1,2,23,45,4,5,4556,3,4,3,3];

// //! unic values
// let un_arr = [...new Set(arr)];

//console.log(arr);
//console.log(un_arr);

// let aArr = [...new Set(a)];
// let bArr = [...new Set(b)];
// console.log(`[1 massiv] ${aArr} [2 massiv] ${bArr}`);

//! 4 часть 4 лабы
// let a = [0, -1, 2, -3, 4, -5, -6, 7, 8, -9, 10, -11];
// let b = [];ё
// let c = [];

// for (let i = 0; i < a.length; i++) {
//   if (a[i] > 0) {
//     b.push(a[i]);
//   } else if (a[i] < 0) {
//     c.push(a[i]);
//   }
// }
// console.log(`a massiv ${a} amount: ${a.length}`);
// console.log(`b massiv ${b} amount: ${b.length}`);
// console.log(`c massiv ${c} amount: ${c.length}`);

// binary search

// function binarySearch(list, item) {
//   let low = 0;
//   let high = list.length - 1;// 4
//   while (low <= high) {
//       let mid = (low + high);// 4
//       let guess = list[mid];// 9
//       if (guess === item) {
//         return mid
//       }
//       if (guess > item) { // true
//         high = mid - 1; //3
//       }
//       else {
//         low = mid + 1;
//       }
//   }
// }

// myList = [1,3,5,7,9]
// console.log(binarySearch(myList,7));
// console.log(binarySearch(myList,-1));

//! task 1
//? составить функцию, которая заполняет массив целыми числами по формуле
//? m[i] = a * (i - b) где a and b целые числа, которые передаются в функцию в
//? качестве параметров

// let arr1 = [],
//     arr2 = [],
//     arr3 = [];

// function one(a, b) {
//   for (let i = 0; i < b; i++) {
//     arr1[i] = a * (i - b);
//     arr1.push(arr1[i]);
//   }
//   return `First task: <br> arr: ${arr1} <br> <br>`; ;
// }
// document.querySelector(".one_task").innerHTML = one(7, 14);
// console.log(one(7, 14));

//! task 2
//? составить функцию, которая выводит массив на экран в виде двух строк:
//? в первой - значения, во второй - номера элементов массива.

// function two(a, b) {
//   for (let i = 0; i < b; i++) {
//     arr2[i] = a * (i - b);
//     arr2.push(arr2[i]);
//     arr3.push(i);
//   }
//   return `Two task: <br> arr: ${arr2} <br> number elements: ${arr3}`;
// }
// document.querySelector(".two_task").innerHTML = two(5,10);
// console.log(two(5,10));














