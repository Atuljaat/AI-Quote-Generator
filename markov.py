import markovify

# it helps in creating the model first time from txt file

# with open(r".\cleaned_files\markov\Markov_quotes.txt", encoding='utf-8') as file:
#     text = file.read()

# it created my model first time and then saves it 

# model_json = quotes_model.to_json()
# with open(r".\cleaned_files\markov\model.json", "w", encoding="utf-8") as f:
#     f.write(model_json)

with open (r".\cleaned_files\markov\model.json" , encoding='utf-8') as f:
    model = f.read()

quotes_model = markovify.NewlineText.from_json(model)

for _ in range(5):
    quote = quotes_model.make_short_sentence(140, tries=100)
    if quote and quote.endswith(('.', '!', '?')):
        print(quote)
