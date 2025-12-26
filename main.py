# main.py
from fastapi import FastAPI
from pydantic import BaseModel

# Creo l'app FastAPI
app = FastAPI()

# --- ROUTE BASE ---
@app.get("/")
def home():
    return {"message": "Hello from Python 3.14!"}

# --- ROUTE CON PARAMETRO URL ---
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

# --- ROUTE POST CON JSON ---
# Definisco un modello dati
class Item(BaseModel):
    name: str
    quantity: int

@app.post("/items/")
def create_item(item: Item):
    return {
        "message": f"Received item {item.name} with quantity {item.quantity}"
    }

# --- ROUTE DI TEST ---
@app.get("/status")
def status():
    return {"status": "ok", "python_version": "3.14"}
