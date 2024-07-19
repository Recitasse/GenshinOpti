from dataclasses import dataclass, InitVar, field
from abc import ABC
from utils._typing import *
from _enum_types import *

from datetime import date

from typing import Dict, Tuple


@dataclass(order=False, repr=True, eq=True)
class Character(ABC):
    # Description
    name: str = field(init=False)
    element: Element = field(init=False)
    weapon_type: Weapons = field(init=False)

    # Statistics
    niveau: uint8 = field(init=False)
    pv: uint32 = field(init=False)
    atq: uint32 = field(init=False)
    def_: uint32 = field(init=False)
    b_pv: float16 = field(init=False)
    b_atq: float16 = field(init=False)
    b_def: float16 = field(init=False)

    m_elem: uint32 = field(init=False)

    t_crit: float16 = field(init=False)
    d_crit: float16 = field(init=False)
    b_soin: float16 = field(init=False)
    recharge: float16 = field(init=False)
    red_tdr: float16 = field(init=False)
    f_bouclier: float16 = field(init=False)

    res_anemo: float16 = field(init=False)
    bon_anemo: float16 = field(init=False)
    res_geo: float16 = field(init=False)
    bon_geo: float16 = field(init=False)
    res_electro: float16 = field(init=False)
    bon_electro: float16 = field(init=False)
    res_dendro: float16 = field(init=False)
    bon_dendro: float16 = field(init=False)
    res_hydro: float16 = field(init=False)
    bon_hydro: float16 = field(init=False)
    res_pyro: float16 = field(init=False)
    bon_pyro: float16 = field(init=False)
    res_cryo: float16 = field(init=False)
    bon_cryo: float16 = field(init=False)
    res_phy: float16 = field(init=False)
    bon_phy: float16 = field(init=False)

    # Set
    artifacts: Dict[str, object] = field(init=False)

    # Weapon
    weapon: object = field(init=False)

    # character stats
    constellations: object = field(init=False)
    buffs: object = field(init=False)

    # Aptitudes
    normal_attack: object = field(init=False)
    elemental_skill: object = field(init=False)
    elemental_burst: object = field(init=False)

    # Passive
    f_passive: object = field(init=False)
    l_passive: object = field(init=False)

    # metadata
    _category: Tuple[Gender, CSize] = field(init=False)
    _release_date: date = field(init=False)
    _location: Location = field(init=False)
    _version: float16 = field(init=False)
    _rarity: Rarity = field(init=False)

    # InitVar
    _json_loader: InitVar[str] = field(init=True)

    def __post_init__(self, _json_loader: str) -> None:
        ...

    @staticmethod
    def __set_statistics(name: str) -> None:
        """
        Charge toutes les statistiques d'un personnage
        :param name: nom du personnage
        :return: None
        """
        ...

    @staticmethod
    def __set_metadata(name: str) -> None:
        """
        Charge toutes les meta données du personnage
        :param name: nom du personnage
        :return: None
        """
        ...

    @staticmethod
    def __set_types(name: str) -> None:
        """
        Charge toutes les données type d'un personnage
        :param name: nom du personnage
        :return: None
        """
        ...

    @staticmethod
    def __set_constellation(name: str) -> None:
        """
        Charge les constellations d'un personnage
        :param name: nom du personnage
        :return: None
        """
        ...

    @staticmethod
    def __set_passive(name: str) -> None:
        """
        Charge tous les passifs d'un personnage
        :param name: nom du personnage
        :return: None
        """
        ...

    @staticmethod
    def __set_aptitudes(name: str) -> None:
        """
        Charge toutes les aptitudes
        :param name:
        :return:
        """
