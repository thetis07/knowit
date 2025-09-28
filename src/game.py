import json
import time
import random
import os
from colorama import Fore, Style

dt = "dictionary.json"

def game():
    with open(dt, "r") as f:
        source = json.load(f)
        
    print("seviyeni sec\n1- a1\n2- a2\n3- b1\n4- b2\n5- c1\n6- c2")
    decision = input(": ")

    sentences_get = source.get(decision)
    sentences = []
    for i in sentences_get:
        sentences.append(i)
    
    os.system("clear")

    while True:
        try:
            choosen = random.choice(sentences)
            answer = sentences_get.get(choosen)
            print(f"gelen kelime: {Fore.BLUE} {choosen}")
            response = input(f"{Style.RESET_ALL}: {Fore.RED}")
            print(Style.RESET_ALL, end="")

            if response.lower().strip() == answer:
                print("hll bildin!")
            elif response.lower().strip() != answer:
                print(f"bilemedin ez, cevap: {Fore.GREEN}{answer}")
                print(Style.RESET_ALL, end="")
            
            sentences.remove(choosen)

            time.sleep(0.8)
            os.system("clear")

        except IndexError:
            print("butun kelimeler bitti.")
            time.sleep(1)
            break