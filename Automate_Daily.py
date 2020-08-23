import time
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Automation:
    def weather(self):
        #Opening chrome browser in icognito mode
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver=webdriver.Chrome(options=options)
        
        driver.get("https://www.google.com")
        #Change into English version of Google
        try:
            driver.find_element_by_xpath("//*[@id='SIvCob']/a").click()
        except:
            'no need to change as Google is already in its English form'
        
        #Search for weather in city and retrieve data from Google's top result
        search_bar=driver.find_element_by_xpath("//input[@title='Search']")
        search_bar.send_keys("alexandria weather", Keys.ENTER)
        temperature="Temperature is "+driver.find_element_by_id("wob_tm").text+" degrees Celsius"
        precipitation=" Precipitation is "+driver.find_element_by_id("wob_pp").text
        humidity=" Humidity is "+driver.find_element_by_id("wob_hm").text
        wind=" Wind speed is "+driver.find_element_by_id("wob_ws").text
        
        full_temperature=temperature+precipitation+humidity+wind
        
        #Opening text reader to play the weather report out loud
        driver.get("https://ttsreader.com/")
        text_box=driver.find_element_by_id("text_box")
        text_box.clear()
        text_box.send_keys(full_temperature)
        driver.find_element_by_id("speak_button_new").click()
        #Give time for the weather report to be fully read out
        time.sleep(10)
        self.music()
        
    def music(self):
        #Open Spotify app to play music
        os.startfile("C:\\Users\\Nouh\\AppData\\Roaming\\Spotify\\Spotify.exe")    
#Run the script
Automate=Automation()
Automate.weather()