# ESEMPIO 1
# dependecipes.py
from typing import Dict

def get_db_config() -> Dict:
    return {
        "db_url": "localhost:5432",
        "db_name": "my_database"
    }

# main.py
from fastapi import FastAPI, Depends
from dependencies import get_db_config

app = FastAPI()

@app.get("/db-info/")
async def read_db_info(db_config: Dict = Depends(get_db_config)):
    return {"db_url": db_config["db_url"], "db_name": db_config["db_name"]}


# ESEMPIO 2
# models.py
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


# dependencies.py
from models import Item
from fastapi import HTTPException, Depends

def get_item_from_request(item: Item = Depends()) -> Item:
    if item.price <= 0:
        raise HTTPException(status_code=400, detail="Price must be greater than 0")
    return item

# main.py
from fastapi import FastAPI, Depends
from models import Item
from dependencies import get_item_from_request

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item = Depends(get_item_from_request)):
    return {"name": item.name, "price": item.price, "description": item.description}
