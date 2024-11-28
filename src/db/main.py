from sqlmodel import create_engine, SQLModel, Session

from src.config import Config

engine = create_engine(
    url=Config.DB_URL,
    echo=True
)

def init_db() -> None:
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    with Session(engine) as session:
        yield session
