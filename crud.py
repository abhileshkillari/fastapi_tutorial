from fastapi import FastAPI,status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
books = [
    {
        "id": 1,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "publish_date": "1998-01-01"
    },
    {
        "id": 2,
        "title": "Atomic Habits",
        "author": "James Clear",
        "publish_date": "2018-10-16"
    },
    {
        "id": 3,
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "publish_date": "1997-04-01"
    },
    {
        "id": 4,
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "publish_date": "1997-09-29"
    }
]

app= FastAPI()
@app.get("/book")
def get_book():
  return books

@app.get("/books/{book_id}")
def getbookbyid(book_id:int):
  for book in books:
    if book["id"]==book_id:
      return book
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found")

class Book(BaseModel):
  id:int
  title:str
  author:str
  publish_date:str

@app.post("/book")
def add_book(book:Book):
  new_book=book.model_dump()
  books.append(new_book)


class Bookupdate(BaseModel):
  title:str
  author:str
  publish_date:str

@app.put("/book/{book_id}")
def update_book(book_id:int,book_update:Bookupdate):
  for book in books:
    if book["id"]==book_id:
      book["title"]=book_update.title
      book["author"]=book_update.author
      book["publish_date"]=book_update.publish_date
      return book
  raise HTTPException(status.HTTP_403_FORBIDDEN,detail="No book found")

@app.delete("/book/{book_id}")
def delete_book(book_id:int):
  for book in books:
    if book["id"]==book_id:
      books.remove(book)
      return {"message":"book is removed"}
  raise HTTPException(status.HTTP_400_BAD_REQUEST,detail="no book existed")