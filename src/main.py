import os
import json
import time
from add import add
from game import game

dt = "dictionary.json"

if not os.path.exists(dt):
    with open(dt, "w", encoding="utf-8") as f:
        f.write("{}")

print("1- baslat")
print("2- sozluge ekle")
decision = int(input(": "))

if decision == 1:
    os.system("clear")
    game()

elif decision == 2:
    os.system("clear")

    print("eklemek istedigin seviyeyi sec\n1- a1\n2- a2\n3- b1\n4- b2\n5- c1\n6- c2")
    decision = input(": ")
    os.system("clear")

    eng = input("sozluge eklenecek ingilizce sozcuk : ")
    tr = input("turkce karsılıgı : ")

    add(eng,tr,decision)