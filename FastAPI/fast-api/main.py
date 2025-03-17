from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app=FastAPI()

# @app.get('/blog')
# def index():
#     return {'data':'Blog List'}

#using query parameter
# query params are becoming required

# @app.get('/blog')
# def index(limit,published:bool):
#     if published:
#       return {'data':f'published Blog List is limited to {limit} '}
#     else:
#       return {'data':f'Unpublished Blog List is limited to {limit} '}
  
# Defaulting Parameters with some value  and makng few params as optional

@app.get('/blog')
def index(limit=100,published:bool=False,sort:Optional[str]=None):
    if published:
      return {'data':f'published Blog List is limited to {limit} '}
    else:
      return {'data':f'Unpublished Blog List is limited to {limit} '}


@app.get('/blog/unpublished')
def displayUnpublishedBlog():
    return {'data':{"All Un Published Blogs"}}

@app.get('/blog/{id}')
def displayBlog(id:int):
    return {'data':id}



# Fats APi can identify whether provided  params are path params or query params
@app.get('/blog/{id}/Comments')
def displayBlogComments(id,limit=10):
    return {'data': "Comments for"+ id}


class Blog(BaseModel):
    title:str 
    body:str 
    published:Optional[bool]


@app.post('/blog')
def createBlog(request:Blog):
    return {'data':f"Blog is created with title as {request.title}"}


