from fastapi import FastAPI
from collections import Counter
import re 


words = re.findall(r'\w+', open('articles//sample2.txt').read().lower())
words +=( re.findall(r'\w+', open('articles//sample3.txt').read().lower()))
#words +=( re.findall(r'\w+', open('articles//jonaxx_-_24_signs_of_summer_001[1].txt').read().lower()))
commow= ( Counter(words).most_common(5) )
print ("most common words in articles" , commow)
app = FastAPI()


@app.get("/")
async def root():
  return  ("most common words in articles" , commow)