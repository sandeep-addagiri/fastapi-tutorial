from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


@app.get('/blog')
def index(limit,published:bool):
    if published:
        return {f'{limit} published blogs list'}
    else:
        return{'all published blogs'}

@app.get('/blog/{id}')
def show(id:int):
    return{'data':id}


@app.get('/blog/unpublished')
def unpublished():
    return{'data':'unpublished'}

class items(BaseModel):
    name:str
    id:int
    branch:str

@app.post('items/')
def create_items(item:items):
    return item
