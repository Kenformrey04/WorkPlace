let ageField = document.querySelector('.age');
	oneArr = document.querySelector('.oneArr'),
	twoArr = document.querySelector('.twoArr'),
	threeArr = document.querySelector('.threeArr'),
	fourArr = document.querySelector('.fourArr'),
	fiveArr = document.querySelector('.fiveArr'),
	comparisonsFieldOne = document.querySelector('.comparisonsOne');
	comparisonsFieldTwo = document.querySelector('.comparisonsTwo');
	comparisonsFieldThree = document.querySelector('.comparisonsThree');
	comparisonsFieldFour = document.querySelector('.comparisonsFour');
function getAge(date) {
	let now = new Date(),
		monthNow = now.getMonth(),
		yearNow = now.getFullYear(),
		month = date.substr(3, 5),
		year = date.substr(6, 10),
		age = yearNow - year;
	if (monthNow < month) {
		age -= 1;
	}
	return age ;
}
let date = prompt('Введите дату рождения', '');// вводим данные
let age = getAge(date);// применяем функцию к введенным данным
ageField.innerHTML = age;// добавляем значение age на страницу

let arr = [394, 392, 391, 393];// список
oneArr.innerHTML = arr;
twoArr.innerHTML = arr.sort();// сортируем список и выводим
arr.push(397);// добавляем элемент в список
threeArr.innerHTML = arr;
arr.splice(6, 0, 399);// добавляем по индексу в список
fourArr.innerHTML = arr;
length = arr.length;// длинна списка
fiveArr.innerHTML = arr + ' = ' + length + " элементов";
let a = 7,
	comparisonsOne = `${a==7}`,
	comparisonsTwo = `${a==="7"}`,
	comparisonsThree = `${a<9}`,
	comparisonsFour = `${a!==7}`;
comparisonsFieldOne.innerHTML = comparisonsOne;
comparisonsFieldTwo.innerHTML = comparisonsTwo;
comparisonsFieldThree.innerHTML = comparisonsThree;
comparisonsFieldFour.innerHTML = comparisonsFour;
