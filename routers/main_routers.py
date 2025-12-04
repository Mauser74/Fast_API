from fastapi import APIRouter
from models.books_list import books_list


router = APIRouter()


@router.get("/")
async def index():
    return {"message": "Hello World",
            "books": books_list
            }



@router.get("/about/")
async def about_us():
    return {"message": "О нас",
            "author": "Семенов Владимир",
            "product": "Онлайн картотека библиотеки",
            "address": "Г. Нижний Новгород, ул. Максима Горького, дом 15, Библиотека №17"
            }
