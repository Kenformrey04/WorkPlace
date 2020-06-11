function changeCol() {
    var ch = true;
    switch (ch) {
        case document.getElementById("red").checked:
            document.getElementById("tex").style.color = 'red';
            break;

        case document.getElementById("ye").checked:
            document.getElementById("tex").style.color = 'yellow';
            break;

        case document.getElementById("g").checked:
            document.getElementById("tex").style.color = 'green';
            break;

        case document.getElementById("o").checked:
            document.getElementById("tex").style.color = '#ff6666';
            break;

        case document.getElementById("bg").checked:
            document.getElementById("tex").style.color = '#b3b300';
            break;

        case document.getElementById("wg").checked:
            document.getElementById("tex").style.color = '#ace600';
            break;

        default: document.getElementById("tex").style.color = 'green';
            break;
    }
}





















