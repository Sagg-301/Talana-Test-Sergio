from pydantic import BaseModel, PositiveInt, validator


class Power(BaseModel):
    name: str
    combination: str
    damage: PositiveInt


class Moves(BaseModel):
    movements: list[str] = []
    hits: list[str] = []

    @validator("*", each_item=True)
    def validate_moves_and_hits(cls, v: str) -> str:
        for move in v:
            if move.upper() not in "WASDPK":
                raise ValueError(
                    f"{move} no es un movimiento valido, solo W,A,S,D y P, K son aceptados"
                )
        return v.upper()

    @validator("hits")
    def validate_hits_lenght(
        cls, v: list[str], values: dict[str, list[str]]
    ) -> list[str]:
        if "movements" in values and len(v) != len(values["movements"]):
            raise ValueError(
                "Los movimientos y los golpes deben ser de la misma longitud"
            )
        return v


class Fighter(BaseModel):
    name: str
    hp: int
    special_moves: list[Power] = []
    moves: Moves

    @validator("special_moves")
    def special_moves_lenght(cls, v: list[str]) -> list[str]:
        if len(v) > 2 or len(v) < 2:
            raise ValueError("Special Moves list must be 2")

        return v
