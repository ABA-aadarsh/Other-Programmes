import speech_recognition as sr
import time
import pyautogui as auto
voice_recognizer=sr.Recognizer()
translated="!"
with sr.Microphone() as MC:
    while True and translated!="code kill it":
        try:
            print("::")
            audio_data=voice_recognizer.listen(MC)
            translated=voice_recognizer.recognize_google(audio_data)
            translated=translated.lower()
            if translated=="hang on the program":
                print("Sleeping for 10 seconds")
                time.sleep(10)
                print("Woke up")
                time.sleep(1)
            elif translated =="take a screenshot":
                print("Taking Screenshot of current window")
                auto.screenshot("screenshot.png")
            else:
                print(translated)
        except:
            print("Error\n")
