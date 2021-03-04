from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
# import datetime
import uvicorn


app = FastAPI()

@app.get('/blog')
def index(limit, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} blog from the db'}
    else:
        return {'data': f'{limit}'}

@app.get('blog/un')
def unpublished():
    
    return {'data': 'allunpublished'}
    

    
@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit = 10):
    return{'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    # date: datetime.datetime.now()

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f"Blog is created with title as {request.title }"}

#
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port= '9000')