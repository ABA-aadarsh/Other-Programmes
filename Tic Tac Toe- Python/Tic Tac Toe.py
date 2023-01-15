import pygame
import random
pygame.init()
global bg_color, l_color, XO_list, position_left,  CheckList,WINLINE
WINLINE=(0,0)
bg_color="aquamarine3"
l_color="cadetblue4"
CheckList=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
a=9
b=188
Centre=[((2*a+b)/2,(2*a+b)/2),((4*a+3*b)/2,(2*a+b)/2),((6*a+5*b)/2,(2*a+b)/2),
((2*a+b)/2,(4*a+3*b)/2),((4*a+3*b)/2,(4*a+3*b)/2),((6*a+5*b)/2,(4*a+3*b)/2),
((2*a+b)/2,(6*a+5*b)/2),((4*a+3*b)/2,(6*a+5*b)/2),((6*a+5*b)/2,(6*a+5*b)/2)]
def call(i):
    XO_list[i]="O"
    position_left.remove(i)
def draw_background():
    screen.fill(bg_color)
    a=9
    b=188
    pygame.draw.rect(screen, l_color, [0,0,a,height])
    pygame.draw.rect(screen,l_color,[a+b,0,a,height])
    pygame.draw.rect(screen, l_color, [2*a+2*b,0,a,height])
    pygame.draw.rect(screen, l_color, [3*a+3*b,0,a,height])
    pygame.draw.rect(screen, l_color, [0,0,width,a])
    pygame.draw.rect(screen,l_color,[0,a+b,width,a])
    pygame.draw.rect(screen, l_color, [0,2*a+2*b,width,a])
    pygame.draw.rect(screen, l_color, [0,3*a+3*b,width, a])
def player(x,y):
    a=9
    b=188
    if (x in range(a,a+b)) and (y in range(a,a+b)) and XO_list[0]==" ":
        call(0)
    elif (x in range(2*a+b,2*a+2*b)) and (y in range(a,a+b)) and XO_list[1]==" ":
        call(1)
    elif (x in range(3*a+2*b,3*a+3*b)) and (y in range(a,a+b)) and XO_list[2]==" ":
        call(2)
    elif (x in range(a,a+b)) and (y in range(2*a+b,2*a+2*b)) and XO_list[3]==" ":
        call(3)
    elif (x in range(2*a+b,2*a+2*b)) and (y in range(2*a+b,2*a+2*b)) and XO_list[4]==" ":
        call(4)
    elif (x in range(3*a+2*b,3*a+3*b)) and (y in range(2*a+b,2*a+2*b)) and XO_list[5]==" ":
        call(5)
    elif (x in range(a,a+b)) and (y in range(3*a+2*b,3*a+3*b)) and XO_list[6]==" ":
        call(6)
    elif (x in range(2*a+b,2*a+2*b)) and (y in range(3*a+2*b,3*a+3*b)) and XO_list[7]==" ":
        call(7)
    elif (x in range(3*a+2*b,3*a+3*b)) and (y in range(3*a+2*b,3*a+3*b)) and XO_list[8]==" ":
        call(8)
    else:
        return False
    return True
def computerIntellec(runtime,firstTurn):
    if runtime==1:
        if firstTurn=="O":
            temp=0
            for i in position_left:
                temp+=i
            player1stposition=36-temp
            if player1stposition==4:
                print("yes")
                computerchoose(0)
            else:
                computerchoose(4)
        else:
            computerchoose(4)
    else:
        CA=checkAttack()
        if CA==0:
            CD=checkDefense()
            if CD==0 :
                makeMove()
def computerchoose(position):
    XO_list.pop(position)
    XO_list.insert(position,"X")
    position_left.remove(position)
