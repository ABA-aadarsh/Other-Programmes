const cubePieces=[...document.querySelectorAll(".cube-piece")]
const styleTag=document.querySelector("style")


// [[translateX,translateY,translateZ],[rotateX,rotateY,rotateZ]]
const transformInfo=[
    // top layer
[[100,0,0],[0,0,0]],
[[200,0,0],[0,0,0]],
[[300,0,0],[0,0,0]],
[[100,-100,0],[0,0,0]],
[[200,-100,0],[0,0,0]],
[[300,-100,0],[0,0,0]],
[[100,-200,0],[0,0,0]],
[[200,-200,0],[0,0,0]],
[[300,-200,0],[0,0,0]],
    // middle layer
[[100,0,-100],[0,0,0]],
[[200,0,-100],[0,0,0]],
[[300,0,-100],[0,0,0]],
[[100,-100,-100],[0,0,0]],
[[200,-100,-100],[0,0,0]],
[[300,-100,-100],[0,0,0]],
[[100,-200,-100],[0,0,0]],
[[200,-200,-100],[0,0,0]],
[[300,-200,-100],[0,0,0]],
    // bottom layer
[[100,0,-200],[0,0,0]],
[[200,0,-200],[0,0,0]],
[[300,0,-200],[0,0,0]],
[[100,-100,-200],[0,0,0]],
[[200,-100,-200],[0,0,0]],
[[300,-100,-200],[0,0,0]],
[[100,-200,-200],[0,0,0]],
[[200,-200,-200],[0,0,0]],
[[300,-200,-200],[0,0,0]],
]

let frontFace=[0,1,2,9,10,11,18,19,20]

let rightFace=[2,5,8,11,14,17,20,23,26]

let backFace=[8,7,6,17,16,15,26,25,24]

let leftFace=[6,3,0,15,12,9,24,21,18]

let bottomFace=[18,19,20,21,22,23,24,25,26]

let topFace=[6,7,8,3,4,5,0,1,2]

const rotation=(spin)=>{
    if( spin=="clockwise"){
        let temp=[...frontFace]
        frontFace=rightFace
        rightFace=backFace
        backFace=leftFace
        leftFace=temp
        temp=[topFace[6],topFace[3],topFace[0],topFace[7],topFace[4],topFace[1],topFace[8],topFace[5],topFace[2]]
        topFace=temp
        temp=[bottomFace[2],bottomFace[5],bottomFace[8],bottomFace[1],bottomFace[4],bottomFace[7],bottomFace[0],bottomFace[3],bottomFace[6]]
        bottomFace=temp
    }
    else if (spin=="anticlockwise"){
        rotation("clockwise")
        rotation("clockwise")
        rotation("clockwise")
    }
}
const _move_=(m)=>{
    // this is for array manipulation to record which piece is where after perfoming certain moves
    if (m=="R"){   
        let temp=[...[frontFace[2],frontFace[5],frontFace[8]]]

        frontFace[2]=bottomFace[2]
        frontFace[5]=bottomFace[5]
        frontFace[8]=bottomFace[8]

        bottomFace[2]=backFace[6]
        bottomFace[5]=backFace[3]
        bottomFace[8]=backFace[0]

        backFace[0]=topFace[8]
        backFace[3]=topFace[5]
        backFace[6]=topFace[2]

        topFace[2]=temp[0]
        topFace[5]=temp[1]
        topFace[8]=temp[2]

        temp=[...[rightFace[6],rightFace[3],rightFace[0],rightFace[7],rightFace[4],rightFace[1],rightFace[8],rightFace[5],rightFace[2]]]
        rightFace=temp
    }
    else if (m=="R!"){
        _move_("R")
        _move_("R")
        _move_("R")
    }  
    else if (m=="U"){

        let temp=[...[frontFace[0],frontFace[1],frontFace[2]]]

        frontFace[0]=rightFace[0]
        frontFace[1]=rightFace[1]
        frontFace[2]=rightFace[2]

        rightFace[0]=backFace[0]
        rightFace[1]=backFace[1]
        rightFace[2]=backFace[2]

        backFace[0]=leftFace[0]
        backFace[1]=leftFace[1]
        backFace[2]=leftFace[2]

        leftFace[0]=temp[0]
        leftFace[1]=temp[1]
        leftFace[2]=temp[2]

        temp=[...[topFace[6],topFace[3],topFace[0],topFace[7],topFace[4],topFace[1],topFace[8],topFace[5],topFace[2]]]
        topFace=[...temp]

    }
    else if (m=="U!"){
        _move_("U")
        _move_("U")
        _move_("U")
    }  
    else if (m=="B"){
        rotation("clockwise")
        _move_("R!")
        rotation("anticlockwise")
    }  
    else if (m=="B!"){
        rotation("clockwise")
        _move_("R")
        rotation("anticlockwise")
    }  
    else if (m=="F"){
        rotation("anticlockwise")
        _move_("R")
        rotation("clockwise")
    }  
    else if (m=="F!"){
        rotation("anticlockwise")
        _move_("R!")
        rotation("clockwise")
    } 
}


