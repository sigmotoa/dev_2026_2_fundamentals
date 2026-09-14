from pydantic import BaseModel
from poke_types import Poke_types

class PokemonBase(BaseModel):
    id:int
    name:str
    alive:bool
    type:Poke_types
    can_evolve:bool

class PokemonCatched(BaseModel):
    id:int
    name:str
    type:Poke_types