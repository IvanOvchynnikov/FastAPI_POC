from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.db.main import get_session
from src.db.models import Genre
from src.genres.crud import get_genres, create_genre

genres_router = APIRouter()

@genres_router.get("/genres", response_model=list[Genre])
def list_genres(session: Session = Depends(get_session)):
    return get_genres(session)

@genres_router.post("/genres", response_model=Genre)
def create_new_genre(genre: Genre, session: Session = Depends(get_session)):
    return create_genre(session, genre)
