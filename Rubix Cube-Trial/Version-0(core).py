import pygame
pygame.init()
width=800
height=530
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Rubik's Cube")
clock=pygame.time.Clock()
front=[ 1,2,3,
        4,5,6,
        7,8,9]
right=[ 10,11,12,
        13,14,15,
        16,17,18]
back=[  19,20,21,
        22,23,24,
        25,26,27]
left=[  28,29,30,
        31,32,33,
        34,35,36]
bottom=[37,38,39,
        40,41,42,
        43,44,45]
top=[   46,47,48,
        49,50,51,
        52,53,54]
#Cubes Cordinates
leftFace=[(30,190),(80,190),(130,190),(30,240),(80,240),(130,240),(30,290),(80,290),(130,290)]
frontFace=[(190,190),(240,190),(290,190),(190,240),(240,240),(290,240),(190,290),(240,290),(290,290)]
rightFace=[(350,190),(400,190),(450,190),(350,240),(400,240),(450,240),(350,290),(400,290),(450,290)]
backFace=[(510,190),(560,190),(610,190),(510,240),(560,240),(610,240),(510,290),(560,290),(610,290)]
topFace=[(190,30),(240,30),(290,30),(190,80),(240,80),(290,80),(190,130),(240,130),(290,130)]
bottomFace=[(190,350),(240,350),(290,350),(190,400),(240,400),(290,400),(190,450),(240,450),(290,450)]

font=pygame.font.Font("freesansbold.ttf",32)
font1=pygame.font.Font("freesansbold.ttf",20)
def rotation(spin):
    global front, right, back, left, top, bottom
    if spin=="clockwise":
        temp=front
        front=right
        right=back
        back=left
        left=temp
        temp=[top[6],top[3],top[0],top[7],top[4],top[1],top[8],top[5],top[2]]
        top=temp
        temp=[bottom[2],bottom[5],bottom[8],bottom[1],bottom[4],bottom[7],bottom[0],bottom[3],bottom[6]]
        bottom=temp
    elif spin=="anticlockwise":
        rotation("clockwise")
        rotation("clockwise")
        rotation("clockwise")
def move(m):
    global front, right, back, left, bottom, top
    if m==1:   #1 is for R
        temp=[front[2],front[5],front[8]]
        front[2],front[5],front[8]=bottom[2],bottom[5],bottom[8]
        bottom[2],bottom[5],bottom[8]=back[6],back[3],back[0]
        back[0],back[3],back[6]=top[8],top[5],top[2]
        top[2],top[5],top[8]=temp[0],temp[1],temp[2]
        temp=[right[6],right[3],right[0],right[7],right[4],right[1],right[8],right[5],right[2]]
        right=temp
    elif m==2:  #2 is for R prime
        move(1)
        move(1)
        move(1)
    elif m==5: #5 is for U
        temp=[front[0],front[1],front[2]]
        front[0],front[1],front[2]=right[0],right[1],right[2]
        right[0],right[1],right[2]=back[0],back[1],back[2]
        back[0],back[1],back[2]=left[0],left[1],left[2]
        left[0],left[1],left[2]=temp[0],temp[1],temp[2]
        temp=[top[6],top[3],top[0],top[7],top[4],top[1],top[8],top[5],top[2]]
        top=temp
    elif m==6:  #6 is for U prime
        move(5)
        move(5)
        move(5)
    elif m==7:  #7 is for B
        rotation("clockwise")
        move(2)
        rotation("anticlockwise")
    elif m==8:  #8 is for B prime
        rotation("clockwise")
        move(1)
        rotation("anticlockwise")
    elif m==3:  #3 is for F
        rotation("anticlockwise")
        move(1)
        rotation("clockwise")
    elif m==4:  #4 is for F prime
        rotation("anticlockwise")
        move(2)
        rotation("clockwise")
def background():
    global width, height
    screen.fill((0,255,255))
    #borders
    linecolor=(48,144,144)
    pygame.draw.rect(screen,linecolor,[0,0,width,10])
    pygame.draw.rect(screen,linecolor,[0,0,10,height])
    pygame.draw.rect(screen,linecolor,[width-10,0,10,height])
    pygame.draw.rect(screen,linecolor,[0,height-10,width,10])
    #moves box
    pygame.draw.rect(screen,(31,36,36),[670,70,100,100])
def cube():
    global front, right, back, left, bottom, top, topFace, frontFace, rightFace, backFace, leftFace, bottomFace
    Face=[front, right, back, left, bottom, top]
    Cordinates=[frontFace,rightFace,backFace,leftFace,bottomFace,topFace]
    for i in range(0,6):
        for j in range(0,9):
            if Face[i][j] in range(1,10):
                color="red"
            elif Face[i][j] in range(10,19):
                color="green"
            elif Face[i][j] in range(19,28):
                color=(255,115,0)
            elif Face[i][j] in range(28,37):
                color="blue"
            elif Face[i][j] in range(37,46):
                color="white"
            elif Face[i][j] in range(46,55):
                color="yellow"
            pygame.draw.rect(screen,color,[Cordinates[i][j][0]+2,Cordinates[i][j][1]+2,48,48])
def write(m):
    #to blit the name of the move taken in the screen
    text1=font1.render("Last Move",True,"black")
    if m!="none":
        text=font.render(m,True,"white")
        screen.blit(text,[670+50-16,70+50-16])
    screen.blit(text1,[670,70-25])
m="none"
running = True
while running:
    background()
    cube()
    write(m)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                move(1)
                m="R"           
            elif event.key==pygame.K_2:
                move(2)
                m="R!"       
            elif event.key==pygame.K_3:
                move(3)
                m="F"
            elif event.key==pygame.K_4:
                move(4)
                m="F!"
            elif event.key==pygame.K_5:
                move(5)
                m="U"
            elif event.key==pygame.K_6:
                move(6)
                m="U!"
            elif event.key==pygame.K_7:
                move(7)
                m="B"
            elif event.key==pygame.K_8:
                move(8)
                m="B!"
            elif event.key==pygame.K_LEFT:
                rotation("anticlockwise")
                m="<--"
            elif event.key==pygame.K_RIGHT:
                rotation("clockwise")
                m="-->"
    clock.tick(20)
    pygame.display.update()
pygame.quit()