from selenium import webdriver
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import os
from pathlib import Path
import youtube_dl


def mp3counter():
    count = 0
    for file in os.listdir(str(Path.home())+"//Downloads"):
        if file.endswith(".mp3"):
            count+=1
    return count


settings = webdriver.ChromeOptions()
settings.add_argument("--log-level=3")

service = Service(".//chromedriver.exe")
service.creationflags = CREATE_NO_WINDOW

downloader = webdriver.Chrome(".//chromedriver.exe",chrome_options=settings)

script = open(".//data//scripts//searching.txt","r",encoding="utf-8").read()

script.replace(" ","+")

downloader.get("https://www.youtube.com/results?search_query="+script)
title = downloader.find_element_by_id("video-title")
link = title.get_attribute("href")

downloader.get("https://mp3y.download/tr/fast-mp3-convert")

downloader.find_element_by_name("url").send_keys(link+Keys.RETURN)

dongu = True
while dongu == True:
    try:
        downloader.find_element_by_xpath("/html/body/main/section[2]/div/article/div/p[2]/button").click()
        dongu = False
    except:
        pass

parent = downloader.window_handles[0]
downloader.switch_to.window(parent)
time.sleep(1)
downloader.find_element_by_xpath("/html/body/main/section[2]/div/article/div/p[2]/a").click()

truth = mp3counter()
files = truth

print("Started")
while files == truth:
    files = mp3counter()
print("finished")
downloader.quit()
