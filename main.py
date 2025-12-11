from fastapi import FastAPI
from routers.book_router import router as books_router
from routers.api_book_router import  router as api_books_router
import uvicorn

app = FastAPI()

# Роутеры
app.include_router(api_books_router, tags=["api_books"], prefix="/api")
app.include_router(books_router, tags=["books"])


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
