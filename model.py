from pydantic import BaseModel
from poke_types import Poke_type

class PokemonBase(BaseModel):
    id:int
    name:str
    lvl:int
    type_1:Poke_type
    type_2:Poke_type | None = None
    #types:Poke_type = [2]
    is_alive:bool
    have_evolve:bool

class PokemonCatched(BaseModel):
    name:str
    type_1:Poke_type
    type_2:Poke_type