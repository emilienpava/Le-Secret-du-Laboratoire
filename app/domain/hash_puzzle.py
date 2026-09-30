from dataclasses import dataclass
import hashlib

from .puzzle import Puzzle


@dataclass
class HashPuzzle(Puzzle):
    expected_hash: str

    def check_solution(self, answer: str) -> bool:
        answer_hash = hashlib.sha256(answer.encode()).hexdigest()
        return answer_hash == self.expected_hash