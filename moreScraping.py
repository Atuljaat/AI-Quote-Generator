from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_path = r"C:\Users\Atul\Downloads\chrome-win64\chrome-win64\chrome.exe"  # Update this if your path is different
driver_path = r"C:\Windows\chromedriver.exe"


options = Options()
options.binary_location = chrome_path  # tell Selenium where Chrome is
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)


# Open the BrainyQuote positive quotes page
driver.get("https://www.goodreads.com/quotes")
time.sleep(2)  # Allow time for JS to load

# Scroll to load more quotes (if needed)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Locate all quote containers
quote_elements = driver.find_elements(By.CLASS_NAME, "quote")

# Extract and print
for quote in quote_elements:
    try:
        quote = quote.find_element(By.CLASS_NAME, "quoteText").text
        print(f"Quote: {quote}")
    except:
        continue  # Skip if quote or author isn't found

driver.quit()

# print(driver.title)
# driver.quit()
