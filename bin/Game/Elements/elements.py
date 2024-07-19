from dataclasses import dataclass, InitVar, field
from reaction import *
from abc import ABC, abstractmethod
from typing import final, Self, Tuple, Optional, NewType, Union
from utils._typing import float16_t


@dataclass(order=False)
class Element(ABC):
    @abstractmethod
    def __add__(self, other: Union['Element', 'Reaction_t']) -> Tuple[Reaction_t, float16_t, Optional['Element_t']]:
        """
        Renvoie la réaction élémentaire entre 2 éléments
        :param other: Element (RÉACTIF) qui réagit à self
        :return: La réaction élémentaire associée
        """
        pass


@dataclass(order=False, slots=True)
class PYRO(Element):
    def __add__(self, other: Union['Element', 'Reaction_t']) -> Tuple[Reaction_t, float16_t, Optional['Element_t']]:
        if other == CRYO:
            return Fonte, float16_t(1.5), None
        elif other == HYDRO:
            return Evaporation, float16_t(2.0), None
        elif other == ELECTRO:
            return Surcharge, float16_t(1.0), None
        elif other == DENDRO:
            return Brulure, float16_t(1.0), None
        elif other == GEO:
            return Cristallisation, float16_t(1.0), None
        elif other == ANEMO:
            return Dispersion, float16_t(1.0), None


@dataclass(order=False, slots=True)
class CRYO(Element):
    def __add__(self, other: Union['Element', 'Reaction_t']) -> Tuple[Reaction_t, float16_t, Optional['Element_t']]:
        if other == PYRO:
            return Fonte, float16_t(2.0), None
        elif other == GEO:
            return Cristallisation, float16_t(1.0), None
        elif other == ANEMO:
            return Dispersion, float16_t(1.0), None
        elif other == HYDRO:
            return Gel, float16_t(1.0), None
        elif other == ELECTRO:
            return Supraconduction, float16_t(1.0), None


@dataclass(order=False, slots=True)
class GEO(Element):
    def __add__(self, other: Union['Element', 'Reaction_t']) -> Tuple[Reaction_t, float16_t, Optional['Element_t']]:
        if other == PYRO:
            return Cristallisation, float16_t(1.0), None
        elif other == HYDRO:
            return Cristallisation, float16_t(1.0), None
        elif other == CRYO:
            return Cristallisation, float16_t(1.0), None
        elif other == ELECTRO:
            return Cristallisation, float16_t(1.0), None


@dataclass(order=False, slots=True)
class HYDRO(Element):
    def __add__(self, other: Union['Element', 'Reaction_t']) -> Tuple[Reaction_t, float16_t, Optional['Element_t']]:
        if other == PYRO:
            return Evaporation, float16_t(1.5), None
        elif other == GEO:
            return Cristallisation, float16_t(1.0), None
        elif other == ANEMO:
            return Dispersion, float16_t(1.0), None
        elif other == CRYO:
            return Gel, float16_t(1.0), None
        elif other == ELECTRO:
            return Electrocution, float16_t(1.0), None
        elif other == DENDRO:
            return Bourgeonnement, float16_t(1.0), None


@dataclass(order=False, slots=True)
class DENDRO(Element):
    def __add__(self, other: Union['Element', 'Reaction_t']) -> Tuple[Reaction_t, float16_t, Optional['Element_t']]:
        if other == PYRO:
            return Brulure, float16_t(1.0), None
        elif other == HYDRO:
            return Bourgeonnement, float16_t(1.0), None
        elif other == ELECTRO:
            return Acceleration, float16_t(1.0), None


@dataclass(order=False, slots=True)
class ANEMO(Element):
    def __add__(self, other: Union['Element', 'Reaction_t']) -> Tuple[Reaction_t, float16_t, Optional['Element_t']]:
        if other == PYRO:
            return Dispersion, float16_t(1.0), None
        elif other == HYDRO:
            return Dispersion, float16_t(1.0), None
        elif other == CRYO:
            return Dispersion, float16_t(1.0), None
        elif other == ELECTRO:
            return Dispersion, float16_t(1.0), None


@dataclass(order=False, slots=True)
class ELECTRO(Element):
    def __add__(self, other: Union['Element', 'Reaction_t']) -> Tuple[Reaction_t, float16_t, Optional['Element_t']]:
        if other == PYRO:
            return Surcharge, float16_t(1.0), None
        elif other == GEO:
            return Cristallisation, float16_t(1.0), None
        elif other == ANEMO:
            return Dispersion, float16_t(1.0), None
        elif other == CRYO:
            return Supraconduction, float16_t(1.0), None
        elif other == HYDRO:
            return Electrocution, float16_t(1.0), None


Element_t = NewType('Reaction', Union[
    ANEMO,
    GEO,
    ELECTRO,
    DENDRO,
    HYDRO,
    PYRO,
    CRYO
])
