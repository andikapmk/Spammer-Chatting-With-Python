import time
import pyautogui

pesan = "sayang"
jumlah = 50

time.sleep(2)

for i in range(jumlah):
    pyautogui.typewrite(pesan + "\n")
