from fastapi import FastAPI
from starlette.responses import HTMLResponse

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



@app.get('/books')
async def get_all_books():
    return books


@app.post('/books')
async def create_a_book() -> dict:
    pass

@app.get('/book/{book_id}')
async def get_book(book_id: int) -> dict:
    pass

@app.get('/book/{book_id}')
async def update_book(book_id: int) -> dict:
    pass

@app.get('/book/{book_id}')
async def delete_book(book_id: int) -> dict:
    pass