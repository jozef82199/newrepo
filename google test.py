from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Path to chromedriver
PATH = 'chromedriver_folder/chromedriver'
service = Service(PATH)
driver = webdriver.Chrome(service=service)



# Open Google
driver.get('http://www.google.com/')

# Find search box and enter query
element = driver.find_element(By.NAME, 'q')
element.click()
element.send_keys('hello')
element.send_keys(Keys.RETURN)  # Corrected Keys.RETURN usage

# Wait for results to load
driver.implicitly_wait(8)

# Find and print the "Hello" definition (if available)
try:
    hello_text = driver.find_element(By.ID, 'kp-wp-tab-overview')
    print(hello_text.text)  # Extract and print text
except:
    print("Could not find the expected result.")

input("Press Enter to close the browser...")  # Keeps script running
driver.quit()
