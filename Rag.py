import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec, Index
from sentence_transformers import SentenceTransformer

class RAG():
    def __init__(self): #데이터베이스 초기화 또는 불러오기
        load_dotenv()
        self.key = os.getenv('PINECONEKEY')
        print(f"key = {self.key[:4]}...")

        pc = Pinecone(
            api_key=self.key,
            default_serverless_spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

        index_name = "rag"

        if index_name not in [index["name"] for index in pc.list_indexes()]: #없으면 생성
            pc.create_index(
                name=index_name,
                dimension=768,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )
            )
        
        self.index = pc.Index(index_name)
        self.model = SentenceTransformer('jhgan/ko-sbert-nli')

    def add(self, paragraph): #문단 추가
        embedding = self.model.encode(paragraph).tolist()
        unique_id = str(self.index.describe_index_stats()["total_vector_count"])  
        self.index.upsert([(unique_id, embedding, {"text": paragraph})])
        print(f"added : {paragraph[:30]}...")

    def search(self, query_sentence, top_k=3): #쿼리로 검색 수행, top_k로 반환되는 답변 개수 조절 가능

        query_embedding = self.model.encode(query_sentence).tolist()

        result = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_values=False,
            include_metadata=True 
        )

        return result
