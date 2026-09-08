from fastapi import FastAPI
from pydantic import BaseModel

class Type(BaseModel):
    id:int
    name:str

class Pokemon(BaseModel):
    id:int
    name:str
    type:Type

leaf=Type(id=1,name="Leaf")
fire=Type(id=2,name="Fire")
water=Type(id=3,name="Water")
bug=Type(id=4,name="Bug")
ghost=Type(id=5,name="Ghost")

types=[leaf,fire,water,bug,ghost]

pokemons = [
    Pokemon(id=1, name="Bulbasaur", type=types[0]),
    Pokemon(id=2, name="Ivysaur", type=types[0]),
    Pokemon(id=3, name="Venusaur", type=types[0]),
    Pokemon(id=4, name="Charmander", type=types[1]),
    Pokemon(id=5, name="Charmeleon", type=types[1]),
    Pokemon(id=6, name="Charizard", type=types[1]),
    Pokemon(id=7, name="Squirtle", type=types[2]),
    Pokemon(id=8, name="Wartortle", type=types[2]),
    Pokemon(id=9, name="Blastoise", type=types[2]),
    Pokemon(id=10, name="Caterpie", type=types[3]),
]

app = FastAPI()

@app.get("/pokemons/v1")
def show():
    return pokemons

@app.get("/pokemons/v1/{id}")
def show_one(id:int):
    return pokemons[id]

@app.get("/pokemons/v2/{id}")
def show_one_p(id:int):
    for pokemon in pokemons:
        if pokemon.id==id:
            return pokemon.model_dump()
    return {"error":"pokemon didnt find"}

@app.get("/pokemons/v3")
def show_one(id:int):
    return pokemons[id]

@app.get("/pokemons/v4")
def list_query(step:int, final:int):
    return pokemons[step:step+final]


@app.get("/pokemons/v4/{step}/{final}")
def list_path(step:int, final:int):
    return pokemons[step:step+final]


@app.post("/pokemons")
def catch_pokemon(pk1:Pokemon):
    pokemons.append(pk1)
    return pokemons[-1]

@app.patch("/pokemons")
def update_pokemon(id:int, name:str):
    old_name = pokemons[id].name
    pokemons[id].name=name
    return f"{"El pokemon antes conocido como: {old_name} ahora se llama {pokemons[id].name}"}"


@app.delete("/pokemons")
def remove_pokemon(id:int):
    old = pokemons[id]
    pokemons.pop(id)
    return f"{old} has been removed"





