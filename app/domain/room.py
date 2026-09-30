from dataclasses import dataclass, field

from .item import Item
from .door import Door
from .puzzle import Puzzle


@dataclass
class Room:
    id: str
    name: str
    description: str
    items: list[Item] = field(default_factory=list)
    doors: list[Door] = field(default_factory=list)
    puzzles: list[Puzzle] = field(default_factory=list)