from numpy import uint8 as uint8_t
from numpy import uint32 as uint32_t
from numpy import float16 as float16_t
from typing import NewType, TypeAlias, Union
from enum import Enum

# Declaration
uint8 = NewType('uint8', uint8_t)
uint32 = NewType('uint32', uint32_t)
float16 = NewType('uint8', float16_t)

# Character Type
Anemo: TypeAlias = uint8
Geo: TypeAlias = uint8
Electro: TypeAlias = uint8
Dendro: TypeAlias = uint8
Hydro: TypeAlias = uint8
Pyro: TypeAlias = uint8
Cryo: TypeAlias = uint8
Physic: TypeAlias = uint8
Element = NewType('Element', Union[
    Anemo,
    Geo,
    Electro,
    Dendro,
    Hydro,
    Pyro,
    Cryo,
    Physic
])

# Region
Mondstadt: TypeAlias = uint8
Liyue: TypeAlias = uint8
Inazuma: TypeAlias = uint8
Sumeru: TypeAlias = uint8
Fontaine: TypeAlias = uint8
Natlan: TypeAlias = uint8
Shneznaya: TypeAlias = uint8
tmp1: TypeAlias = uint8
Location = NewType('Location', Union[
    Mondstadt,
    Liyue,
    Inazuma,
    Sumeru,
    Fontaine,
    Natlan,
    Shneznaya,
    tmp1
])

# Character weapon
Hast_t: TypeAlias = uint8
Oh_Sword_t: TypeAlias = uint8
Th_Sword_t: TypeAlias = uint8
Catalyst_t: TypeAlias = uint8
Tome_t: TypeAlias = uint8
Bow_t: TypeAlias = uint8
Weapons = NewType('Weapons', Union[
    Hast_t,
    Oh_Sword_t,
    Th_Sword_t,
    Catalyst_t,
    Tome_t,
    Bow_t
])

# Character gender
Woman: TypeAlias = uint8
Man: TypeAlias = uint8
Gender = NewType('Gender', Union[Woman, Man])

# Character size
Small: TypeAlias = uint8
Normal: TypeAlias = uint8
Tall: TypeAlias = uint8
CSize = NewType('CSize', Union[Small, Normal, Tall])

# Rarity
OneStar_t: TypeAlias = uint8
TwoStar_t: TypeAlias = uint8
ThreeStar_t: TypeAlias = uint8
FourStar_t: TypeAlias = uint8
FiveStar_t: TypeAlias = uint8
Rarity_t = NewType('Rarity', Union[OneStar_t, TwoStar_t, ThreeStar_t, FourStar_t, FiveStar_t])


class Rarity(Enum):
    OneStar: OneStar_t = 1
    TwoStar: TwoStar_t = 2
    ThreeStar: ThreeStar_t = 3
    FourStar: FourStar_t = 4
    FiveStar: FiveStar_t = 5
