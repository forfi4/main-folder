import pyautogui
from time import sleep

time = 0   
while time != 10:
    time += 1
    sleep(1)
    print("spammer waiting..." + str(time))

def spam(msg, maxMsg):
    count = 0

    while count != maxMsg:
        count += 1
        print("send message: " + str(count))
        pyautogui.write(msg)
        pyautogui.press("enter")
        if count == 1000:
            sleep(8)

spam("NIGGER",100)  
