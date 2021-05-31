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
        