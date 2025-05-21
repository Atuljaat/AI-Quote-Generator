import pandas as pd
import re
import emoji
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0  # for consistent results

# Load your quotes CSV
df = pd.read_csv("all_quotes.csv")

# Check for required column
if 'quote' not in df.columns:
    raise ValueError("CSV must have a 'quote' column.")

# Function to clean each quote
def clean_quote(quote):
    quote = str(quote).strip()
    quote = emoji.replace_emoji(quote, replace='')                # remove emojis
    quote = re.sub(r"http\S+", "", quote)                         # remove URLs
    quote = re.sub(r"[’‘]", "'", quote)
    quote = re.sub(r"[“”]", '"', quote)
    quote = re.sub(r"[^\x00-\x7F]+", "", quote)                   # remove non-ASCII
    quote = re.sub(r"[^a-zA-Z0-9\s.,!?'\"]", "", quote)           # keep letters and common punctuation
    quote = re.sub(r"\s+", " ", quote)                            # normalize whitespace
    return quote.strip()

# Function to check if quote is valid
def is_valid(quote):
    try:
        return (
            15 <= len(quote) <= 200
            and len(quote.split()) >= 3
            and detect(quote) == "en"
        )
    except:
        return False

# Clean and filter
cleaned = []
for quote in df['quote']:
    cleaned_quote = clean_quote(quote)
    if is_valid(cleaned_quote):
        cleaned.append(cleaned_quote)

# Save to txt file
with open("cleaned_quotes_lstm.txt", "w", encoding="utf-8") as f:
    for quote in cleaned:
        f.write(quote + "\n")

print(f"✅ Done! Saved {len(cleaned)} cleaned quotes to cleaned_quotes_lstm.txt")
