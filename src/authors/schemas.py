from pydantic import BaseModel


class AuthorBase(BaseModel):
    id: int
    name: str