from fastapi import FastAPI
from . import schemas
from . import database
from . import models

app = FastAPI()
  
models.Base.metadata.create_all(database.engine)
# create a blog
@app.post('/blog')
def create(request:schemas.Blog):
    return request