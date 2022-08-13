# import fast api
from fastapi import FastAPI

#optional
from typing import Optional

# create app
app = FastAPI()

#define the route
@app.get("/blog")
# function
def index(limit=10,published:bool=True,sort:Optional[str]= None):
    if published:
        return {'data':f'{limit} published blogs from db'}

@app.get('/blog/unpublished')
async def unpublished():
    return {'data':'all unpublished blogs'}

#another route
@app.get("/blog/{id}")
def show(id:int):
    return {'data':id}



# commmets sections
@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog wiht id=id 
    return {'data':'comments'}
