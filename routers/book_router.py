from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models.books_list import books_list
from view import text


router = APIRouter()
# Указываем путь где лежат шаблоны
templates = Jinja2Templates(directory="templates")



@router.get("/", response_class=HTMLResponse)
async def book_list(request: Request):
    """"Главная страница со списком книг"""
    context = {
        "request": request,
        "name": text.org_name,
        "items_name": text.items_name,
        "books": books_list
    }
    return templates.TemplateResponse("books_list.html", context=context)



@router.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    """Страница О библиотеке"""
    context = {
        "request": request,
        "name": text.org_name,
        "items_name": text.about_name,
    }
    return templates.TemplateResponse("about.html", context=context)



@router.get("/{book_id}/", response_class=HTMLResponse)
async def book_details(request: Request, book_id: int):
    """Страница с детальной информацией о книге"""
    for index, book in enumerate(books_list):
        if book.id == book_id:
            context = {
                "request": request,
                "name": text.org_name,
                "items_name": text.detail_name,
                "book": books_list[index],
            }
            return templates.TemplateResponse("book_detail.html", context=context)

    raise HTTPException(status_code=404, detail="Book not found")
