# Morte Carlo Simulator for Pi estimation
import pygame
import random
pygame.init()
clock=pygame.time.Clock()
fps=10  #For speed no of fps here determine the number of points in 1 secondwhite


WindowSize=(800,600)
screen=pygame.display.set_mode(WindowSize)
pygame.display.set_caption("MC Simulator: PI")
nc,t=0,0
lst=[]
#Square
#800-2*a=600-2*b
a=150
b=50
l=800-2*a
c=0
font=pygame.font.Font("freesansbold.ttf", 32)
fps_text=font.render(f"FPS:{fps}", True, "red")
def square_circle():
    global a,b, l
    pygame.draw.rect(screen, "white", [a,b,l,l],2)
    #Circle
    pygame.draw.circle(screen, "white",[a+l/2,b+l/2],l/2,2)
def pi_display(nc,t):
    global WindowSize, a
    # x=nc/ns
    # epi=(4*x)/(x+1)
    x=nc/t
    epi=4*x
    text=font.render(f"PI~{epi}", True, "white")
    text1=font.render("For increasing speed increase fps value",True,"white")
    screen.blit(text, [WindowSize[0]-500,10])
    screen.blit(text1, [a-100,WindowSize[1]-50])
running=True
while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    square_circle()
    for i in range(50):
        x=random.randint(a,a+l)
        y=random.randint(b,b+l )
        r=pow(x-(a+l/2), 2)+pow(y-(b+l/2), 2)
        r=pow(r,0.5)
        if r<=(l/2):
            nc+=1
            lst.append(["c",x,y])
        else:
            lst.append(["s",x,y])
        t+=1  
    for point in lst:
        if point[0]=="c":
            pygame.draw.circle(screen, "yellow", point[1:], 3)
        else:
            pygame.draw.circle(screen,"green",point[1:],3)
    pi_display(nc,t)
    screen.blit(fps_text, [0,50])
    c+=1
    clock.tick(fps)
    pygame.display.update()
pygame.quit()