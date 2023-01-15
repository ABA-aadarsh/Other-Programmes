import pygame
import random
pygame.init()
clock=pygame.time.Clock()
fps=25
fontsize=40
font=pygame.font.Font("freesansbold.ttf", fontsize)
Window=(500,400)
screen=pygame.display.set_mode(Window)
pygame.display.set_caption('Are you dumb??')

#Buttons
yesbutton=[100,300]
nobutton=[300,300]
Yes=font.render("Yes", True, "black")
No=font.render("No",True,"black")
button_lb=[80,40]

running = True
state=False     #this will help us to determine which of the background to display
def background(state):
    if state==False:
        global yesbutton, nobutton, button_lb
        text=font.render("Are you dumb?", True, "black")
        screen.blit(text, [125,70])
        #Button box
        pygame.draw.rect(screen, "black", [yesbutton[0],yesbutton[1],button_lb[0],button_lb[1]],3)
        pygame.draw.rect(screen, "black", [nobutton[0],nobutton[1],button_lb[0],button_lb[1]],3)
        #Button text
        screen.blit(Yes, [yesbutton[0]+6,yesbutton[1]+5])
        screen.blit(No, [nobutton[0]+15,nobutton[1]+5])
        #hovering effect
        temp_mp=pygame.mouse.get_pos()
        if temp_mp[0] in range(nobutton[0],nobutton[0]+button_lb[0]) and temp_mp[1] in range(nobutton[1],nobutton[1]+button_lb[1]):
            pygame.draw.rect(screen,"blue",[nobutton[0]+2,nobutton[1]+2,button_lb[0]-2,button_lb[1]-2],2)
        if temp_mp[0] in range(yesbutton[0],yesbutton[0]+button_lb[0]) and temp_mp[1] in range(yesbutton[1],yesbutton[1]+button_lb[1]):
            pygame.draw.rect(screen,"blue",[yesbutton[0]+2,yesbutton[1]+2,button_lb[0]-2,button_lb[1]-2],2)
    else:
        text=font.render("I knew it :3",True,"black")
        screen.blit(text, [165,150])
def buttonslogic(mouseposition):
    global yesbutton, nobutton, button_lb, Window
    if int(mouseposition[0]) in range(yesbutton[0],yesbutton[0]+button_lb[0]) and int(mouseposition[1]) in range(yesbutton[1],yesbutton[1]+button_lb[1]):
        #Yes button is pressed
        global state
        state=True
    elif int(mouseposition[0]) in range(nobutton[0],nobutton[0]+button_lb[0]) and int(mouseposition[1]) in range(nobutton[1],nobutton[1]+button_lb[1]):
        #No button is pressed
        nobutton[0]=random.randint(yesbutton[0]+button_lb[0]+5, Window[0]-button_lb[0])
        nobutton[1]=random.randint(70+fontsize+5,Window[1]-button_lb[1])

while running:
    #For background
    screen.fill("white")
    background(state)
    for event in pygame.event.get():
        if event.type==pygame.QUIT and state==True:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouseposition=pygame.mouse.get_pos()
            buttonslogic(mouseposition)
    clock.tick(fps)
    pygame.display.update()
pygame.quit()