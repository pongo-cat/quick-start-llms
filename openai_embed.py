#Code from Listing 2.1

import hashlib
import os
from fastapi import FastAPI
from pydantic import BaseModel
import openai
from openai import OpenAI

print(os.environ)

client = OpenAI()
engine = 'text-embedding-3-small'

def get_embedding(text, model):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

raw_text = input("Enter the text you want to embed: ")
embedding = get_embedding(raw_text, engine)
 
#Print length and embedding
print(f"Length of the embedding: {len(embedding)}")
print(f"Embedding: {embedding}")