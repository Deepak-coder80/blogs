# import fast api
from fastapi import FastAPI

# create app
app = FastAPI()

#define the route
@app.get("/")
# function
async def index():
    return {'data':{'name':'Deepak'}};


#another route
@app.get("/about")
def about():
    return {'data':{'about page'}}
