import pygame
import pyautogui as auto
seconds=int(input("\n\nEnter in seconds (recommended less than 60):: "))
pygame.init()
clock=pygame.time.Clock()
width=400
height=300
size=auto.size()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Said you to wait')
font=pygame.font.Font("freesansbold.ttf", 32)
running = True
def displaytime(seconds):
    pygame.draw.rect(screen, "aquamarine3", [140,90,100,50])
    minute=int((seconds-seconds%60)/60)
    seconds%=60
    hour=int((minute-minute%60)/60)
    minute%=60
    if hour<0:
        return False
    hms=f"{hour}:{minute}:{int(seconds)}"
    waittext=font.render("WAIT FOR:::", True, "red")
    timerset=font.render(hms, True, "red")
    screen.blit(timerset, (150,100))
    screen.blit(waittext,(100,50))
while running:
    auto.moveTo(int(size[0]/2),int(size[1]/2),0)
    screen.fill("grey")
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            running=False
    if displaytime(seconds)==False:
        running=False
    seconds-=1/10
    clock.tick(1*10)
    pygame.display.update()
pygame.quit()
