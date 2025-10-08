# models.py
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    price: float
    description : Optional[str] = None

class User(BaseModel):
    username: str
    email : str
    full_name : Optional[str] = None

# items_router.py
from fastapi import APIRouter
from models import Item

router = APIRouter()

# ENDPOINT PER CREARE L'ARTICOLO
@router.post("/items/")
async def create_item(item: Item):
    return {"name" : item.name}

# users_router.py
from fastapi import APIRouter
from models import User

router = APIRouter()

@router.post("/users/")
async def create_user(user : User):
    return {"name" : user.name}

# main.py
from fastapi import FastAPI
from items_router import router as items_router
from users_router import router as users_router

app = FastAPI()

# INCLUSIONE DEI ROUTER
# IL PREFIX PUÒ ESSERE OMESSO OPPURE DEFINITO DENTRO APIRouter(prefix="/name")
app.include_router(items_router, prefix="/items", tags=["items"])
app.include_router(users_router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message" : "Welcome to the API"}