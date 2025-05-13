import pandas as pd

df1 = pd.read_csv("quotes_data1to24.csv")
df2 = pd.read_csv("quotes_data25to30.csv")
df3 = pd.read_csv("quotes_data31to50.csv")
df4 = pd.read_csv("quotes_data51to74.csv")
df5 = pd.read_csv("quotes_data75to100.csv")

goodreads_Quotes = pd.concat([df1,df2,df3,df4,df5] , ignore_index=True)

goodreads_Quotes.to_csv("goodreads_Quotes.csv")

print( len(df1) + len(df2) + len(df3) + len(df4) + len(df5)  )
print( len(goodreads_Quotes))