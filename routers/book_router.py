from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
#from schemas.book import Book
from models.books_list import books_list
from view import text


router = APIRouter()
# Указываем путь где лежат шаблоны
templates = Jinja2Templates(directory="templates")



@router.get("/", response_class=HTMLResponse)
async def book_list(request: Request):
    context = {
        "request": request,
        "name": text.org_name,
        "items_name": text.items_name,
        "books": books_list
    }
    return templates.TemplateResponse("books_list.html", context=context)



@router.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    context = {
        "request": request,
        "name": text.org_name
    }
    return templates.TemplateResponse("about.html", context=context)



@router.get("/{book_id}/", response_class=HTMLResponse)
async def book_details(request: Request, book_id: int):
    """Получить детальную информацию по списку"""
    for index, book in enumerate(books_list):
        if book.id == book_id:
            context = {
                "request": request,
                "name": text.org_name,
                "book": books_list[index]
            }
            return templates.TemplateResponse("book_detail.html", context=context)

    raise HTTPException(status_code=404, detail="Book not found")
