"""
This Code aim to get the latest uploaded holy mass link from youtube channel
"""

import json
import requests
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


def get_url_and_details():
    url = "https://www.youtube.com/playlist?list=PLrQpAZRHiEyKUK-w2Mne0tpWzYvAHafy0"  
    driver = Initializing_chrome()
    driver.implicitly_wait(5)
    driver.get(url)
    xpath_expression = '//*[@id="video-title"]'
    wait = WebDriverWait(driver, 5)
    title_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_expression)))
    title_value = title_element.text.strip()
    date = title_value.split('|')[0]
    date = date.split(',')[1]
    Fr_name = title_value.split('|')[1]
    Video_url = title_element.get_attribute('href')
    
    Video_details = {
        "Video_url": Video_url,
        "Date": date.strip(),
        "Fr_name": Fr_name.strip()
    }

    json.dumps(Video_details)
    return(json.dumps(Video_details))
    


if __name__ == "__main__":
    Initializing_chrome().quit()
    print(get_url_and_details())
    Initializing_chrome().quit()