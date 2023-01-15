const double_angle=document.querySelector(".motion-icon")
const fpw=document.querySelector(".forgot-pw")
const input_boxes=[...document.querySelectorAll(".input-box input")]
fpw.addEventListener("mousemove",()=>{
    double_angle.classList.add("move-right")
})
fpw.addEventListener("mouseout",()=>{
    double_angle.classList.remove("move-right")
})
input_boxes.forEach((input)=>{
    input.addEventListener("focus",()=>{
        input.parentElement.style.outline="1px solid #4e4eace6"
    })
    input.addEventListener("focusout",()=>{
        input.parentElement.style.outline="0px"
    })
})