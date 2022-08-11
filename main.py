# import fast api
from fastapi import FastAPI

# create app
app = FastAPI()

#define the route
@app.get("/")
# function
async def index():
    return {'data':{'name':'Deepak'}};
