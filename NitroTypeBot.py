import time as t
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from seleniumbase import Driver

username = "YOUR_USERNAME_GOES_HERE"
password = "YOUR_PASSWORD_GOES_HERE"


driver = Driver(
        browser="chrome",
        uc=True,
        headless2=False,
        incognito=True,
        agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36 AVG/112.0.21002.139",
        do_not_track=True,
        undetectable=True
    )
options = webdriver.ChromeOptions() 
options.add_argument('--lang=en')  
options.add_argument('log-level=3')  
options.add_argument('--mute-audio') 
driver.maximize_window()  
driver.get('https://www.nitrotype.com/login')

def human_type(element, text):
    for char in text:
        t.sleep(random.randint(1,2))
        element.send_keys(char)

while True:
    try:
        elm = driver.find_element(by=By.XPATH,value="/html/body/div/div/div/main/div/section/div[2]/div/div[3]/form/div[1]/div[1]/div[2]/input")
        human_type(elm,username)
        print("Username")
        break
    except:
        continue
el = driver.find_element(by=By.XPATH,value="/html/body/div/div/div/main/div/section/div[2]/div/div[3]/form/div[1]/div[2]/div[2]/input")
human_type(el,password)
print("Password")
driver.find_element(by=By.XPATH,value="/html/body/div/div/div/main/div/section/div[2]/div/div[3]/form/button").click()
print("Login")
while True:
    try:
        if driver.current_url == "https://www.nitrotype.com/garage":
            print("In Garage")
            break
    except:
        continue
actions = ActionChains(driver)
while True:
    print("New Race")
    driver.get("https://www.nitrotype.com/race")
    while True:
        try:                                             
            text =driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/main/div/section/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/span[1]/span[1]").text
            print("Race Started")
            break
        except:
            continue
    whole_sentance = ""
    for word in range(1,500):
        try:                                                         
            driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/main/div/section/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/span[{word}]/span[1]")
        except:
            break
        for letter in range(1,30):
            try:                                                 
                letter =driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/main/div/section/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/span[{word}]/span[{letter}]").get_attribute('textContent')
                if letter == "\u00a0":
                    actions.key_down(" ").key_up(" ").perform()
                else: 
                    actions.key_down(letter).perform()
                    actions.key_up(letter).perform()
                # you can control the speed by changing the number, higher is slower.
                t.sleep(0.05)
                # print(letter)
                whole_sentance += letter
            except:
                break
    print(whole_sentance)
    t.sleep(5)
t.sleep(1000)
