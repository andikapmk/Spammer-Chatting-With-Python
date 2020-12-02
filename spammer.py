import time
import pyautogui
print("SPAMMER CHATTING BY ANDIKAPMK")
print("")
pesan = input("masukan pesan yang akan di kirim : ")
jumlah = int(input("masukan jumlah pesan : "))

time.sleep(2)

for i in range(jumlah):
    pyautogui.typewrite(pesan + "\n")
print("")
print("spam selesai")
