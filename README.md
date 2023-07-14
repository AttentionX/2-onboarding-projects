# 2기 Onboarding Projects

# 목적
- SOTA LLM을 사용해보면서 성능과 잘하는점, 한계를 직접 체험하고 이를 활용해서 새로운 문제를 해결할 수 있는 프로덕트 만들어보기
- 동아리의 다양한 사람들과 팀 프로젝트를 해보면서 동아리분들 알아가기

## Week 1️⃣ - retriever-augmented Q&A 

### 베이스라인 - Hybrid search with Chain-of-Thought moderation ([`RAGVer5`](https://github.com/eubinecto/tinyRAG/blob/e6bcacbca872a7e0b04c2baaf992c1126a5fbfa8/tinyrag/rag_v5.py#L6-L72))

example Q & A with `RAGVer5` | 
--- | 
<img href="https://asciinema.org/a/CqOiYktayTo6MXJ5MlgvPKj4C" src="https://asciinema.org/a/CqOiYktayTo6MXJ5MlgvPKj4C.svg"  width="700"/> | 

-  how it's made - the retriever 🔎
      - `RAGVer1`: term-matching search with BM25
         - pros: high precision (`main goal` / `내일 날씨` 와 같은 키워드 검색에 용이)
         - cons: low recall (`what are the keyfindings of the paper?` / `내일 우산 필요해`와 같은 의도파악이 필요한 질의에 약함)
      - `RAGVer2`: semantic search with ANN
         - pros: high recall (의도파악에 용이)
         - cons: low precision (키워드 검색에 약함 - 이것도 못찾아? 같은 경우가 왕왕 있음)
      - `RAGVer3`: 그럼 둘다 써보자 - bringing the best of both worlds with hybrid search
- how it's made - the reader 📖
  - `RAGVer4`: augmented generation with stuffing
  - `RAGVer5`: chitchat moderation with Chain-of-Thought & Microsoft’s guidance

  
### 팀 프로젝트 - go above and beyond `RAGVer5`

🔥 하이브리드 검색보다 나은 방법이 있을까요? Reader를 더 개선해볼 수 있을까요? `RAGVer5`보다 더 나은 Q & A 시스템을 만들어보세요!

➡️ 상세설명: [week1/README.md](https://github.com/AttentionX/season-2-onboarding-projects/blob/main/week1/README.md)

    
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