def hunt(numList,priority1,priority2):
    n1=numList[0]
    n2=numList[1]
    n3=numList[2]
    XO1=XO_list[n1]
    XO2=XO_list[n2]
    XO3=XO_list[n3]
    z=[XO1,XO2,XO3,n1,n2,n3]
    if z.count(priority1)==2 and z.count(priority2)==1:
        return z[z.index(" ")+3]
    else:
        return "Nope"
def checkAttack():
    if hunt( CheckList[0], "X", " ")!="Nope":
        computerchoose(hunt( CheckList[0], "X", " "))
    elif hunt(CheckList[1],"X"," ")!="Nope":
        computerchoose(hunt(CheckList[1],"X"," "))
    elif hunt(CheckList[2],"X"," ")!="Nope":
        computerchoose(hunt(CheckList[2],"X"," "))
    elif hunt(CheckList[3],"X"," ")!="Nope":
        computerchoose(hunt(CheckList[3],"X"," "))
    elif hunt(CheckList[4],"X"," ")!="Nope":
        computerchoose(hunt(CheckList[4],"X"," "))
    elif hunt(CheckList[5],"X"," ")!="Nope":
        computerchoose(hunt(CheckList[5],"X"," "))
    elif hunt(CheckList[6],"X"," ")!="Nope":
        computerchoose(hunt(CheckList[6],"X"," "))
    elif hunt(CheckList[7],"X"," ")!="Nope":
        computerchoose(hunt(CheckList[7],"X"," "))
    elif (XO_list[5]=="O" and XO_list[7]=="O" and XO_list[8]==" " and XO_list[6]==" "):
        computerchoose(8)
    elif XO_list[4]=="X" and (XO_list[1]=="O" or XO_list[3]=="O" or XO_list[5]=="O"or XO_list[7]=="O") and (XO_list[0]==" " and XO_list[2]==" " and XO_list[6]==" " and XO_list[8]==" "):
        computerchoose(0)
    else:
        return 0
    return 1
def checkDefense():
    if hunt( CheckList[0], "O", " ")!="Nope":
        computerchoose(hunt( CheckList[0], "O", " "))
    elif hunt(CheckList[1],"O"," ")!="Nope":
        computerchoose(hunt(CheckList[1],"O"," "))
    elif hunt(CheckList[2],"O"," ")!="Nope":
        computerchoose(hunt(CheckList[2],"O"," "))
    elif hunt(CheckList[3],"O"," ")!="Nope":
        computerchoose(hunt(CheckList[3],"O"," "))
    elif hunt(CheckList[4],"O"," ")!="Nope":
        computerchoose(hunt(CheckList[4],"O"," "))
    elif hunt(CheckList[5],"O"," ")!="Nope":
        computerchoose(hunt(CheckList[5],"O"," "))
    elif hunt(CheckList[6],"O"," ")!="Nope":
        computerchoose(hunt(CheckList[6],"O"," "))
    elif hunt(CheckList[7],"O"," ")!="Nope":
        computerchoose(hunt(CheckList[7],"O"," "))
    elif XO_list[4]=="O" and XO_list[8]=="O" and XO_list[0]=="X" and XO_list.count(" ")==6:
        computerchoose(6)
    elif XO_list[5]==" " and XO_list[8]==" " and XO_list[2]=="O" and XO_list[7]=="O" and len(position_left)>2:
        computerchoose(8)
    elif XO_list[5]=="O" and XO_list[6]=="O" and XO_list[7]==" " and XO_list[8]==" " and XO_list[2]==" ":
        computerchoose(8)    
    else:
        return 0
    return 1
