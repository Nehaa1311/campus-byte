import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Locally we use a simple SQLite file. In Docker we'll switch to PostgreSQL
# just by setting the DATABASE_URL environment variable.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./campus_byte.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


# Each API request gets its own database session, closed when the request ends.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()