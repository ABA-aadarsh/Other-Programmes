const canvas=document.querySelector("#canvas")
canvas.width=1024
canvas.height=576
const c=canvas.getContext("2d")
c.fillStyle="black"
c.fillRect(0,0,canvas.width,canvas.height)
const simulation={
    i:2,
    count:1,
    availableSteps:1,
    prevTotalSteps:1,
    direction:"+x",
    position:{
        x:canvas.width/2,
        y:canvas.height/2
    },
    motion:{
        "+x":[13,0],
        "+y":[0,13],
        "-x":[-13,0],
        "-y":[0,-13]
    }
}
const changeDirection=()=>{
    const directions=["+x","-y","-x","+y"]
    let currentindex=directions.indexOf(simulation.direction)
    if(currentindex==3){
        simulation.direction="+x"
    }else{
        const newDirection=directions[currentindex+1]
        simulation.direction=newDirection
    }
}
const checkPrime=(n)=>{
    if(n==0 || n==1){
        return false
    }else{
        let flag=true
        for(let a=2;a<n;a++){
            if(n%a==0){
                flag=false
                break
            }
        }
        return flag
    }
}
const drawCircle=(color)=>{
    c.beginPath();
    c.arc(
        simulation.position.x, 
        simulation.position.y, 
        4, 
        0, 
        2 * Math.PI
    )
    c.fillStyle=color
    c.fill()
    c.stroke(); 
}
const draw=()=>{
    const vector=simulation.motion[simulation.direction]
    c.beginPath();
    c.moveTo(simulation.position.x,simulation.position.y);
    c.lineTo(simulation.position.x+vector[0],simulation.position.y+vector[1]);
    c.lineWidth=1
    c.strokeStyle="white"
    c.stroke();
    simulation.position.x+=vector[0]
    simulation.position.y+=vector[1]
}
for(let i=0;i<=1500;i++){
    if(simulation.availableSteps==0){
        changeDirection()
        simulation.i-=1
        if(simulation.i==0){
            simulation.availableSteps=simulation.prevTotalSteps+1
            simulation.prevTotalSteps++ //for next time
            simulation.i=2
        }else{
            simulation.availableSteps=simulation.prevTotalSteps
        }
    }
    if(checkPrime(simulation.count)==true){
        drawCircle("white")
    }
    draw()
    simulation.count++
    simulation.availableSteps-=1
}