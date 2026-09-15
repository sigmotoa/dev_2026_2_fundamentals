from enum import Enum

class Poke_status(str, Enum):
    POISSONED="Poisson"
    BURNED="Burned"
    FREEZE="Freeze"
    CONFUSED = "Confused"
    SLEEPY = "Sleepy"
    DEFAULT = "Default"