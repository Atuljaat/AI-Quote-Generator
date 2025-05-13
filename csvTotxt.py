import pandas as pd

Data = pd.read_csv("goodreads_Quotes.csv")

Data.drop_duplicates(subset='quote')
Data.drop_duplicates()

quotes = Data["quote"]
# author = Data["author"]
# tags = Data["tags"]
# likes = Data["likes"]

# Clean quote column
Data['quote'] = Data['quote'].replace(r'\s+', ' ', regex=True).str.strip()

# Join all quotes into a single string
text = " ".join(Data['quote'].dropna().unique())

# Save to txt if needed
with open("goodReads.txt", "w", encoding="utf-8") as f:
    f.write(text)