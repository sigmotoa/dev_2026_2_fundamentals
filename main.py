from fastapi import FastAPI
#from pydantic import BaseModel
from model import PokemonBase, PokemonCatched

pokemons:PokemonBase = []

app = FastAPI()

@app.get("/pokemons/v1", response_model=list[PokemonCatched])
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

@app.post("/pokemons", response_model=PokemonCatched)
def catch_pokemon(p_n:PokemonBase):
    new_pokemon = p_n
    pokemons.append(new_pokemon)
    return new_pokemon

@app.patch("/pokemons")
def update_pokemon(id:int, name:str):
    
    for pokemon in pokemons:
            if pokemon.id==id:
                pokemons[pokemon.id].name=name
                
                break
    return pokemons[id+1]

@app.delete("/pokemons")
def kill_pokemon(id:int):
    pokemons.pop(id)
    return {"bye bye":"bye bye"}





