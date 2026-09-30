from pydantic import BaseModel, Field, field_validator


class PuzzleSubmission(BaseModel):
    puzzle_id: str = Field(
        ...,
        description="Identifiant    unique du puzzle"
    )

    attempt_code: str = Field(
        ...,
        description="Tentative du joueur"
    )

    player_id: str = Field(
        ...,
        description="Identifiant du joueur"
    )

    @field_validator("attempt_code")
    @classmethod
    def code_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Le code ne peut pas être vide")
        return v