def makeMove():
    if hunt( CheckList[0], " ", "X ")!="Nope":
        computerchoose(hunt( CheckList[0], " ", "X"))
    elif hunt(CheckList[1]," ","X")!="Nope":
        computerchoose(hunt(CheckList[1]," ","X"))
    elif hunt(CheckList[2]," ","X")!="Nope":
        computerchoose(hunt(CheckList[2]," ","X"))
    elif hunt(CheckList[3]," ","X")!="Nope":
        computerchoose(hunt(CheckList[3]," ","X"))
    elif hunt(CheckList[4]," ","X")!="Nope":
        computerchoose(hunt(CheckList[4]," ","X"))
    elif hunt(CheckList[5]," ","X")!="Nope":
        computerchoose(hunt(CheckList[5]," ","X"))
    elif hunt(CheckList[6]," ","X")!="Nope":
        computerchoose(hunt(CheckList[6]," ","X"))
    elif hunt(CheckList[7]," ","X")!="Nope":
        computerchoose(hunt(CheckList[7]," ","X"))
    else:
        c=random.randint(0,len(position_left)-1)
        XO_list.pop(position_left[c])
        XO_list.insert(position_left[c],"X")
        position_left.pop(c)
def check(list,XO):
    if XO_list[list[0]]==XO and XO_list[list[1]]==XO and XO_list[list[2]]==XO:
        return True
    return False
def result(XO):
    global WINLINE
    Flag=False
    for i in range(8):
        Flag=check(CheckList[i],XO)
        if Flag==True:
            WINLINE=(CheckList[i][0],CheckList[i][2])
            return "WON"
            break
    return "NOT WON"
def display_result(char):
    pygame.draw.rect(screen, l_color, [165,220,300,100])
    text=font.render(char, True, "white")
    screen.blit(text, (175,250))
    #For play again button
    pygame.draw.rect(screen,"aquamarine4",[215,350,200,60])
    play_again=font.render("Play again", True, "white")
    screen.blit(play_again,[230,365])
clock=pygame.time.Clock()
fps=20
width=600
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Tic Tac Toe')
font=pygame.font.Font("freesansbold.ttf",32)
firstTurn,turn,runtime,counter,gameover,XO_list,position_left=0,0,0,0,0,0,0
def begin():
    global runtime, counter, gameover, firstTurn, turn, XO_list, position_left, WINLINE
    firstTurn=random.choice(["X","O"])
    if firstTurn=="X":
        turn="XO"
    else:
        turn="OX"
    runtime=1
    counter=0
    gameover=False
    XO_list=[" "," "," "," "," "," "," "," "," "]
    position_left=[0,1,2,3,4,5,6,7,8]
    WINLINE=(0,0)
begin()
running=True
while running:
    draw_background()
    for i in range(9):
        if XO_list[i]=="X":
            pygame.draw.line(screen,l_color,(Centre[i][0]-50,Centre[i][1]-50),(Centre[i][0]+50,Centre[i][1]+50),7)
            pygame.draw.line(screen,l_color,(Centre[i][0]+50,Centre[i][1]-50),(Centre[i][0]-50,Centre[i][1]+50),7)
        elif XO_list[i]=="O":
            pygame.draw.circle(screen, (210,210,210), Centre[i], 50, 7)
    if WINLINE!=(0,0):
        pygame.draw.line(screen, (50,50,50), (Centre[WINLINE[0]][0],Centre[WINLINE[0]][1]), (Centre[WINLINE[1]][0],Centre[WINLINE[1]][1]),10)
    if turn[counter%2]=="X" and position_left!=[]:
        computerIntellec(runtime, firstTurn)
        runtime=0
        counter+=1
    if result("X")=="WON":
        gameover=True
        display_result("COMPUTER WON")
    elif result("O")=="WON":
        gameover=True
        display_result("PLAYER WON")
    elif len(position_left)==0:
        gameover=True
        display_result("         DRAW")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN and gameover==False:
            if turn[counter%2]=="O":
                mouse=pygame.mouse.get_pos()
                if player(mouse[0], mouse[1])==True:
                    counter+=1
                    result("O")
        if event.type==pygame.MOUSEBUTTONDOWN and  gameover==True:
            mouse=pygame.mouse.get_pos()
            if mouse[0] in range(215,215+200) and mouse[1] in range(350,350+60):
                begin()
    clock.tick(fps)
    pygame.display.update()
pygame.quit()
exit()
