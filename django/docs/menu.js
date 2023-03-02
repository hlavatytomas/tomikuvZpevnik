var open = document.getElementById("open_pdf_menu");
open.addEventListener("click", function(){
    document.getElementById("sidebar").classList.toggle("active");
    document.getElementById("hide").classList.toggle("active");
    event.stopPropagation();
})

var close = document.getElementById("close_pdf_menu");
close.addEventListener("click", function(){
    document.getElementById("sidebar").classList.toggle("active");
    document.getElementById("hide").classList.toggle("active");
    event.stopPropagation();
})

var hide = document.getElementById("hide");
close.addEventListener("click", function(){
    document.getElementById("sidebar").classList.toggle("active");
    document.getElementById("hide").classList.toggle("active");
    event.stopPropagation();
})