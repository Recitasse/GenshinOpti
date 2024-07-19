from dataclasses import dataclass
from abc import ABC
from typing import Union, Optional, Tuple
from elements import Element_t, Element, DENDRO, ELECTRO, PYRO
from reaction import Reaction_t, Elargissement, Aggravation, Bourgeon, Hyperbourgeonnement
from utils._typing import float16_t


@dataclass(order=False)
class Aura(ABC):
    ...


@dataclass(order=False)
class Accelerer(Aura):
    def __add__(self, other: Union['Element', 'Reaction_t']) -> Tuple[Reaction_t, float16_t, Optional['Element_t']]:
        if other == DENDRO:
            return Elargissement, float16_t(1.0), DENDRO
        if other == ELECTRO:
            return Aggravation, float16_t(1.0), ELECTRO


@dataclass(order=False)
class Bourgeonner(Aura):
    def __add__(self, other: Union['Element', 'Reaction_t']) -> Tuple[Reaction_t, float16_t, Optional['Element_t']]:
        if other == PYRO:
            return Bourgeon, float16_t(1.0), PYRO
        if other == ELECTRO:
            return Hyperbourgeonnement, float16_t(1.0), ELECTRO
