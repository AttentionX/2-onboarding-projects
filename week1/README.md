# Week 1️⃣ - Q & A with Retriever Augmented Generation 

## Running the baseline 🚀

install dependencies:
```bash
pip3 install requirements.txt
```
Create `.env` file and type your `OPENAI_API_KEY` in the following format:
```
OPENAI_API_KEY=<your key>
```
Ask questions with `python3 baseline_qa.py` | 
--- | 
<a href="https://asciinema.org/a/NDDHUuBb5JQyN3Wck6TrBO6jG" target="_blank"><img src="https://asciinema.org/a/NDDHUuBb5JQyN3Wck6TrBO6jG.svg" width="600" /></a> | 

## Goal 🥅

팀별로 베이스라인과 문답해보며 문제점을 발견해보세요. 이번 주 온보딩의 목표는 베이스라인의 문제점을 찾고 개선하는 것입니다.
어떤 문제점이든 좋습니다. 어떤 접근법이든 좋습니다. 베이스라인을 개선하여 공유해주세요!

## Some Pointers 👇


### better chunking

`baseline_chunk.py`를 살펴보면 청킹을 어떻게 했는지 확인할 수 있습니다. 

우선 같은 섹션에 있는 문장을 모은 뒤: 
https://github.com/AttentionX/season-2-onboarding-projects/blob/5c7be2540aa2349294256ed465cb84f52e068573/week1/baseline_chunk.py#L11-L24

인접한 문장 2개를 이어 chunk를 만들고 있는데요:
https://github.com/AttentionX/season-2-onboarding-projects/blob/5c7be2540aa2349294256ed465cb84f52e068573/week1/baseline_chunk.py#L25-L35

이게 최선일까요? 더 나은 청킹 알고리즘이 있다면 제안해보세요!

### Chitchat moderation
 
쓸데 없는 질의에도 검색을 합니다. - 리소스 낭비다. 

References:
- Chain-of-Thought prompting 
- Microsoft's guidance

### Hybrid Search


References:
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
