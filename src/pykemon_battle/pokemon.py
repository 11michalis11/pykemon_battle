from .utils import (
    get_pokemon_info,
    choose_best_moveset,
    randomly_choose_moveset,
    manually_choose_moveset,
    choose_first_four_moves_for_now,
)

from .move import Move


class Pokemon:
    def __init__(self, poke_id):
        self.json = get_pokemon_info(poke_id=poke_id)
        self.id = self.json["id"]
        self.name = self.json["name"]
        self.heal()

        # self.get_moves()

    def reset(self):
        self.attack = self.json["stats"][1]["base_stat"]
        self.deffense = self.json["stats"][2]["base_stat"]
        self.special_attack = self.json["stats"][3]["base_stat"]
        self.special_deffense = self.json["stats"][4]["base_stat"]
        self.speed = self.json["stats"][5]["base_stat"]

    def heal(self):
        self.reset()
        self.hp = self.json["stats"][0]["base_stat"]
        self.status = "healthy"

    def get_moves(self):
        all_possible_moves = self.json["moves"]
        move_selection_method = input(
            "Move selection method: \n1: Automatic \n2: Manual \n3: Random \nAnswer:"
        )
        if move_selection_method == "1" or move_selection_method.lower() == "automatic":
            selected_moves = choose_best_moveset(all_possible_moves)
        elif move_selection_method == "2" or move_selection_method.lower() == "manual":
            selected_moves = manually_choose_moveset(all_possible_moves)
        elif move_selection_method == "3" or move_selection_method.lower() == "random":
            selected_moves = randomly_choose_moveset(all_possible_moves)
        else:
            selected_moves = choose_first_four_moves_for_now(all_possible_moves)

        self.moveset = (
            Move(selected_moves[0]),
            Move(selected_moves[1]),
            Move(selected_moves[2]),
            Move(selected_moves[3]),
        )

    def __repr__(self):
        return f"{self.name.capitalize()}"


# demo_poke = Pokemon("Silcoon")
# demo_poke.get_moves()
