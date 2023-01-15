const date= new Date()
let currSec=date.getSeconds()
let currHour=date.getHours()
let currMinute=date.getMinutes()

const secondHand=document.querySelector("#second")
const minuteHand=document.querySelector("#minute")
const hourHand=document.querySelector("#hour")

let hourdeg=(currHour+currMinute*(1/60))*30
// minute le pni hour ko angle lae impact parcha so tyeslae pni consider garnu parcha angle lae ramro sanga sync garna

const CLOCK=()=>{
    const secdeg=currSec*6;
    const minutedeg=currMinute*6;
    // second is equivalent to degree
    secondHand.setAttribute("style",`transform:rotate(${(secdeg-90)%360}deg)`)

    minuteHand.setAttribute("style",`transform:rotate(${(minutedeg-90)%360}deg)`)

    hourHand.setAttribute("style",`transform:rotate(${(hourdeg-90)%360}deg)`)
}
// initialize
CLOCK()
const START=setInterval(() => {
    currSec+=1
    if(currSec>=60){
        currMinute+=1;
        hourdeg+=0.45;
        currSec%=60;
    }
    CLOCK()
}, 1000);