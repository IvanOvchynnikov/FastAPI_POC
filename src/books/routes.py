from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from src.books.schemas import BookBase
from src.db.main import get_session
from src.db.models import Book
from src.books.crud import (
    get_books,
    get_book_by_id,
    create_book,
    update_book,
    delete_book, get_books_detailed,
)

books_router = APIRouter()


@books_router.get("/books", response_model=list[Book])
def list_books(session: Session = Depends(get_session)):
    return get_books(session)


@books_router.get("/books/{book_id}", response_model=Book)
def retrieve_book(book_id: int, session: Session = Depends(get_session)):
    book = get_book_by_id(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@books_router.post("/books", response_model=Book)
def create_new_book(book: Book, session: Session = Depends(get_session)):
    return create_book(session, book)


@books_router.put("/books/{book_id}", response_model=Book)
def modify_book(book_id: int, book: Book, session: Session = Depends(get_session)):
    updated_book = update_book(session, book_id, book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@books_router.delete("/books/{book_id}")
def remove_book(book_id: int, session: Session = Depends(get_session)):
    deleted_book = delete_book(session, book_id)
    if not deleted_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}


@books_router.get("/books_detailed", response_model=list[BookBase])
def list_books_detailed(session: Session = Depends(get_session)):
    books = get_books_detailed(session)
    return books
