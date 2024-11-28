from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class Genre(SQLModel, table=True):
    __tablename__ = "genres"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Author(SQLModel, table=True):
    __tablename__ = "authors"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    books: List["Book"] = Relationship(back_populates="author")


class Book(SQLModel, table=True):
    __tablename__="books"
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    published_year: Optional[int] = None
    author_id: int = Field(foreign_key="authors.id")
    genre_id: int = Field(foreign_key="genres.id")
    author: Optional[Author] = Relationship(back_populates="books")
    genre: Optional[Genre] = Relationship()
