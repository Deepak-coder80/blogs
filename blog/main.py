from fastapi import FastAPI,Depends
from . import schemas
from . import database
from . import models
from sqlalchemy.orm import Session
app = FastAPI()
  
models.Base.metadata.create_all(database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

# create a blog
@app.post('/blog',status_cod=201)
def create(request:schemas.Blog,db:Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


#get all blogs
@app.get('/blogs')
def all(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

#get blog by id
@app.get('/blog/{id}')
def blogById(id,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    return blog