from pydantic import BaseModel


class Blog(BaseModel):
    title:str
    body : str


# class for user
class User(BaseModel):
    name : str
    email : str
    password : str
