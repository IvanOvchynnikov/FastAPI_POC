from sqlmodel import Session, select
from src.db.models import Genre

# Fetch all genres
def get_genres(session: Session):
    return session.exec(select(Genre)).all()

# Create a new genre
def create_genre(session: Session, genre: Genre):
    session.add(genre)
    session.commit()
    session.refresh(genre)
    return genre
