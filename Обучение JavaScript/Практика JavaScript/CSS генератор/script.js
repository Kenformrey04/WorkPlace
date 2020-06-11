let corTitles = ["tl", "tr", "br", "bl"];

function rangeChanged(cT) {
    let rangeBox = document.getElementById("r" + corTitles[cT]);
    let textBox = document.getElementById("t" + corTitles[cT]);
    textBox.value = rangeBox.value;
    changeBlock();
}

function textChanged(cT) {
    let rangeBox = document.getElementById("r" + corTitles[cT]);
    let textBox = document.getElementById("t" + corTitles[cT]);
    rangeBox.value = textBox.value;
    changeBlock();
}

function changeBlock() {
    //let values = new Array(4);
    let cssGen = "";
    for (let i = 0; i < 4; i++) {
        let curInp = document.getElementById("t" + corTitles[i]);
        cssGen += (curInp.value + "px ");
    }

    let block = document.getElementById("block");
    block.style.borderRadius = cssGen;

    let screen = document.getElementById("screen");
    screen.innerHTML = "border-radius: " + cssGen + ";";
}