from pydantic import BaseModel


class Book(BaseModel):
    id: int
    author: str
    title: str
    year: int
    publishing: str
    isbn: str
    description: str
