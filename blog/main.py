from fastapi import FastAPI
from . import schemas

app = FastAPI()
  
# create a blog
@app.post('/blog')
def create(request:schemas.Blog):
    return request