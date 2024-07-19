from utils._typing import *
from enum import Enum


class GType(Enum):
    MAN: Man = 0
    Woman: Woman = 1


class SType(Enum):
    SMALL: Small = 0
    NORMAL: Normal = 1
    TALL: Tall = 2


class CType(Enum):
    ANEMO: Anemo = 0
    GEO: Geo = 1
    ELECTRO: Electro = 2
    DENDRO: Dendro = 3
    HYDRO: Hydro = 4
    PYRO: Pyro = 5
    CRYO: Cryo = 6
    NORMAL: Normal = 7


class RType(Enum):
    MONDSTADT: Mondstadt = 0
    LIYUE: Liyue = 1
    INAZUMA: Inazuma = 2
    SUMERU: Sumeru = 3
    FONTAINE: Fontaine = 4
    NATLAN: Natlan = 5
    SHNEZNAYA: Shneznaya = 6
    TMP1: tmp1 = 7


class WType(Enum):
    HAST: Hast_t = 0
    OH_SWORD: Oh_Sword_t = 1
    TW_SWORD: Th_Sword_t = 2
    CATALYST: Catalyst_t = 3
    TOME: Tome_t = 4
    BOW: Bow_t = 5