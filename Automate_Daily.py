import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Automation:
    def daily(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver=webdriver.Chrome(options=options)
        
        driver.get("https://www.google.com")
        driver.find_element_by_xpath("//*[@id='SIvCob']/a").click()
        search_bar=driver.find_element_by_xpath("//input[@title='Search']")
        search_bar.send_keys("alexandria weather", Keys.ENTER)
        temperature="Temperature is "+driver.find_element_by_id("wob_tm").text+" degrees Celsius"
        precipitation=" Precipitation is "+driver.find_element_by_id("wob_pp").text
        humidity=" Humidity is "+driver.find_element_by_id("wob_hm").text
        wind=" Wind speed is "+driver.find_element_by_id("wob_ws").text
        full_temperature=temperature+precipitation+humidity+wind
        
        driver.get("https://ttsreader.com/")
        text_box=driver.find_element_by_id("text_box")
        text_box.clear()
        text_box.send_keys(full_temperature)
        driver.find_element_by_id("speak_button_new").click()
        time.sleep(10)
        
Automate=Automation()
Automate.daily()