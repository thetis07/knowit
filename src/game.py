import json
import time
import random
import os

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
            print(f"gelen kelime: {choosen}")
            response = input(": ")

            if response.lower().strip() == answer:
                print("hll bildin!")
            elif response.lower().strip() != answer:
                print(f"bilemedin ez, cevap: {answer}")
            
            sentences.remove(choosen)

            time.sleep(0.8)
            os.system("clear")

        except IndexError:
            print("butun kelimeler bitti.")
            time.sleep(1)
            break