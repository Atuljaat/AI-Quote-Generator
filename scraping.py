from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random

firstTime = True
for page in range(1,11):
    link = f'https://quotes.toscrape.com/page/{page}/'
    html = requests.get(link)
    soup = BeautifulSoup(html.text,'html5lib')

    fullQuote = soup.find_all('div',class_="quote")

    data=[]

    for quote in fullQuote:
        quoteText = (quote.find('span',class_='text')).text
        authorName = (quote.find('small',class_='author')).text
        tags =  [ tag.text for tag in quote.find_all('a',class_='tag')]
        data.append({
            "quote" : quoteText,
            "authorName":authorName,
            "Tags": ','.join(tags)
        })
        
    df = pd.DataFrame(data)
    df.to_csv("quotes_data.csv",mode='a',header=firstTime,index=False)
    firstTime = False
    delayTime = random.choice([1,2,3])
    print(f"page:{page} saved ")
    time.sleep(delayTime)
    
