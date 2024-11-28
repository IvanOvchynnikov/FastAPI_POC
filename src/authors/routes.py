from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.db.main import get_session
from src.db.models import Author
from src.authors.crud import get_authors, create_author

authors_router = APIRouter()

@authors_router.get("/authors", response_model=list[Author])
def list_authors(session: Session = Depends(get_session)):
    return get_authors(session)

@authors_router.post("/authors", response_model=Author)
def create_new_author(author: Author, session: Session = Depends(get_session)):
    return create_author(session, author)
