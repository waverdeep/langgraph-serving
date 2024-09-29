from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import chatbot

app = FastAPI(title="langgraph-ai-server", version="1.0.0")
app.include_router(chatbot.router, prefix="/note", tags=["posts"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서의 접근 허용 (보안상 필요한 도메인만 허용하는 것이 좋음)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST, OPTIONS 등)
    allow_headers=["*"],  # 모든 헤더 허용
)


@app.get("/")
async def root():
    return {"message": "Welcome to langgraph-ai-server"}


@app.get("/health")
async def health():
    return JSONResponse(status_code=200, content={"message": "success!"})
