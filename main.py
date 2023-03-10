import json
from Logic.Fight import Fight
from Models.Fighter import Fighter, Moves, Power
import sys


def main(p1_moves: Moves, p2_moves: Moves):
    player1 = Fighter(
        name="Tonyn Stallone",
        hp=6,
        special_moves=[
            Power(name="Taladoken", combination="DSD,P", damage=3),
            Power(name="Remuyuken", combination="SD,K", damage=2),
        ],
        moves=p1_moves,
    )

    player2 = Fighter(
        name="Arnaldor Shuatseneguer",
        hp=6,
        special_moves=[
            Power(name="Remuyuken", combination="SA,K", damage=3),
            Power(name="Taladoken", combination="ASA,P", damage=2),
        ],
        moves=p2_moves,
    )

    fight = Fight(player1=player1, player2=player2)

    fight.fight()


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) < 1:
        print("Se requiere un json con los movimientos utilizados por los personajes")

    try:
        moves = json.loads(sys.argv[1])
        main(
            p1_moves=Moves(
                movements=moves["player1"]["movimientos"],
                hits=moves["player1"]["golpes"],
            ),
            p2_moves=Moves(
                movements=moves["player2"]["movimientos"],
                hits=moves["player2"]["golpes"],
            ),
        )
    except ValueError as e:
        print(e)
    except KeyError as e:
        print("Json invalido")
    except Exception as e:
        print(e)
