from dataclasses import dataclass, field, InitVar
from abc import ABC, abstractmethod
from typing import ClassVar, Dict, Tuple, Any
from utils._typing import *


@dataclass(order=False)
class Weapon(ABC):
    # metadata
    name: str = field(init=False)
    dgt: float16 = field(init=False)
    lvl: uint8 = field(init=False)
    ascension: uint8 = field(init=False)
    rarity: Rarity_t = field(init=False)
