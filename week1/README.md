# 1. Q&A Chatbot

## (1) 목표
- GPT-4 논문에 대해 Q&A 챗봇 만들기

## (2) 참조
1. OpenAI API ([공식 문서](https://platform.openai.com/docs/guides/gpt/chat-completions-api))
```python
import openai
from dotenv import load_dotenv
load_dotenv()

# OpenAI API Key 세팅하기
openai.api_key = os.environ.get('OPENAI_KEY')

model = "gpt-3.5-turbo"
system_message = "You are a helpful assistant"
query = "Explain self-attention"

messages = [
    {"role":"system", "content":system_message},
    {"role":"user", "content":query}
]

response = openai.ChatCompletion.create(model=model, messages=messages).choices[0].message
```
2. Pinecone Vector DB (Pinecone [공식 문서](https://docs.pinecone.io/docs/quickstart))
```python
import pinecone
pinecone.init(api_key="YOUR_API_KEY", environment="YOUR_ENVIRONMENT")

example_sentence_1 = {
    "text" : "GPT-4 is a multimodal model"
}
example_sentence_2 = {
    "text" : "GPT has over 1 trillion parameters"
}

embeddings_list = [
    {"id":"1", "values":embedding_1, "metadata":example_sentence_1},
    {"id":"2", "values":embedding_2, "metadata":example_sentence_2}
]

pinecone.create_index("quickstart", dimension=1536, metric="cosine")
index = pinecone.Index("quickstart")
index.upsert(embeddings_list)
fetched_results = index.query(vector=query_embedding,tok_k=2,includeMetadata=True)
fetched_sentence = fetched_results['matches'][0]['metadata']['text']
```

## (3) To-do
1. GPT-4 PDF를 chunking하기
2. 각 chunk를 embedding으로 바꾸고 vector DB에 저장하기
3. User chat flow 만들기
    1. 유저가 질문했을 때 질문을 embedding으로 바꾸기
    2. vector DB를 query를 대답할 수 있는 정보를 fetch하기
    3. fetch한 chunk들을 prompt에 넣어서 질문하기
4. Bonus
    1. 유저의 Chat History도 프롬트에 넣기
    2. 실시간 웹서칭을 통해 실시간으로 최신 정보를 찾아서 알려주기 (Bing Chat)
    3. 사진을 이용한 질문에도 대답하기 (OCR, Vision Library를 사용해서 정보를 stringify하기)