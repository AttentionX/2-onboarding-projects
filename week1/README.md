# Week 1️⃣ - Q & A with Retriever Augmented Generation 

## Quick Start 🚀

install dependencies:
```bash
pip3 install requirements.txt
```
Create `.env` file and type your `OPENAI_API_KEY` in the following format:
```
OPENAI_API_KEY=<your key>
```
Run the baseline:
```python
python3 baseline_qa.py 
```
<a href="https://asciinema.org/a/NDDHUuBb5JQyN3Wck6TrBO6jG" target="_blank"><img src="https://asciinema.org/a/NDDHUuBb5JQyN3Wck6TrBO6jG.svg" width="400" /></a>

## Goal 

...
하지만 더 개선해볼 수 있지 않을까요? 

온보딩 첫 주의 목표는 베이스라인을 개선하는 것입니다. 어떤 접근법이든 좋습니다. 어떤 형식이든 좋습니다. 팀 별로 베이스라인을 개선 후 다음 모임 때 공유해주세요.

## Some Pointers 👇

### better chunking

`RAGVer5`는 [같은 섹션에 있는 문장을 모은 뒤](https://github.com/eubinecto/tinyRAG/blob/e6bcacbca872a7e0b04c2baaf992c1126a5fbfa8/main_preprocess.py#L10-L23) 인접한 문장 [2개를 이어 chunk를 만듭니다.](https://github.com/eubinecto/tinyRAG/blob/e6bcacbca872a7e0b04c2baaf992c1126a5fbfa8/main_preprocess.py#L24-L34) 이게 최선일까요? 더 나은 방법은 없을까요? 



### Chitchat moderation
 
쓸데 없는 질의에도 검색을 합니다. - 리소스 낭비다. 

- Chain-of-Thought prompting 
- Microsoft's guidance

### Hybrid Search


references:
- rank_bm25
- reciprocal rank fusion


### Conversational Q & A

`RAGVer5`는 아직 챗봇이 아닙니다. 대화형 Q & A는 할 수 없습니다. 대화형 Q & A를 구현해보는건 어떨까요?  (e.g. [Mendable](https://www.mendable.ai))

e.g. Mendable


### Real-time Q & A

2. `RAGVer5`처럼 검색엔진을 직접 구축할 필요가 있을까요?  그냥 구글을 쓰면 되지 않을까요? 실시간 정보도 얻을 수 있지 않을까요? Retreiver를 구글 검색으로 바꿔보는건 어떨까요? (e.g. [WebChatGPT](https://chrome.google.com/webstore/detail/webchatgpt-chatgpt-with-i/lpfemeioodjbpieminkklglpmhlngfcn))

e.g. WebChatGPT


### Multimodal Q & A

4. `RAGVer5`는 텍스트만 이해합니다. 이미지로 증강할 수는 없을까요? 멀티모달 정보로 증강을 해보는건 어떨까요? 

- e.g. [GPT4의 위력](https://www.clien.net/service/board/park/17962934))
- e.g. Bard Lens
