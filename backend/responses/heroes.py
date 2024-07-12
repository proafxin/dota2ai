from enum import Enum

from backend.responses.base import Base


class AttackType(str, Enum):
    MELEE = "melee"
    RANGED = "ranged"


class PrimaryAttribute(str, Enum):
    AGILITY = "agi"
    STRENGTH = "str"
    INTELLIGENCE = "int"
    UNIVERSAL = "all"


class Role(str, Enum):
    SUPPORT = "Support"
    DISABLER = "Disabler"
    NUKER = "Nuker"
    DURABLE = "Durable"
    CARRY = "Carry"
    INITIATOR = "Initiator"
    PUSHER = "Pusher"
    ESCAPE = "Escape"


class Hero(Base):
    id: int
    name: str
    localized_name: str
    primary_attr: PrimaryAttribute
    attack_type: AttackType
    roles: list[Role]
    legs: int
