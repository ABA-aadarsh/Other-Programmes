# lets create a 6X6 grid where marbles are made to move to the available direction randomly
import pygame
import random
pygame.init()
clock=pygame.time.Clock()
fps=15
WindowSize=(600,600)
screen=pygame.display.set_mode(WindowSize)
pygame.display.set_caption("Simple marble simulation")
#Marbles
a=24
b=72
def background():
    global a, b
    screen.fill("white")
    line_color="aquamarine3"
    #Vertical lines
    for i in range(0,7):
        pygame.draw.rect(screen, line_color, [i*(a+b),0,a,600])
    #Horizontal lines
    for i in range(0,7):
        pygame.draw.rect(screen, line_color, [0,i*(a+b),600,a])
num_marbles=9
centerlist=[]
truelist=[]
marble_position=[]
for i in range(36):
    truelist.append(False)
for i in range(1,7):
    centerlist.append([int(a+(b)/2),int(i*a+(2*i-1)*b/2)])
    centerlist.append([int(2*a+3*(b)/2),int(i*a+(2*i-1)*b/2)])
    centerlist.append([int(3*a+5*(b)/2),int(i*a+(2*i-1)*b/2)])
    centerlist.append([int(4*a+7*(b)/2),int(i*a+(2*i-1)*b/2)])
    centerlist.append([int(5*a+9*(b)/2),int(i*a+(2*i-1)*b/2)])
    centerlist.append([int(6*a+11*(b)/2),int(i*a+(2*i-1)*b/2)])
#Setting marble position randomly
for i in range(num_marbles):
    while True:
        p=random.randint(0, 35)
        if truelist[p]==False:
            truelist[p]=True
            marble_position.append(p)
            break
counter=0
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #Background
    background()
    #displaying marbles in the grid
    for i in range(0,36):
        if truelist[i]==True:
            pygame.draw.circle(screen, "gold", centerlist[i], (b/2)-2)
    #for random movement of the marble
    if counter%5==0:
        index=random.choice(marble_position)
        pygame.draw.circle(screen,"green",centerlist[index],(b/2)-2)
        validposition=[]
        for i in [1,-1,6,-6]:
            x=i+index
            if x in range(0,36) and truelist[x]==False:
                if i==1 or i==-1:
                    if centerlist[index][1]==centerlist[x][1]:
                        validposition.append(x)
                else:
                    validposition.append(x)
        if len(validposition)!=0 :
            position=random.choice(validposition)
            truelist[index]=False
            truelist[position]=True
            marble_position[marble_position.index(index)]=position
    counter+=1

    clock.tick(fps)
    pygame.display.update()
pygame.quit()
exit()