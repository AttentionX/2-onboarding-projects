# 2기 Onboarding Projects

# 목적
- SOTA LLM을 사용해보면서 성능과 잘하는점, 한계를 직접 체험하고 이를 활용해서 새로운 문제를 해결할 수 있는 프로덕트 만들어보기
- 동아리의 다양한 사람들과 팀 프로젝트를 해보면서 동아리분들 알아가기

## Week 1️⃣ - retriever-augmented Q&A 

### Baseline - fundamentals of Retriever-augmented Generation with [`tinyRAG`](https://github.com/eubinecto/tinyRAG)

example retriever-augmented answer from `text-ada-002` | 
--- | 
[![asciicast](https://asciinema.org/a/7asQ1olH0AXMAxtrRtwG1L8xU.svg)](https://asciinema.org/a/7asQ1olH0AXMAxtrRtwG1L8xU) | 

 1. 검색은 어떻게 구현해볼 수 있을까?  - the retriever 🔎
      - `RAGVer1` - term-matching search with BM25
         - pros: high precision (`main goal` / `내일 날씨` 와 같은 키워드 검색에 용이)
         - cons: low recall (`what are the keyfindings of the paper?` / `내일 우산 필요해`와 같은 의도파악이 필요한 질의에 약함)
      - `RAGVer2` - semantic search with ANN
         - pros: high recall (의도파악에 용이)
         - cons: low precision (키워드 검색에 약함 - 이것도 못찾아? 같은 경우가 왕왕 있음)
      - `RAGVer3` - 그럼 둘다 써보자 - bringing the best of both worlds with hybrid search
  2. 검색결과로 생성을 어떻게 증강해볼 수 있을까?  - the reader 📖
      - `RAGVer4` - augmented generation with stuffing
      - `RAGVer5` - 더 똑똑하고 안전한 답변을 생성하고 싶다면? - moderation with Chain-of-Thought & Microsoft’s guidance
  
### Team project - go above and beyond `RAGVer5`

🔥 하이브리드 검색보다 나은 방법이 있을까요? Reader를 더 개선할 수는 없을까요? `RAGVer5`보다 더 나은 Q & A 시스템을 만들어보세요!

some pointers:
1. `RAGVer5`는 하나의 PDF만 검색해 답변합니다. 여러 개 문서를 검색할 수 있게 만들어 보세요! (e.g. [ChatDOC](https://chatdoc.com))
2. `RAGVer5`처럼 검색엔진을 직접 구축할 필요가 있을까요? 그냥 구글을 쓰면 되지 않을까요? Retreiver를 구글 검색으로 바꿔보세요!(e.g. ChatGPT Browser plugin,  Bing Chat, etc) 
3. `RAGVer5`는 텍스트만 이해합니다. 하지만 이미지로 증강할 수는 없을까요? 다중모달 정보로 생성을 증강해보세요! (e.g. GPT4,  OCR Chat, LENS)

    
## Week 2️⃣ - browser automation
- Action을 해주는 Agent
- General Action을 해주는 것을 목표
- 또는 아래 중 택 1
  - 영화 예약
  - 음식 배달
  - SNS 자동 포스팅 
  - (위와 같이 한 도메인 선택)
  - Function call api 참조

     

## Week 3️⃣ - build whatever you want
- 예시 주제
  - 여러 modality api를 이용한 프로젝트 (OCR Chat, LENS)
  - General World Agent
- Voyager를 참조해서 real world에 풀어 놓기
  - 예시. 트위터에서 오늘까지 팔로워 1000명 받을 수 있도록 활동해봐
- LLM Generation
  - 예시 문제 생성
- LLM Evaluation
  - 성능 평가 framework


