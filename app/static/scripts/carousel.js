var slideIndex = 1;
showSlide(slideIndex);
showSlides();

function plusSlide(n){
    showSlide(slideIndex += n);
}

function currentSlide(n){
    showSlide(slideIndex = n);
}

function showSlide(n){
    var i;
    var slides = document.getElementsByClassName('slide');
    var dots = document.getElementsByClassName('dot');

    if (n > slides.length){
        slideIndex = 1
    }
    if (n < 1){
        slideIndex = slides.length
    }
    for (i=0; i < slides.length; i++){
        slides[i].style.display = "none";

    }
    for (i=0; i < dots.length; i++){
        dots[i].className = dots[i].className.replace("active", "");

    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
    
}

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("slide");
    var dots = document.getElementsByClassName('dot')
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    setTimeout(showSlides, 5000);
    for (i=0; i < dots.length; i++){
        dots[i].className = dots[i].className.replace("active", "");

    }
    dots[slideIndex-1].className += " active"; // Change image every 2 seconds
}
