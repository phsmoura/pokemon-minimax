from random import randint, choice
from math import floor
from data.moves_db import moves as moves_db
from data.pokemon_db import pokemons as pokemon_db
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

    def get_effective_factor(self, atk_type:str, def_types:list) -> float:
        atk_factor = type_matrix['header'].index(atk_type[:3])
        def_factor = 1   
        for def_type in def_types:
            def_factor *= type_matrix['header'].index(def_type[:3])

        return type_matrix['matrix'][atk_factor][def_factor]

    def fight(self, opponent):
        opponent.print_battle()
        self.print_battle()
        for k in range(4):
            print(f"{k}: {moves_db[self.moves[k]]['name']} - type: {moves_db[self.moves[k]]['type']}")

        move_chosen = int(input('Choose your move [0-3]: '))
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

        if damage == 0:
            damage = 1
            
        opponent.hp -= damage

        print(f"{self.name} used {move_chosen} and caused {damage} points of damage!")
        if effective_factor >= 2:
            print("This move was super effective...\n")
        elif effective_factor < 1:
            print("This move was not very effective...\n")

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
        
def generate_pokemon():
    pkmn_randomized = choice(list(pokemon_db.keys()))
    moveset = list()
     
    while len(moveset) < 4:
        moveset.append(choice(pokemon_db[pkmn_randomized]['moves']))
        moveset = list(set(moveset))
    
    return Pokemon(
                pokemon_db[pkmn_randomized],
                randint(45,60),
                moveset
            )

def battle(pkmn_1, pkmn_2):
    keep_fighting = True
    while keep_fighting:
        if pkmn_1.speed > pkmn_2.speed:
            pkmn_1.fight(pkmn_2)
            pkmn_2.fight(pkmn_1)
        else:
            pkmn_2.fight(pkmn_1)
            pkmn_1.fight(pkmn_2)

        # keep_fighting = False
        if pkmn_2.hp <= 0: 
            keep_fighting = False
            print("You win!")
        elif pkmn_1.hp <= 0:
            keep_fighting = False
            print("You lose!")

def main():
    team_1 = [
        Pokemon(
            pokemon_db['pikachu'],
            65,
            [ 
                pokemon_db['pikachu']['moves'][pokemon_db['pikachu']['moves'].index('dig')],
                pokemon_db['pikachu']['moves'][pokemon_db['pikachu']['moves'].index('iron-tail')],
                pokemon_db['pikachu']['moves'][pokemon_db['pikachu']['moves'].index('thunder-punch')],
                pokemon_db['pikachu']['moves'][pokemon_db['pikachu']['moves'].index('thunder')]
            ]
        ),
    ]

    team_2 = [
        Pokemon(
            pokemon_db['blastoise'],
            50,
            [ 
                pokemon_db['blastoise']['moves'][pokemon_db['blastoise']['moves'].index('earthquake')],
                pokemon_db['blastoise']['moves'][pokemon_db['blastoise']['moves'].index('hydro-pump')],
                pokemon_db['blastoise']['moves'][pokemon_db['blastoise']['moves'].index('bite')],
                pokemon_db['blastoise']['moves'][pokemon_db['blastoise']['moves'].index('skull-bash')]
            ]
        ),
    ]

    battle(team_1[0], team_2[0])


if __name__ == '__main__':
    main()
