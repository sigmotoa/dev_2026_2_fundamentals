from pydantic import BaseModel
<<<<<<< HEAD
from poke_types import Poke_type
=======
from poke_types import Poke_types
>>>>>>> main

class PokemonBase(BaseModel):
    id:int
    name:str
<<<<<<< HEAD
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
=======
    alive:bool
    type:Poke_types
    can_evolve:bool

class PokemonCatched(BaseModel):
    id:int
    name:str
    type:Poke_types
>>>>>>> main
