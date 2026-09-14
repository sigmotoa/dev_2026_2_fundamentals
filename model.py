from pydantic import BaseModel
from poke_types import Poke_types

class Pokemon(BaseModel):
    id:int
    name:str
    alive:bool
    type:Poke_types
    can_evolve:bool