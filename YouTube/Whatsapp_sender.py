from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Replace with the name/contact of the person you want to send the message to
contact_name = "Martin Mathew Us"

# Replace with the message you want to send
message_text = "Hello, this is an automated test message sent using Selenium!"


chrome_driver_path = '/home/mmk/Downloads/chromedriver-linux64/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir=/home/mmk/Downloads/chromedriver-linux64')
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

driver.implicitly_wait(5)
driver.get("https://web.whatsapp.com")
driver.implicitly_wait(20)


try:
    # Find the search input field
    search_field = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_field.send_keys(contact_name)
    driver.implicitly_wait(5)

    contact = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//span[@title="{contact_name}"]')))
    contact.click()

    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(5)
    input_element = driver.find_element_by_css_selector('[title="Type a message"][data-testid="conversation-compose-box-input"]')

    input_element.send_keys(message_text)
    driver.implicitly_wait(10)
    button_element = driver.find_element_by_xpath('//button[@data-testid="compose-btn-send"]')
    driver.implicitly_wait(15)

    button_element.click()
    driver.implicitly_wait(15)

    print(f"Text '{message_text}' inserted successfully.")
    print(f"Message sent to {contact_name}: {message_text}")

except Exception as e:
    print("An error occurred:", e)

# finally:
#     # Close the browser
#     driver.quit()