from pydantic import BaseModel


class Book(BaseModel):
    author: str
    title: str
    year: int
    publishing: str
    isbn: str
    description: str
