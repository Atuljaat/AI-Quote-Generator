import pandas as pd

clean_df = pd.read_csv('cleaned_quotes_markov.csv')
clean_df['quote'] = clean_df['quote'].str.replace(r'[\n\r]+', ' ', regex=True)
clean_df['quote'].to_csv("Markov_quotes.txt", index=False, header=False)
