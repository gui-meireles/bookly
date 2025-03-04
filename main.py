from typing import List

from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-01",
        "page_count": 464,
        "language": "English"
    },
    {
        "id": 2,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt, David Thomas",
        "publisher": "Addison-Wesley",
        "published_date": "1999-10-20",
        "page_count": 352,
        "language": "English"
    },
    {
        "id": 3,
        "title": "Design Patterns",
        "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        "publisher": "Addison-Wesley",
        "published_date": "1994-10-21",
        "page_count": 416,
        "language": "English"
    },
    {
        "id": 4,
        "title": "Introduction to the Theory of Computation",
        "author": "Michael Sipser",
        "publisher": "Cengage Learning",
        "published_date": "2005-02-15",
        "page_count": 480,
        "language": "English"
    },
    {
        "id": 5,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2019-05-03",
        "page_count": 544,
        "language": "English"
    },
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


@app.get('/books', response_model=List[Book])
async def get_all_books():
    return books


@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()

    books.append(new_book)
    return new_book


@app.get('/book/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")


@app.patch('/book/{book_id}')
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['author'] = book_update_data.author
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return book

    raise HTTPException(status_code=404, detail="Book not found")


@app.delete('/book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}

    raise HTTPException(status_code=404, detail="Book not found")
