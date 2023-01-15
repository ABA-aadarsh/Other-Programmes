import pyautogui as  auto
import time
surity=input("Are You Sure? (yes(y)/no(n)) : ")
if surity=="y":
    time.sleep(1)
    #(26,751)
    auto.moveTo(26,751, 2)
    time.sleep(1)
    auto.click(26, 751, 1, 1, button="left")
    time.sleep(2)
    #(297, 694)
    auto.moveTo(297,694, 1)
    auto.click(297,694, 1 , 1, button="left")
else:
    pass
exit()
