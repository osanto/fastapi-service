from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

if settings.database_url:
    DATABASE_URL = settings.database_url
else:
    DATABASE_URL = (
        f"postgresql://{settings.database_username}:"
        f"{settings.database_password}@"
        f"{settings.database_hostname}:"
        f"{settings.database_port}/"
        f"{settings.database_name}"
    )

if not DATABASE_URL:
    raise RuntimeError("Database configuration is missing")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
