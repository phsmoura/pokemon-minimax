from random import randint, choice
from math import floor
from data.moves_db import moves
from data.pokemon_db import pokemons
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

def generate_pokemon() -> dict:
    pkmn_randomized = choice(list(pokemons.keys()))
    moves = list()
     
    while len(moves) < 4:
        moves.append(choice(pokemons[pkmn_randomized]['moves']))
        moves = list(set(moves))
    
    return Pokemon(
                pokemons[pkmn_randomized],
                randint(45,60),
                moves
            )

def battle(my_pkmn, opponent):
    _round = True
    while _round:
        opponent.print_battle()
        my_pkmn.print_battle()
        for k in range(4):
            print(f"{k}: {my_pkmn.moves[k]}")

        move_chosen = input('Chose your move: ')
        _round = False

def main():
    my_team = {
        0: Pokemon(
                pokemons['pikachu'],
                85,
                [ 
                    pokemons['pikachu']['moves'][3],
                    pokemons['pikachu']['moves'][7],
                    pokemons['pikachu']['moves'][2],
                    pokemons['pikachu']['moves'][17]
                ]
            ),
        1: generate_pokemon()
        # 2: generate_pokemon()
    }

    oponent_team = {
        0: generate_pokemon(),
        1: generate_pokemon()
    }

    # my_team[1].print_pokemon()
    battle(my_team[0], oponent_team[0])


if __name__ == '__main__':
    main()
