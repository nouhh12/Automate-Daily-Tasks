import time
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Automation:
    def music(self):
        #Open Spotify app to play music
        os.startfile("C:\\Users\\Nouh\\AppData\\Roaming\\Spotify\\Spotify.exe")
        #Go to the next step which is the audible weather report
        self.weather()
        
    def weather(self):
        driver.get("https://www.google.com")
        #Change into English version of Google
        try:
            driver.find_element_by_xpath("//*[@id='SIvCob']/a").click()
        except:
            'no need to change as Google is already in its English form'
        #Insert the city you want to check the weather in
        desired_city="alexandria"
        #Search for weather in city and retrieve data from Google's top result
        search_bar=driver.find_element_by_xpath("//input[@title='Search']")
        search_bar.send_keys(desired_city+" weather", Keys.ENTER)
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
        word_count=len(full_temperature.split())
        #Give time for the weather report to be fully read out by dividing the word count by 5, 
        #given that the average speed for reading out loud is 5 words per second
        time.sleep(word_count/5)
        #Go to the final step which is reading the emails out loud
        self.email()
        
    def email(self):
        #Insert your email and password for Microsoft Outlook
        my_email=""
        my_password=""
        driver.get("https://outlook.live.com/owa/")
        #Inserting email and password to sign in
        driver.find_element_by_xpath("//a[@data-task='signin']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@type='email']").send_keys(my_email)
        driver.find_element_by_xpath("//input[@type='submit']").click()
        driver.find_element_by_xpath("//input[@type='password']").send_keys(my_password)
        #Time for page to fully load before clicking sign in button to access the Inbox
        #try/except is used here instead of time.sleep() to optimize speed
        while True:
            try:
                driver.find_element_by_xpath("//input[@type='submit']").click()
                break
            except:
                print("Log-in page still hasn't loaded")
        #To choose no when asked whether to always stay signed in with this email or not
        try:
            driver.find_element_by_id("idBtn_Back").click()
        except:
            "user was not prompted with the question"
        #Time for page to fully load before reading emails from the Inbox
        #try/except is used here instead of time.sleep() to optimize speed
        while True:
            try:
                #To find all the emails in the inbox
                recieved_mail=driver.find_elements_by_xpath("//div[starts-with(@id,'AQAAAW')]")
                break
            except:
                "Inbox still hasn't loaded"
        read_out=[]
        for i in range(10):
            try:
                #Print() is used to check whether the email contains any non english letters or not
                print(recieved_mail[i].get_attribute('aria-label'))
                read_out.append(recieved_mail[i].get_attribute('aria-label'))
            except:
                "Contains non english letters"
        #Opening text reader to play the received emails out loud
        driver.get("https://ttsreader.com/")
        
        for j in range(len(read_out)):
            text_box=driver.find_element_by_id("text_box")
            text_box.clear()
            text_box.send_keys(read_out[j])
            driver.find_element_by_id("speak_button_new").click()
            #Number of words in each email
            word_count=len(read_out[j].split())
            #Give time for each email to be fully read out by dividing the word count by 5, 
            #given that the average speed for reading out loud is 5 words per second
            time.sleep(word_count/5)
        
#Opening chrome browser in icognito mode
#Incognito mode is used to prevent the script from affecting my normal browser cookies
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver=webdriver.Chrome(options=options)           
#Run the script
Automate=Automation()
Automate.music()