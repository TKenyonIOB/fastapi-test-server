from typing import Union
from random import randint
import os
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
# from fastapi import FastAPI
from db_secrets import *
# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USER}:{DB_USER_PW}@{DB_URL}:{5432}/{DB}'
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db(): #We call this function every time we get a API request that requires db access
    db = SessionLocal() #this object actually talks to the db.
    try:
        yield db
    finally:
        print("connected!")
        db.close()


while True:
    datetime = time.time()
    time.sleep(float(randint(1,10)))
    fishes = randint(1,100)
    time_inserted = time.time()
    text = f"{str(fishes)} mississippi"
    print(time_inserted)