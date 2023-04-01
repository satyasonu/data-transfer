from random import randrange
from typing import Optional
from fastapi import FastAPI, Response, HTTPException, status, Depends
from fastapi.params import Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor #to show column name
import time
from . import models
from .databse import engine, get_db
from sqlalchemy.orm import Session
import logging
#Server running command - uvicorn app.main:app --reload

# Run to store log in log path --  uvicorn app.main:app --log-config ./app/log.ini

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://medium.com/1mgofficial/how-to-override-uvicorn-logger-in-fastapi-using-loguru-124133cdcd4e -- check it tomorrow...

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
while True:

    try:
        conn = psycopg2.connect(host='20.74.186.220',database='fastapi',user='postgres',password='9853', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        # print("Database connection is successfull!")
        logging.info("Database connection is successfull!")
        break
    except Exception as error:
        time.sleep(2)
        logging.error("Check DB is not up!")
        print("DB Conn failed")
        print("Error:", error)


@app.get("/")
def root():
    return {"message": "Hello Panda"}

@app.get("/sqlalchemy")
def test_posts(response: Response,db: Session = Depends(get_db)):
    try:
        posts = db.query(models.Post).all()
        # print(response)
        # logging.info(posts)
        return{"status": posts}
    except Exception as error:
        logging.error(error)



@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts ORDER BY id ASC;""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return {"data":posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post:Post, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s,%s,%s) RETURNING *"""%
    #                (post.title, post.content, post.published ))
    # new_post = cursor.fetchone()
    # conn.commit()
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message": new_post}

@app.get("/posts/latest")
def get_latest_post(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts ORDER BY id ASC;""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    latest_post = posts[len(posts)-1]
    return {"Latest Post": latest_post}

@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = (%s);"""% (str(id)))
    # one_post = cursor.fetchone()
    one_post = db.query(models.Post).filter(models.Post.id == id).first()
    if not one_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"post with id: {id} was not found")
    return {"post_detail": one_post}

@app.delete("/posts/{id}")
def delete_post(id : int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = (%s) RETURNING *"""% (str(id)))
    # delete_post = cursor.fetchone()
    # conn.commit()
    delete_post = db.query(models.Post).filter(models.Post.id == id)
    if delete_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id {id} does not exists")
    delete_post.delete(synchronize_session = False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int,post: Post, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title= (%s), content= (%s), published= (%s) WHERE id = (%s) RETURNING *"""% (post.title, post.content, post.published, (str(id))))
    # updated_post = cursor.fetchone()
    # conn.commit()
    # index = find_index_post(id)
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post1 = post_query.first()

    if post1 == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id {id} does not exists")
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return {"data":post_query.first()}
