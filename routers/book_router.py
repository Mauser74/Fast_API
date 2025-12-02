from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
#from schemas.book import Book
from models.books_list import books_list


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def book_list(request: Request):
    context = {
        "request": request,
        "title": "Список наших книг ",
        "text": "Описание страницы",
        "books": books_list,
    }

    return templates.TemplateResponse("books_list.html", context=context)



@router.get("/{book_id}/", response_class=HTMLResponse)
async def movie_details(request: Request, book_id: int):
    """Получить детальную информацию по списку"""
    book_id -= 1
    if book_id < 0 or book_id >= len(books_list):
        raise HTTPException(status_code=404, detail="Book not found")

    context = {
        "request": request,
        "text": "Описание страницы",
        "book": books_list[book_id],
    }

    return templates.TemplateResponse("book_detail.html", context=context)
