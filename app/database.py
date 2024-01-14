import os
from sqlalchemy import (Column, Integer, String, Table, create_engine, MetaData)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from databases import Database

#DATABASE_URL = "postgresql://postgres:deko@localhost:5432/python_db"
#DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:deko@localhost:5432/python_db")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://hello_fastapi:hello_fastapi@postgres:5432/hello_fastapi_dev")

#DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:deko@localhost/python_db")
load_dotenv()
engine =create_engine(DATABASE_URL,echo=True, 
    )
metadata = MetaData()
SessionLocal= sessionmaker(autocommit =False, autoflush= False, bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
database = Database(DATABASE_URL)