# Week 1 - Q & A with Retriever Augmented Generation 

## Goal

앞서 소개한 베이스라인, `RAGVer5`의 Retreiver는 하이브리드 검색으로 precision과 recall을 모두 잡았습니다. Reader는 Chain-of-Thought 추론으로 자신없는 답변은 하지 않도록 강제했습니다.
하지만 더 개선해볼 수 있지 않을까요? 

온보딩 첫 주의 목표는 베이스라인을 개선하는 것입니다. 어떤 접근법이든 좋습니다. 어떤 형식이든 좋습니다. 팀 별로 베이스라인을 개선 후 다음 모임 때 공유해주세요.

## Some Pointers

1. `RAGVer5`는 [같은 섹션에 있는 문장을 모은 뒤](https://github.com/eubinecto/tinyRAG/blob/e6bcacbca872a7e0b04c2baaf992c1126a5fbfa8/main_preprocess.py#L10-L23) 인접한 문장 [2개를 이어 chunk를 만듭니다.](https://github.com/eubinecto/tinyRAG/blob/e6bcacbca872a7e0b04c2baaf992c1126a5fbfa8/main_preprocess.py#L24-L34) 이게 최선일까요? 더 나은 방법은 없을까요? 
1. `RAGVer5`는 하나의 PDF만 검색해 답변합니다. 여러 개 문서를 검색하게 만들어보는걸 어떨까요? (e.g. [ChatDOC](https://chatdoc.com))
2. `RAGVer5`처럼 검색엔진을 직접 구축할 필요가 있을까요?  그냥 구글을 쓰면 되지 않을까요? 실시간 정보도 얻을 수 있지 않을까요? Retreiver를 구글 검색으로 바꿔보는건 어떨까요? (e.g. [WebChatGPT](https://chrome.google.com/webstore/detail/webchatgpt-chatgpt-with-i/lpfemeioodjbpieminkklglpmhlngfcn))
3. `RAGVer5`는 아직 챗봇이 아닙니다. 대화형 Q & A는 할 수 없습니다. 대화형 Q & A를 구현해보는건 어떨까요?  (e.g. [Mendable](https://www.mendable.ai))
4. `RAGVer5`는 텍스트만 이해합니다. 하지만 이미지로 증강할 수는 없을까요? 멀티모달 정보로 증강을 해보는건 어떨까요? (e.g. [GPT4의 위엄](https://www.dogdrip.net/471917756))

## 참조 코드 - OpenAI & Pinecone
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
