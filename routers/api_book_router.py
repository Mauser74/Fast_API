from fastapi import APIRouter, HTTPException, Query
from schemas.book import Book
from models.books_list import books_list


router = APIRouter()


@router.get("/", response_model=list[Book])
async def book_list(
    year: int = Query(None, description="Year of release"),
    title: str = Query(None, description="The title of books")
):
    result = books_list
    # Фильтрация по году и заголовку
    if year is not None:
        result = [book for book in result if book.year == year]
    if title is not None:
        result = [book for book in result if book.title == title]
    return result



@router.get("/{book_id}/", response_model=Book)  # это маршрут для разных путей /book/1 ,  /book/2
async def book_details(book_id: int):
    """Получить детальную информацию по списку"""
    book_id -= 1
    if book_id < 0 or book_id >= len(books_list):
        # Не выходит за пределы списка
        raise HTTPException(status_code=404, detail="Book not found")
    return books_list[book_id]



@router.post("/", response_model=Book, status_code=201)
async def book_create(book: Book):
    """Добавить новую книгу"""
    for m in books_list:
        if m.title == book.title and m.year == book.year:
            raise HTTPException(status_code=409, detail="Book already exists")
    books_list.append(book)
    return book



@router.put("/{book_id}/", response_model=Book)
async def book_update(book_id: int, book: Book):
    """Обновить книгу"""
    book_id -= 1
    if book_id < 0 or book_id >= len(books_list):
        raise HTTPException(status_code=404, detail="Book not found")
    books_list[book_id].title = book.title
    books_list[book_id].year = book.year
    print(books_list)
    return books_list[book_id]



@router.delete("/{book_id}/")
async def book_delete(book_id: int):
    """Удалить книгу"""
    book_id -= 1
    if book_id < 0 or book_id >= len(books_list):
        raise HTTPException(status_code=404, detail="Book not found")

    result = books_list.pop(book_id)

    return {'message': f'Book  {result.title} deleted'}