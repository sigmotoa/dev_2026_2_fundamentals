from pydantic import BaseModel
from poke_types import Poke_type
from poke_status import Poke_status

class PokemonBase(BaseModel):
    id:int
    name:str
    type:Poke_type
    is_alive:bool=True
    status:Poke_status = Poke_status.DEFAULT

class PokemonCatched(BaseModel):
    name:str
    type:Poke_type
    status:Poke_status


class PokemonUpdated(BaseModel):
    status:Poke_status