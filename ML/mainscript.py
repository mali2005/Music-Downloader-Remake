import os
import random
import time
from pathlib import Path

def mp3counter():
    count = 0
    for file in os.listdir(str(Path.home())+"//Downloads"):
        if file.endswith(".mp3"):
            count+=1
    return count
os.system("color a")
while True:


    print("Print Your Music Name:")
    
    
    a = str(input("Over Here: "))
    
    text = open(".//data//scripts//searching.txt","w",encoding="utf-8")
    text.write(a)
    text.close()   
    os.system("start downloader.pyw")

    truth = mp3counter()
    files = truth

    os.system("cls")

    while files == truth:
        files = mp3counter()
        print("Your download has started. Pls wait.")
        print("."*random.randint(1,4))
        time.sleep(0.1)
        os.system("cls")