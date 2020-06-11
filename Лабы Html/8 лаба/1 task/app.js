input.onblur = function() {
    if (!input.value.includes('@')) { // не email
      input.classList.add('invalid');
      error.innerHTML = 'Пожалуйста, введите правильный email.'
    }
  };


function validateForm() {
    var x = document.forms["form"]["name"].placeholder;
    if (x == "") {
        document.getElementById("name").placeholder = "Укажите имя";
    }

    x = document.forms["form"]["lastName"].placeholder;
    if (x == "") {
        document.getElementById("lastName").placeholder = "Укажите фамилию";
    }

    x = document.forms["form"]["login"].placeholder;
    if (x == "") {
        document.getElementById("login").placeholder = "Поле  не должно быть пустым!";
    }

    x = document.forms["form"]["date"].placeholder;
    if (x == "") {
        document.getElementById("date").placeholder = "Поле  не должно быть пустым!";
    }

    x = document.forms["form"]["pas"].placeholder;
    if (x == "") {
        document.getElementById("pas").placeholder = "Поле  не должно быть пустым!";
    }
    x = document.forms["form"]["pas"].placeholder;
    if (x == "") {
        document.getElementById("pas").placeholder = "Поле  не должно быть пустым!";
    }
    x = document.forms["form"]["sq"].placeholder;
    if (x == "") {
        document.getElementById("sq").placeholder = "Поле не должно быть пустым!";
    }

    x = document.forms["form"]["age"].placeholder;
    if (x < 0 || x > 100 || x == "") {
        document.getElementById("age").value = "";
        document.getElementById("age").placeholder = "Введите корректный возраст!";
    }
    x = document.forms["form"]["em"].placeholder;
    if (x.indexOf('@') != 1) {
        document.getElementById("em").placeholder = "Поле должноо содержать @";
    }
}
