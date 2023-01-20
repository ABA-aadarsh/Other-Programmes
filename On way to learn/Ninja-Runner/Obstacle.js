class OBSTACLE{
    constructor(x,index){
        this.index=index
        this.size={
            width:40,
            height:30
        }
        this.position={
            x:x,
            y:canvas.height-this.size.height-112
        }
        this.velocity={
            x:-7
        }
    }
    update(){
        if(this.position.x+this.size.width+0.2<=0){
            // i.e: the obstacle block has gone outside of the canvas screen
            const refBlockX=obstacles[refBlockIndex].position.x
            const newx=refBlockX+450+Math.floor(Math.random()*20)*20
            this.position.x=newx
            refBlockIndex=this.index
        }else{
            this.position.x+=this.velocity.x
        }
    }
    draw(){
        c.fillStyle="red"
        c.fillRect(this.position.x,this.position.y,this.size.width,this.size.height)
    }
}
const setObstacles=()=>{
    for(let i=0;i<3;i++){
        let x=0
        if(i==0){
            x=Math.floor(Math.random()*150+850)
        }else{
            const previousBlockx=obstacles[i-1].position.x
            x=previousBlockx+450+Math.floor(Math.random()*20)*20
        }
        const obs=new OBSTACLE(x,i)
        obstacles.push(obs)
    }
}
