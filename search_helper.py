import chromadb
import ollama

# create or load the Chroma client, pointing to your persistent database
chroma_client = chromadb.PersistentClient(path="/Users/yashjankay/Desktop/Playground/RAG-telugu-samethalu/vector-store")

# load your existing collection
collection = chroma_client.get_collection("telugu_proverbs")

def generate_clean_search_results(results):
    sr_list = []
    # Assuming results["documents"][0] and results["metadatas"][0] exist and have the same length
    for i, doc in enumerate(results["documents"][0]):
        implication = results["metadatas"][0][i]["implication"]
        translation = results["metadatas"][0][i]["translation"]
        original_proverb = doc

        entry = (
            f"{i+1}. Implication: {implication}\n"
            f"   Translation: {translation}\n"
            f"   Original Proverb: {original_proverb}"
        )
        sr_list.append(entry)
    
    # Join each entry with a blank line in between
    return "\n\n".join(sr_list)

def search_collection(user_input):
    # Embed user query
    embedding = ollama.embed(model="mxbai-embed-large", input=user_input)["embeddings"]

    # Query collection for top results
    results = collection.query(
        query_embeddings=embedding,
        n_results=5
    )

    # Format results
    final_results = generate_clean_search_results(results)
    return final_results
