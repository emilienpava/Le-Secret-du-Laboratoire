from dataclasses import dataclass
from typing import Optional

from .game_element import GameElement


@dataclass
class Door(GameElement):
    is_locked: bool = True
    required_item_id: Optional[str] = None