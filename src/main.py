from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.authors.routes import authors_router
from src.books.routes import books_router
from src.db.main import init_db
from src.genres.routes import genres_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="POC",
    description="FastAPI POC",
    version="v1",
    lifespan=lifespan,
)

app.include_router(books_router, prefix="/api")
app.include_router(authors_router, prefix="/api")
app.include_router(genres_router, prefix="/api")
