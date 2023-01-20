class Player extends Sprite{
    constructor({imgsrc,frameRate,position,motion}){
        super({imgsrc,position,motion,frameRate})
        this.velocity={
            y:0
        }
        this.position=position
        this.gravity=0.8
        this.color="blue"
    }
    gravityAndMotion(){
        this.position.y+=this.velocity.y
        if(player.position.y>=(canvas.height-this.height-112)){
            player.position.y=canvas.height-this.height-112
            player.velocity.y=0
        }else{
            this.velocity.y+=this.gravity
        }
    }
    collisionDetection(){
        const hitBox={
            position:{
                x:this.position.x+33,
                y:this.position.y+39
            },
            width:30,
            height:57
        }
        for(let i=0;i<3;i++){
            const block=obstacles[i]
            if(hitBox.position.x<=block.position.x+block.size.width &&
                hitBox.position.x+hitBox.width>=block.position.x &&
                hitBox.position.y<=block.position.y+block.size.height &&
                hitBox.position.y+hitBox.height>=block.position.y
            ){
                this.color="green"
                exit=true
            }
        }
    }
    update(){
        this.gravityAndMotion()
        this.collisionDetection()
    }
    hitBoxDraw(){
        const hitBox={
            position:{
                x:this.position.x+33,
                y:this.position.y+39
            },
            width:30,
            height:57
        }
        c.fillStyle="orange"
        c.fillRect(hitBox.position.x,hitBox.position.y,hitBox.width,hitBox.height)
    }
    BlockDraw(){
        c.fillStyle=this.color
        c.fillRect(this.position.x,this.position.y,this.width,this.height)
    }
}