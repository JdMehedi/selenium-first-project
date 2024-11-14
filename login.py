from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to your WebDriver
driver_path = "/path/to/chromedriver"  # Replace with your WebDriver path

# Initialize the driver
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://www.google.com")

# Interact with elements (for example, search box)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()

# Close the driver after a short delay
driver.quit()
