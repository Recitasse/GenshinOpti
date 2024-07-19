from dataclasses import dataclass, InitVar, field
from abc import ABC, abstractmethod
from typing import final, Self, Union, NewType


@dataclass(order=False)
class Reaction(ABC):
    ...


@dataclass(order=False)
class Fonte(Reaction):
    ...


@dataclass(order=False)
class Evaporation(Reaction):
    ...


@dataclass(order=False)
class Elargissement(Reaction):
    ...


@dataclass(order=False)
class Surcharge(Reaction):
    ...


@dataclass(order=False)
class Brulure(Reaction):
    ...


@dataclass(order=False)
class Bourgeonnement(Reaction):
    ...


@dataclass(order=False)
class Hyperbourgeonnement(Reaction):
    ...


@dataclass(order=False)
class Gel(Reaction):
    ...


@dataclass(order=False)
class Electrocution(Reaction):
    ...


@dataclass(order=False)
class Brulure(Reaction):
    ...


@dataclass(order=False)
class Bourgeon(Reaction):
    ...


@dataclass(order=False)
class Acceleration(Reaction):
    ...


@dataclass(order=False)
class Supraconduction(Reaction):
    ...


@dataclass(order=False)
class Acceleration(Reaction):
    ...


@dataclass(order=False)
class Aggravation(Reaction):
    ...


@dataclass(order=False)
class Bourgeon(Reaction):
    ...


@dataclass(order=False)
class Cristallisation(Reaction):
    ...


@dataclass(order=False)
class Dispersion(Reaction):
    ...


Reaction_t = NewType('Reaction', Union[
    Acceleration,
    Aggravation,
    Bourgeon,
    Bourgeonnement,
    Brulure,
    Cristallisation,
    Dispersion,
    Elargissement,
    Electrocution,
    Evaporation,
    Fonte,
    Gel,
    Hyperbourgeonnement,
    Reaction,
    Supraconduction,
    Surcharge
])


__all__ = [
    "Acceleration",
    "Aggravation",
    "Bourgeon",
    "Bourgeonnement",
    "Brulure",
    "Cristallisation",
    "Dispersion",
    "Elargissement",
    "Electrocution",
    "Evaporation",
    "Fonte",
    "Gel",
    "Hyperbourgeonnement",
    "Reaction_t",
    "Supraconduction",
    "Surcharge"
]
