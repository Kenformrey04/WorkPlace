let img_item = document.getElementsByClassName('img_item'),
button_three = document.getElementById('button_three'),
button_item = document.getElementsByClassName('button_item'),
left_button = document.getElementById('left_button'),
rigth_button = document.getElementById('rigth_button'),
slaiderIndex = 1;

ShoWSlider(slaiderIndex);
function ShoWSlider(n) {
    if(n<1){
        slaiderIndex = img_item.length;
    }
    else if(n > img_item.length){
        slaiderIndex = 1; 
    }

    for(let i = 0; i < img_item.length; i++ ){

    img_item[i].style.display = 'none';
}
    

    for(let i = 0; i < button_item.length; i++ ){

    button_item[i].classList.remove('new_class');
}
img_item[slaiderIndex - 1].style.display = 'block';
button_item[slaiderIndex-1].classList.add('new_class');

}


function PlusSlider(n) {
    ShoWSlider(slaiderIndex += n);
    
}
function ClearSlider(n) {
    ShoWSlider(slaiderIndex = n);
    
}

left_button.onclick = function (){
    PlusSlider(-1);
}
rigth_button.onclick = function (){
    PlusSlider(1);
}


button_three.onclick = function(e){
    for(let i = 0; i < button_item.length +1; i++){
    if(e.target.classList.contains('button_item') && e.target == button_item[i-1])
    ClearSlider(i);
    }


}