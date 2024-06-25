#Code from listing 2.2

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/multi-qa-mpnet-base-cos-v1')

docs = [ 
        "Horses are sports animals",
        "Horses have grown larger over the centuries"
        ]

doc_emb = model.encode(docs, batch_size = 32, show_progress_bar=True)

print (f"The size of the embeddings is: {doc_emb.shape}")