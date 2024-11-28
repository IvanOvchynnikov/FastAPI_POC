from sqlmodel import Session, select
from src.db.models import Author

# Fetch all authors
def get_authors(session: Session):
    return session.exec(select(Author)).all()

# Create a new author
def create_author(session: Session, author: Author):
    session.add(author)
    session.commit()
    session.refresh(author)
    return author
