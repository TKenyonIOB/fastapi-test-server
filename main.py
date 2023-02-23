from typing import Union
from random import randint
import os
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
# from fastapi import FastAPI
from db_secrets import *
# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USER}:{DB_USER_PW}@{DB_URL}:{5432}/{DB}'
# print(SQLALCHEMY_DATABASE_URL)

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

try:
    conn = psycopg2.connect(host=DB_URL,database=DB,user=DB_USER,password=DB_USER_PW, cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print('database connection was successful')
except Exception as error:
    print('connection failed')
    print("Error: ", error)



while True:
    datetime_ = datetime.now()
    time.sleep(float(randint(1,10)))
    fishes = randint(1,100)
    time_inserted = datetime.now()
    text = f"{str(fishes)} mississippi"
    #print(time_inserted)
    print(f"INSERT INTO public.fish_table (fishes, text_field, datetime, time_inserted) VALUES ({fishes}, '{text}', '{datetime_}', '{time_inserted}') RETURNING *")
    cursor.execute(f"INSERT INTO public.fish_table (fishes, text_field, datetime, time_inserted) VALUES ({fishes}, '{text}', '{datetime_}', '{time_inserted}') RETURNING *") #Usage of fstrings here would make system vulnerable to sql injection. By using this method we ensure our sql library 'sanitizes' the inputs
    new_post = cursor.fetchone() #fetches the post we just created and saves into variable
    conn.commit() #This is when the actual changes to the database are made (the post is added)
    print(f"sucessfully inserted {new_post}")