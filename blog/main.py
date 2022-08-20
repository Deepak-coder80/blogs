from fastapi import FastAPI,Depends,status
import schemas
import database
import models
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
@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}')
def destroy(id:int,db:Session=Depends(get_db)):
    blog_d=db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return {'status':'done','content':blog_d}

@app.put('/blog/{id}')
def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
       db.query(models.Blog).filter(models.Blog.id==id).update({models.Blog.title:request.title})


# get all blogs
@app.get('/blogs')
def all(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

# get blog by id
@app.get('/blog/{id}')
def blogById(id,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    return blog

@app.post('/user')
def create_user(request: schemas.User,db: Session=Depends(get_db)):
    new_user =  models.User(name=request.name,email=request.email,password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return  new_user

@app.get('/users')
def get_all_users(db:Session=Depends(get_db)):
    user = db.query(models.User).all()
    return  user;