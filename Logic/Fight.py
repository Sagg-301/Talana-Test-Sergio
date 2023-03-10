from time import sleep
from pydantic import BaseModel

from Models.Fighter import Fighter


class Fight(BaseModel):
    player1: Fighter
    player2: Fighter

    def __define_turn_order(self) -> list[Fighter]:
        """Private function that gets turn order

        Returns:
            list[Fighter]: A list with the order of fighter
        """

        # Get the lenghts of hits and moves without counting empty strings
        p1_movement_len = len([move for move in self.player1.moves.movements if move])
        p1_hits_len = len([move for move in self.player1.moves.hits if move])

        p2_movement_len = len([move for move in self.player2.moves.movements if move])
        p2_hits_len = len([move for move in self.player2.moves.hits if move])

        # List of comparisons to make
        comparisons = [
            (p1_movement_len + p1_hits_len, p2_movement_len + p2_hits_len),
            (p1_movement_len, p2_movement_len),
            (p1_hits_len, p2_hits_len),
        ]

        # Check the comparisons
        for p1_value, p2_value in comparisons:
            if p1_value > p2_value:
                return [self.player1, self.player2]
            elif p1_value < p2_value:
                return [self.player2, self.player1]

        return [self.player1, self.player2]

    def __calculate_damage(self, fighter: Fighter, turn: int) -> int:
        """Private function that returns damage done

        Args:
            fighter (Fighter): The fighter doing the damage
            turn (int): The current turn

        Returns:
            int: Damage done
        """
        if len(fighter.moves.hits) <= turn:
            return 0

        curr_move = f"{fighter.moves.movements[turn] if len(fighter.moves.movements) > turn else None},{fighter.moves.hits[turn]}"

        # TODO: Optimize this for
        for special in fighter.special_moves:
            if curr_move == special.combination:
                return special.damage

        if fighter.moves.hits[turn] in ["P", "K"]:
            return 1

        return 0

    def __narrate_turn(self, fighter: Fighter, turn: int) -> None:
        """Function that "narrates" a fighter's turn

        Args:
            fighter (Fighter): Current fighter
            turn (int): Current turn
        """
        if len(fighter.moves.hits) <= turn:
            return

        movements = (
            fighter.moves.movements[turn] if len(fighter.moves.movements) > turn else ""
        )
        hits = fighter.moves.hits[turn]

        curr_move = f"{movements},{hits}"

        for special in fighter.special_moves:
            if curr_move == special.combination:
                print(f"{fighter.name} conecta un {special.name}!\n")
                return

        move = (
            curr_move.replace(",", "y " if movements and hits else "")
            .replace("S", "se agacha, ")
            .replace("W", "salta, ")
            .replace(
                "A",
                "se mueve hacia atrás, " if fighter == self.player1 else "avanza, ",
            )
            .replace(
                "D", "avanza, " if fighter == self.player1 else "se mueve hacia atrás, "
            )
            .replace("P", "conecta un puño!  ")
            .replace("K", "conecta una patada!  ")
        )

        print(f"{fighter.name} {move[:-2]}\n")

    def __player_turn(
        self, attacking_player: Fighter, damaged_player: Fighter, turn: int
    ) -> int:
        """Process player turn

        Args:
            attacking_player (Fighter): Player that is currently moving and doing damage
            damaged_player (Fighter): Fighter that is receiving damage
            turn (int): Turn number

        Returns:
            int: Remaining HP of damaged player
        """
        damage_done: int = self.__calculate_damage(attacking_player, turn)
        damaged_player.hp -= damage_done
        self.__narrate_turn(attacking_player, turn)

        if damaged_player.hp < 1:
            print(
                f"{attacking_player.name} gana con {attacking_player.hp} punto de energía restante!\n\n"
            )

        sleep(2)
        return damaged_player.hp

    def fight(self):
        attack_order = self.__define_turn_order()
        turn = 0

        # This loop braks if one of the players health points reaches 0
        while (
            self.__player_turn(
                attacking_player=attack_order[0],
                damaged_player=attack_order[1],
                turn=turn,
            )
            > 0
            and self.__player_turn(
                attacking_player=attack_order[1],
                damaged_player=attack_order[0],
                turn=turn,
            )
            > 0
        ):
            turn += 1
