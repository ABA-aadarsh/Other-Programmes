import pyautogui as auto
spamText=input("Spam Text: ")
while True:
    auto.typewrite(spamText)
    auto.press('enter')
    
