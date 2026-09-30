from fastapi import APIRouter, HTTPException

from app.game_data import room1, room2, room3, room4
from app.schemas.puzzle import PuzzleSubmission


router = APIRouter()


rooms = [room1, room2, room3, room4]


@router.get("/rooms")
def get_rooms():
    return rooms


@router.get("/rooms/{room_id}")
def get_room(room_id: str):
    for room in rooms:
        if room.id == room_id:
            return room

    raise HTTPException(
        status_code=404,
        detail="Salle introuvable"
    )


@router.post("/puzzles/submit")
def submit_puzzle(submission: PuzzleSubmission):
    for room in rooms:
        for puzzle in room.puzzles:
            if puzzle.id == submission.puzzle_id:
                success = puzzle.check_solution(submission.attempt_code)

                if success:
                    return {
                        "success": True,
                        "message": "Porte déverrouillée !"
                    }

                return {
                    "success": False,
                    "message": "Mauvaise réponse."
                }

    raise HTTPException(
        status_code=404,
        detail="Puzzle introuvable"
    )