
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

from products.products_api import product_router
from user.user_api import user_router

from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(product_router)

app.get('/test')


async def test():
    return 'Test page'
