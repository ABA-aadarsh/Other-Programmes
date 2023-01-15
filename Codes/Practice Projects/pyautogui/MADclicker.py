import pyautogui as auto
import time
no_of_clicks=int(input("Enter the number of clicks: "))
time.sleep(10)
counter=0
while counter<=no_of_clicks:
    position=auto.position()
    auto.click(position.x, position.y, 1, 0.1, button="left")
    time.sleep(0.1)
    counter+=1
exit()

