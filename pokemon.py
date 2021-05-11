from math import floor
from data.moves_db import moves as moves_db
from data.type_matrix import type_matrix


class Pokemon:
    def __init__(self, pkmn_base, lvl, moves):
        self.name = pkmn_base['name']
        self.level = lvl
        self.types = pkmn_base['types']
        self.moves = moves
        self.hp = floor(pkmn_base['stats']['hp'] * 2 * lvl / 100) + lvl + 10
        self.hp_full = floor(pkmn_base['stats']['hp'] * 2 * lvl / 100) + lvl + 10
        self.attack = floor(pkmn_base['stats']['atk'] * 2 * lvl / 100) + lvl
        self.defense = floor(pkmn_base['stats']['def'] * 2 * lvl / 100) + lvl
        self.spatk = floor(pkmn_base['stats']['spatk'] * 2 * lvl / 100) + lvl
        self.spdef = floor(pkmn_base['stats']['spdef'] * 2 * lvl / 100) + lvl
        self.speed = floor(pkmn_base['stats']['spd'] * 2 * lvl / 100) + lvl

    def print_all_status(self):
        print(f"{self.name}:")
        print(f"LVL: {self.level}")
        print(f"Types: {self.types}")
        print(f"HP: {self.hp}")
        print(f"Atk: {self.attack}")
        print(f"Def: {self.defense}")
        print(f"Sp. Atk: {self.spatk}")
        print(f"Sp. Def: {self.spdef}")
        print(f"Spd: {self.speed}")

    def print_battle(self):
        print(f"{self.name} - LVL: {self.level}")
        print(f"HP: {self.hp}/{self.hp_full}\n")

    def print_call_pokemon(self):
        print(f"Go {self.name}!\n")

    def get_effective_factor(self, atk_type:str, def_types:list) -> float:
        atk_factor = type_matrix['header'].index(atk_type[:3])
        def_factor = 1   
        for def_type in def_types:
            def_factor *= type_matrix['header'].index(def_type[:3])

        return type_matrix['matrix'][atk_factor][def_factor]

    def fight(self, opponent):
        print(f"{self.name} moves:")
        for k in range(4):
            print(f"{k}: {moves_db[self.moves[k]]['name']} - type: {moves_db[self.moves[k]]['type']}")

        move_chosen = int(input('\nChoose your move [0-3]: '))
        while move_chosen < 0 or move_chosen > 3:
            print("try again:\n")
            move_chosen = int(input('Choose your move [0-3]: '))

        move_type = moves_db[self.moves[move_chosen]]['type']
        move_category = moves_db[self.moves[move_chosen]]['category']
        move_power = moves_db[self.moves[move_chosen]]['power']
        move_chosen = moves_db[self.moves[move_chosen]]['name']
        
        effective_factor = int(self.get_effective_factor(move_type, opponent.types))
        # print(effective_factor)

        if move_category[:3] == 'phy':
            damage = floor((((2*self.level/5)+2) * move_power * self.attack/opponent.defense + 100)/50) * effective_factor
        elif move_category[:3] == 'spe':
            damage = floor((((2*self.level/5)+2) * move_power * self.spatk/opponent.spdef + 100)/50) * effective_factor

        if damage <= 0:
            damage = 1

        opponent.hp -= damage

        print(f"{self.name} used {move_chosen} and caused {damage} points of damage!")
        if effective_factor >= 2:
            print("This move was super effective...\n")
        elif effective_factor == 0.5:
            print("This move was not very effective...\n")
        elif effective_factor == 0:
            print("This move had no effect...\n")

class PokemonAI(Pokemon):
    """docstring for PokemonAI"""
    # def __init__(self, arg):
    #     super(PokemonAI, self).__init__()
    #     self.arg = arg

    def fight(self, opponent):
        opponent.print_battle()
        self.print_battle()
        for k in range(4):
            print(f"{k}: {moves_db[self.moves[k]]['name']} - type: {moves_db[self.moves[k]]['type']}")
        move_chosen = int(input('Chose your move: '))
        