var slides = document.getElementsByClassName("slide");
var mover = 0;

function change(x){
    mover = mover + x;
    slideimage(mover);
}

slideimage(mover)

function slideimage(num){
    
    if(num == slides.length){
        mover = 0;
        num = 0;
    }
    if(num < 0){
        mover = slides.length-1;
        num = slides.length-1;
    }
    
    for(let y of slides){
        y.style.display = "none"
    }
    
    slides[num].style.display = "block";
}