import os
from gtts import gTTS
import pygame
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
from encrypt import decrypt
import help_com as hc

def sweep_waste():
    dir_name = r"C:\Users\Pavilion\Documents\SCARLETT v2.0\\"
    for waste_mp3 in os.listdir(dir_name):
        if(waste_mp3.endswith(".mp3")):
            os.remove(os.path.join(dir_name, waste_mp3))

def audio(message):
    myobj = gTTS(text=message, lang='en', slow=False)
    seed = random.randint(100,1000)
    filename = "welcome" + str(seed) + ".mp3"
    myobj.save(filename)
    pygame.mixer.init(26000)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def scan_loc():
    location = input("Which location you want to scan: ")
    if(location == "desktop"):
        root = r"C:\Users\Pavilion\Desktop"
    elif(location == "downloads"):
        root = r"C:\Users\Pavilion\Downloads"
    elif(location == "entertainment"):
        root = r"F:"
    elif(location == "work"):
        root = r"G:"
    for folder in os.listdir(root):
        print(folder)
    audio(str(len(os.listdir(root))) + " files and folders.")

def web_host():
    audio("Accessing you web hosting package")
    browser = webdriver.Chrome("C:\chromedriver.exe")
    browser.get('https://www.ecowebhosting.co.uk/cp/login')
    email = browser.find_element_by_id('loginemail')
    email.send_keys('sdharchoupsg2016@gmail.com')
    password = browser.find_element_by_id('loginpassword')
    password.send_keys(decrypt("ubzvu^opka2.B"))
    browser.find_element_by_class_name('btn-green').click()

def php_myadmin():
    audio("Accessing localhost database")
    browser = webdriver.Chrome("C:\chromedriver.exe")
    browser.get('http://localhost/phpmyadmin/')
    username = browser.find_element_by_id('input_username')
    username.send_keys('root')
    password = browser.find_element_by_id('input_password')
    password.send_keys(decrypt('r^upyltaB'))
    browser.find_element_by_id('input_go').click()

sweep_waste()
while(1):
    command = input("How may I help you? ")
    if(command == "scan"):
        scan_loc()
    elif(command == "bye"):
        print("Bye bye")
        audio("Bye bye")
        break
    elif(command == "whost"):
        web_host()
    elif(command == "pma"):
        php_myadmin()
    elif(command == "?"):
        hc.help_com()
    elif(command == "sab"):
        hc.all_com()
    elif("hc/" in command):
        command = command.split("/")
        hc.hc(command[1])
    elif(command == "xampp"):
        audio("Starting zamp server")
        location = r'C:\xampp\xampp_start.exe'
        os.system(location)
    else:
        audio("I do not understand what you said")
os.system("say 'hello world'")
