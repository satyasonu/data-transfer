from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# host='localhost',database='fastapi',user='postgres',password='9853',
SQLALCHEMY_DATABSE_URL = 'postgresql://postgres:9853@20.74.186.220:5432/fastapi'

engine = create_engine(SQLALCHEMY_DATABSE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()