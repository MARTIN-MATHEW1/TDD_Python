"""
This Code aim to get the latest uploaded holy mass link from youtube channel
"""

import json
import requests, datetime
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Initializing_chrome():
    try:
        chrome_driver_path = '/home/mmk/Downloads/chromedriver-linux64/chromedriver'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--user-data-dir=/home/mmk/Downloads')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    except Exception as e:
        print("Chrome Initialization failed")

    return(driver)

class Daily_mass_url():

    def __init__(self,channel_url, channel_name):
        self.channel_url = channel_url
        self.channel_name =channel_name
        

    def video_date_checker(self, Date_String):
        Date_Part_01 = Date_String.split('|')[0].split(',')[1].upper()
     
        # Date_Part_01 = ' 04 Aug 2023'
        if Todays_Date.upper() == Date_Part_01[1:]:
            print("Date Matches with Todays", Date_Part_01)
            return True
            
    def daily_url_returner(self):       
        print("Channel_Name", self.channel_name)          
        driver = Initializing_chrome()
        driver.implicitly_wait(5)
        driver.get(self.channel_url)
        xpath_expression = '//*[@id="video-title"]'
        wait = WebDriverWait(driver, 5)
        title_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_expression)))
        title_value = title_element.text
        Video_url = title_element.get_attribute('href')


        if self.channel_name == "Goodness":
            Video_Upload_time_css = "ytd-playlist-video-renderer.style-scope:nth-child(1) > div:nth-child(2)"
            Video_Upload_time = str((driver.find_element_by_css_selector(Video_Upload_time_css).text.split('•')[-1]))

            if Video_Upload_time.split()[0] == 'Scheduled':
                print("First Video in List is Upcoming. Collecting next video")
                next_video_css = driver.find_elements_by_id("video-title")[1]
                next_video_url = next_video_css.get_attribute('href')
                
                #check if the next video is upto date .if not, the function will return the link from Divine Channel
                Channel_1_satisfy = self.video_date_checker(next_video_css.text)
                if Channel_1_satisfy == True:
                    title_value = next_video_css.text
                    return(title_value, next_video_url)
                else:
                    return(False)
        else:
            return(title_value, Video_url)
        driver.quit()



if __name__ == "__main__":
    # Initializing_chrome().quit()
    Goodness_url = "https://www.youtube.com/playlist?list=PLrQpAZRHiEyKUK-w2Mne0tpWzYvAHafy0"
    Divine_url = "https://www.youtube.com/playlist?list=PL6YoNWbdHbxfvmuaJcQA88GlNIShuGWOw"
    

    # for channel in channel_list:
    today = datetime.date.today()
    Todays_Date = today.strftime('%d %b %Y')
    print("Todays_Date", Todays_Date)

    channel_1 = Daily_mass_url(Goodness_url, "Goodness")
    Check_Video_in_Goodness = channel_1.daily_url_returner()

    if Check_Video_in_Goodness == False:
        print("Second Video in Playlist is not of Todays. Channel Changed to Divine !!")
        channel_2 = Daily_mass_url(Divine_url, "Divine")
        Check_Video_in_Divine = channel_2.daily_url_returner()
        print(Check_Video_in_Divine)
    else:
        print(Check_Video_in_Goodness)

