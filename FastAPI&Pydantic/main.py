# ESEMPIO 1
from fastapi import FastAPI
# PER INDICARE CHE UN PARAMETRO PUÒ ESSERE FACOLTATIVO (NONE)
from typing import Optional

# CREAZIONE ISTANZA FASTAPI (APPLICAZIONE WEB)
app = FastAPI()

# DECORATORE CHE INDICA CHE LA FUNZIONE read_root() GESTISCE RICHIESTE GET ALL'ENDPOINT /
@app.get("/")
def read_root():
    return {"Hello" : "World"}

# STESSO DISCORSO DI PRIMA CON PERÒ UNA VARIABILE DINAMICA NEL PERCORSO URL
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = Optional[None]):
    return {"item_id" : item_id, "q" : q}

# ESEMPIO 2
from fastapi import FastAPI
# USATO PER CREARE MODELLI DI DATI CON VALIDAZIONE AUTOMATICA TRAMITE PYDANTIC DEI DATI IN INGRESSO
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# MODELLO DI DATI CHE RAPPRESENTA UN PRODOTTO, PYDANTIC USA I TIPI DICHIARATI PER ESEGUIRE LA VALIDAZIONE IN CASO DI TIPO DIVERSO (ES: NAME != STR)
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = Optional[None]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item): # item È IL CORPO DELLA RICHIESTA INVIATO COME JSON CHE FASTAPI CONVERTE E CONVALIDA IN OGGETTO ITEM
    return {"item_name": item.name, "item_id": item_id}
