from pydantic import BaseModel
from typing import Optional

from src.authors.schemas import AuthorBase
from src.genres.schemas import GenreBase


class BookBase(BaseModel):
    id: int
    title: str
    published_year: Optional[int] = None
    author: AuthorBase
    genre: GenreBase

