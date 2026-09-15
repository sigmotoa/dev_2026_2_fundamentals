from fastapi import FastAPI
from model import PokemonBase, PokemonCatched




pokemons:PokemonBase = []

app = FastAPI()

@app.get("/pokemons/v1", response_model=list[PokemonCatched])
def show():
    return pokemons

@app.get("/pokemons/v1/{id}", response_model=PokemonCatched)
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
def catch_pokemon(new_pk:PokemonBase):
    catched = new_pk
    pokemons.append(new_pk)
    return catched


@app.patch("/pokemons")
def modifie_pokemon(id:int, new_name:str):
    old_name = pokemons[id].name
    pokemons[id].name=new_name
    return {f"The new pokemon for {old_name} now is named as {pokemons[id].name}"}


@app.delete("/pokemons")
def delete_pokemon(id:int):
    pokemons.pop(id)
    return {"Job has been done"}


