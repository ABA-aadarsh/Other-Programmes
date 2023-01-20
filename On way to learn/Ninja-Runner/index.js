const canvas=document.querySelector("#canvas")
canvas.width=1024
canvas.height=576
let exit=false
const c=canvas.getContext("2d")

let refBlockIndex=2
const obstacles=[]
setObstacles()

const player=new Player({
    imgsrc:"./Asset/Ninja_Peasant/Jump.png",
    frameRate:8,
    position:{
        x:100,
        y:389 
    },
    motion:true
})
const background=new Sprite(
    {
        imgsrc:"./Asset/Bg.png",
        position:{
            x:0,
            y:0
        },
        motion:false
    }
)
const animate=()=>{
    window.requestAnimationFrame(animate)
    c.clearRect(0,0,canvas.width,canvas.height) 
    background.draw()
    if(exit!=true){
        for(let i=0;i<3;i++){
            obstacles[i].update()
        }
    }
    for(let i=0;i<3;i++){
        obstacles[i].draw()
    }
    player.update()
    // player.BlockDraw()
    player.hitBoxDraw()
    player.draw()
}
animate()
window.addEventListener("keydown",(e)=>{
    const d=15
    if(e.key=="ArrowUp"){
        if(player.position.y>(canvas.height-player.height-112-0.5)){
            player.velocity.y-=d
        }
    }
    // else if(e.key=="ArrowLeft"){
    //     player.position.x-=d
    // }else if(e.key=="ArrowRight"){
    //     player.position.x+=d
    // }
})