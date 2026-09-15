from fastapi import FastAPI
from models import PokemonBase,PokemonCatched, PokemonUpdated
from poke_types import Poke_type






pokemons = [
    PokemonBase(id=1, name="Bulbasaur", type=Poke_type.LEAF),
    PokemonBase(id=2, name="Ivysaur", type="Leaf"),
    PokemonBase(id=3, name="Venusaur", type="Leaf"),
    PokemonBase(id=4, name="Charmander", type=Poke_type.FIRE),
    PokemonBase(id=5, name="Charmeleon", type=Poke_type.FIRE),
    PokemonBase(id=6, name="Charizard", type=Poke_type.FIRE),
    PokemonBase(id=7, name="Squirtle", type=Poke_type.WATER),
    PokemonBase(id=8, name="Wartortle", type=Poke_type.WATER),
    PokemonBase(id=9, name="Blastoise", type=Poke_type.WATER),
    PokemonBase(id=10, name="Caterpie", type=Poke_type.BUG),
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


@app.post("/pokemons", response_model=PokemonCatched)
def catch_pokemon(pk1:PokemonBase):
    pokemons.append(pk1)
    return pk1

@app.patch("/pokemons", response_model=PokemonBase)
def update_pokemon(id:int, updated:PokemonUpdated):
    #old_name = pokemons[id].name
    pokemons[id].status=updated.status
    return pokemons[id]


@app.delete("/pokemons")
def remove_pokemon(id:int):
    old = pokemons[id]
    pokemons.pop(id)
    return f"{old} has been removed"





