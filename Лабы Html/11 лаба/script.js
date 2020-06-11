// todo 1 task
let person1 = {
    fullName: function () {
        return this.firstName + " " + this.lastName;
    }
}
let person2 = {
    firstName: "John",
    lastName: "Doe",
}
let x = person1.fullName.call(person2);
document.querySelector(".demo").innerHTML = x;

// todo 2 task

// function myFunction() {

//     var message, x;
//     message = document.getElementById("p01");
//     message.innerHTML = "";
//     x = document.getElementById("demo").value;

//     try {
//         if (x == "") throw "is empty";
//         if (isNaN(x)) throw "is not a number";
//         x = Number(x);
//         if (x > 10) throw "is too high";
//         if (x < 5) throw "is too low";
//     } catch (err) {
//         message.innerHTML = "Input " + err;
//     } finally {
//         document.getElementById("demo").value = "";
//     }


// }

// todo 3 task
function myFunction() {

    var message, x;
    message = document.getElementById("p01");
    message.innerHTML = "";
    x = document.getElementById("demo").value;

    try {
        if (x == "") throw "is empty";
        if (isNaN(x)) throw "is not a number";
        x = Number(x);
        if (x > 10) throw "is too high";
        if (x < 5) throw "is too low";
    } catch (err) {
        message.innerHTML = "Input " + err;
    } finally {
        document.getElementById("demo").value = "";
    }


}