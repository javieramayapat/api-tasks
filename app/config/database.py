from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}"

# Create SQLAlchemy Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is an instance of declarative _base() which return a class
# Wich is going to be inherit to create our databse models (The ORM models)
Base = declarative_base()