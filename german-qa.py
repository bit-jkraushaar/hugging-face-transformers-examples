from transformers import pipeline
import requests
from bs4 import BeautifulSoup
import sys

# first argument: url
url = sys.argv[1]
# second argument: question
question = sys.argv[2]

# get the requested website and extract text using BeautifulSoup
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()

# initialise Q&A model
model_name = 'deepset/gelectra-base-germanquad'
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

# query model and print result
input = { 'question': question, 'context': text}
result = nlp(input)
print(f"{ result['answer'] } (Score: {result['score']})")