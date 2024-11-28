from sqlmodel import Session, select
from src.db.models import Book, Genre, Author


# Fetch all books
def get_books(session: Session):
    return session.exec(select(Book)).all()


# Fetch a single book by ID
def get_book_by_id(session: Session, book_id: int):
    return session.get(Book, book_id)


# Create a new book
def create_book(session: Session, book: Book):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


# Update an existing book
def update_book(session: Session, book_id: int, book: Book):
    db_book = session.get(Book, book_id)
    if not db_book:
        return None
    for key, value in book.dict(exclude_unset=True).items():
        setattr(db_book, key, value)
    session.commit()
    session.refresh(db_book)
    return db_book


# Delete a book
def delete_book(session: Session, book_id: int):
    db_book = session.get(Book, book_id)
    if not db_book:
        return None
    session.delete(db_book)
    session.commit()
    return db_book


def get_books_detailed(session: Session):
    statement = select(Book, Author, Genre).join(Author).join(Genre)
    result = session.exec(statement).all()

    books_with_details = []
    for book, author, genre in result:
        books_with_details.append({
            "id": book.id,
            "title": book.title,
            "published_year": book.published_year,
            "author": {
                "id": author.id,
                "name": author.name,
            },
            "genre": {
                "id": genre.id,
                "name": genre.name
            }
        })

    return books_with_details
