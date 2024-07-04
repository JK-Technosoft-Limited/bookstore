from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import Field, SQLModel

DATABASE_URL = "sqlite:///./test.db"  # Example using SQLite
Base = declarative_base()


class UserCredentials(SQLModel, table=True):
    __tablename__ = "user_credentials"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    email: str = Field(index=True, unique=True)
    password: str


class Book(SQLModel, table=True):
    __tablename__ = "books"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(index=True)
    author: str = Field(index=True)
    published_year: int
    book_summary: str


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SQLModel.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