const init=()=>{
    let style=""
    for(let i=0;i<27;i++){
        const translate=transformInfo[i][0]
        style+=`#cube${i}{transform:translateX(${translate[0]}px) translateY(${translate[1]}px) translateZ(${translate[2]}px)
        rotateX(0deg) rotateY(0deg) rotateZ(0deg)
        ;}
        `
    }
    styleTag.innerHTML=style
}

const validMoves=["U","U!"]

const action=(indexlist,rx,ry,rz)=>{
    // later i will use array as parameter also
    let style=""
    for(let i=0;i<27;i++){
        const translate=transformInfo[i][0]
        const rotate=transformInfo[i][1]
        if(indexlist.indexOf(i)!=-1){
            if(rotate[0]%360==0){
                rotate[0]+=rx
                rotate[1]+=ry
                rotate[2]+=rz
            }
            else if(rotate[0]%360==90){
                rotate[0]+=rx
                rotate[1]+=rz
                rotate[2]+=ry
            }
            else if(rotate[0]%360==180 && rotate[1]%360==0){
                rotate[0]+=rx
                rotate[1]+=ry
                rotate[2]-=rz
            }
            else if(rotate[0]%360==180 && rotate[1]%360==90){
                rotate[0]-=rz
                rotate[1]+=rz
                rotate[2]+=rx
            }
        }
        style+=`#cube${i}{transform:translateX(${translate[0]}px) translateY(${translate[1]}px) translateZ(${translate[2]}px)
        rotateX(${rotate[0]}deg) rotateY(${rotate[1]}deg) rotateZ(${rotate[2]}deg)
        ;
        transition:0.5s linear;}
        `
    }

    styleTag.innerHTML=style
}

const MOVE=(move)=>{
    if(move==="U"){
        action(topFace,0,0,90)
        _move_("U")
    }
    else if(move==="U!"){
        action(topFace,0,0,-90)
        _move_("U!")
    }
    else if(move==="R"){
        action(rightFace,90,0,0)
        _move_("R")
    }
    else if(move==="R!"){
        action(rightFace,-90,0,0)
        _move_("R!")
    }
    else if(move==="F"){
        action(frontFace,0,90,0)
        _move_("F")
    }
    else if(move==="F!"){
        action(frontFace,0,-90,0)
        _move_("F!")
    }
    else if(move==="B"){
        action(backFace,0,-90,0)
        _move_("B")
    }
    else if(move==="B!"){
        action(backFace,0,90,0)
        _move_("B!")
    }
}


init()

// listening to the event for performing moves
window.addEventListener("keyup",(e)=>{
    e.preventDefault()

    // e.g: (u)=>Up(U) (shift+u)=>Up Prime(U!)

    if(e.key=="u"){
        MOVE("U")
    }
    else if(e.key=="U"){
        MOVE("U!")
    }
    else if(e.key=="r"){
        MOVE("R")
    }
    else if(e.key=="R"){
        MOVE("R!")
    }
    else if(e.key=="f"){
        MOVE("F")
    }
    else if(e.key=="F"){
        MOVE("F!")
    }
    else if(e.key=="b"){
        MOVE("B")
    }
    else if(e.key=="B"){
        MOVE("B!")
    }
    console.log("....................")
    console.log("frontFace:",frontFace)
    console.log("rightFace:",rightFace)
    console.log("topFace:",topFace)
    console.log("....................")

})













/*
    1. U and U prime with keyboard event
*/