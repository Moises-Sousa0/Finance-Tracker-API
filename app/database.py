from dotenv import load_dotenv

from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() #permite criar e ver as tabelas com python


def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()