from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import random

driver_path = r"C:\Windows\chromedriver.exe"
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
]

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(f"user-agent={random.choice(user_agents)}")
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

first_time = True

for page in range(75,101):
    while True : 
        print(f"Scraping page: {page}")
        driver.get(f'https://www.goodreads.com/quotes?page={page}')
        # input("⏸️ Page loaded. Press Enter after you're done closing the popup manually...")
        # try:
        #     WebDriverWait(driver, 3).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, 'modal__content'))
        #     )
        #     input("⏸️ Login popup detected. Please close it manually, then press Enter to continue...")
        # except:
        #     pass

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'quote'))
        )

        quotes = driver.find_elements(By.CLASS_NAME, 'quote')
        data = []

        for quote in quotes:
            try:
                quotetext = quote.find_element(By.CLASS_NAME, 'quoteText').text.strip()
                author = quote.find_element(By.CLASS_NAME, 'authorOrTitle').text.strip()

                try:
                    likes = quote.find_element(By.CLASS_NAME, 'right').find_element(By.CLASS_NAME, 'smallText').text.strip()
                    likes = likes.replace('likes', '').strip()
                except NoSuchElementException:
                    likes = ""

                try:
                    tags = quote.find_element(By.CLASS_NAME, 'left').text.strip()
                    tags = tags.split(':')[1].strip().replace('attributed-no-source,', '')
                except NoSuchElementException:
                    tags = ""

                clean_quote = quotetext.split("―")[0].strip().strip('“”"')

                data.append({
                    "quote": clean_quote,
                    "author": author,
                    "tags": tags,
                    "likes": likes
                })

            except Exception as e:
                print(f"Error parsing quote on page {page}: {e}")
                continue

        if data:
            df = pd.DataFrame(data)
            df.to_csv("quotes_data75to100.csv", mode='a', header=first_time, index=False)
            first_time = False
            print(f"✅ Saved page {page} with {len(data)} quotes.")
            time.sleep(random.uniform(2, 5))
            break  # move to next page
        else:
            print(f"⚠️ No quotes scraped on page {page}. Possibly due to popup or error.")
            input("⏸️ Press Enter to reload the page after fixing (e.g. closing popup)...")

        time.sleep(random.uniform(3, 5))

driver.close()
