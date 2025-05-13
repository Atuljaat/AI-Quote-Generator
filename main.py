import pandas as pd
import markovify
import json

with open("goodReads.txt","r",encoding="utf-8") as file :
    text = file.read()

model = markovify.Text(text)
modelJSON = model.to_json()

with open("goodReads.json","w") as f:
    f.write(modelJSON)

# with open("model.json","r") as f:
#     modelJSON = f.read()

# model = markovify.Text.from_json(modelJSON)

print("generated quote by ai model : ")
for a in range(10):
    quote = model.make_sentence(list=100)
    print("-",quote)
