# RAG method for Cover Letters


## 1. requirements.txt
```
pip install -r requirements.txt
```

## 2. pinecone
https://www.pinecone.io/

pinecone으로 가서 api key를 받으세요

## 3. api key 보관
Rag.py와 같은 폴더에 .env 파일을 생성합니다.

그 후, 파일 안에 다음 과 같이 입력합니다.

```
PINECONEKEY = 당신의 api key
```

## 4. 사용법

Rag.py는 RAG라는 클래스로 이루어져 있습니다. 초기화 할 때 인덱스를 불러오거나 생성합니다. text를 입력하고 싶으면 add, query로 검색을 하고 싶으면 search를 호출하세요.

Input_txt.ipynb에 예제들이 나와 있습니다. 본인의 프로젝트에 맞게 만들어주세요.