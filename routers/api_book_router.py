from fastapi import APIRouter, HTTPException, Query
from schemas.book import Book
from models.books_list import books_list


router = APIRouter()


@router.get("/", response_model=list[Book])
async def api_book_list(
    year: int = Query(None, description="Год издания"),
    publishing: str = Query(None, description="Издательство")
)->list[Book]:
    """"Фильтрация списка книг по году и издательству"""
    result = books_list
    # Фильтрация по году и издательству
    if year is not None:
        result = [book for book in result if book.year == year]
    if publishing is not None:
        result = [book for book in result if book.publishing == publishing]
    return result



@router.get("/{book_id}/", response_model=Book)  # это маршрут для разных путей /book/1 ,  /book/2
async def api_book_details(book_id: int)->Book:
    """Получить детальную информацию по книге"""
    index = find_index_by_id(books_list, book_id)

    if index is not None:
        return books_list[index]

    raise HTTPException(status_code=404, detail="Book not found")



@router.post("/", response_model=Book, status_code=201)
async def book_create(book: Book)->Book:
    """Добавление новой книги"""
    for item in books_list:
        if item.title == book.title and item.year == book.year:
            raise HTTPException(status_code=409, detail="Book already exists")
    # Присваиваем id
    max_id = max(item.id for item in books_list)
    book.id = max_id + 1
    books_list.append(book)
    return book



@router.put("/{book_id}/", response_model=Book)
async def book_update(book_id: int, book: Book)->list[Book]:
    """Обновление существующей книги"""
    index = find_index_by_id(books_list, book_id)

    if index is not None:
        books_list[index] = book
        return books_list[index]

    raise HTTPException(status_code=404, detail="Book not found")



@router.delete("/{book_id}/")
async def book_delete(book_id: int):
    """Удалить книгу"""
    index = find_index_by_id(books_list, book_id)

    if index is not None:
        result = books_list.pop(index)
        return {'message': f'Book {result.title} deleted'}

    raise HTTPException(status_code=404, detail="Book not found")




def find_index_by_id(item_list: list, id: int)->int | None:
    """"Поиск индекса в списке по совпадению id"""
    for index, item in enumerate(item_list):
        if item.id == id:
            return index

    return None