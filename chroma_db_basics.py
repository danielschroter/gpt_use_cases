import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="MyDocs")

collection.add(
    
    documents=["my name is daniel", "i am a software engineer"],
    metadatas=[{"source": "my_source"}, {"source": "my_second_source"}],
    ids=["id1", "id2"],
    
)

result = collection.query(
    query_texts=["what is my name"],
    n_results= 1
)

print(result)