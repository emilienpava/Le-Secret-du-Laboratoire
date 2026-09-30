from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Puzzle(ABC):
    id: str
    name: str
    description: str

    @abstractmethod
    def check_solution(self, answer: str) -> bool:
        pass