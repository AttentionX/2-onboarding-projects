"""
This is an example template code and may contain errors
"""
import openai_api

PDF_PATH = ''

def read_pdf(path):
    raise NotImplementedError

def chunk_text(text):
    raise NotImplementedError

def initialize_vectordb():
    raise NotImplementedError

def save_to_vectordb(index, chunks):
    raise NotImplementedError

def fetch_from_vectordb(index, query):
    raise NotImplementedError

def main():
    OpenAIAPI = openai_api.OpenAIAPI()

    pdf_text = read_pdf(PDF_PATH)
    chunks = chunk_text(pdf_text)
    chunks = [openai_api.get_embedding(chunk) for chunk in chunks]

    vector_db_index = initialize_vectordb()
    save_to_vectordb(vector_db_index, chunks)

    while True:
        query = input("Ask a question:\n")
        reponse_embedding = openai_api.get_embedding(response)
        relevant_result =  fetch_from_vectordb(vector_db_index, reponse_embedding)
        prompt = f"Answer the following question based on the given informaiton:\n\nQuestion: {query}\nGiven Information:\n{relevant_result}"
        response = OpenAIAPI.get_response(prompt)
        print(response)

if __name__ == "__main__":
    main()