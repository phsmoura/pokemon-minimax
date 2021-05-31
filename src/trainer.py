from math import floor
from random import choice, randint
from data.moves_db import moves as moves_db
from data.type_matrix import type_matrix


class Trainer:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.current_pkmn = team[0]
        self.current_move = 100
        self.atk_this_turn = True

        self.score = 0
        self.total_score = 0

    def print_team(self, k):
        print(f"{self.name}\'s team:")
        aux = self.team[k:]
        for pkmn in aux:
            print(f"{k}: {pkmn.name} - HP: {pkmn.hp}/{pkmn.hp_full}")
            k += 1
        print()

    def choose_move(self):
        self.current_move = randint(0,3)

    def change_pokemon(self):
        if self.current_pkmn.hp > 0:
            pkmn_index = randint(1,len(self.team) - 1)
            self.current_pkmn = self.team[pkmn_index]
            self.team[0], self.team[pkmn_index] = self.current_pkmn, self.team[0]
        else:
            self.current_pkmn = choice(self.team)

        print(f"{self.name} sent out {self.current_pkmn.name}!")

    def battle_menu(self):
        call = {0: self.choose_move, 1: self.change_pokemon}
        opt = randint(0,1)

        if len(self.team) == 1:
            opt = 0

        if opt != 0:
            self.atk_this_turn = False

        call[opt]()

    def get_effective_factor(self, atk_type:str, def_types:list) -> int:
        atk_factor = type_matrix['header'].index(atk_type[:3])
        effective_factor = 1

        for def_type in def_types:
            def_factor = type_matrix['header'].index(def_type[:3])
            effective_factor *= type_matrix['matrix'][atk_factor][def_factor]

        return int(effective_factor)
    
    def pokemon_battle(self, first, second):
        move_type = moves_db[first.moves[self.current_move]]['type']
        move_category = moves_db[first.moves[self.current_move]]['category']
        move_power = moves_db[first.moves[self.current_move]]['power']
        move_chosen = moves_db[first.moves[self.current_move]]['name']
        
        effective_factor = self.get_effective_factor(move_type, second.types)
        # print(effective_factor)

        if move_category[:3] == 'phy':
            damage = floor((((2 * first.level/5) + 20 * move_power * first.attack/50) / second.defense) + 2) * effective_factor
        elif move_category[:3] == 'spe':
            damage = floor((((2 * first.level/5) + 20 * move_power * first.spatk/50) / second.spdef) + 2) * effective_factor

        if damage <= 0:
            damage = 1

        second.hp -= damage

        print(f"{first.name} used {move_chosen} and caused {damage} points of damage!")
        if effective_factor >= 2:
            print("This move was super effective...\n")
        elif effective_factor == 0.5:
            print("This move was not very effective...\n")
        elif effective_factor == 0:
            print("This move had no effect...\n")

        if second.hp <= 0: 
            print(f"{second.name} fainted...\n")
            return True
        return False

    def main_battle(self, opponent):
        self.print_team(0)
        opponent.print_team(0)

        print(f"{self.name} sent out {self.current_pkmn.name}!")
        print(f"Go {opponent.current_pkmn.name}!")

        while True:
            self.current_pkmn.print_battle()
            opponent.current_pkmn.print_battle()

            self.battle_menu()
            if not self.atk_this_turn:
                self.current_pkmn.print_battle()
                opponent.current_pkmn.print_battle()
            opponent.battle_menu()

            if not self.atk_this_turn and opponent.atk_this_turn:
                opponent.score += 1
                self.score -= 1
                if opponent.pokemon_battle(opponent.current_pkmn, self.current_pkmn):
                    opponent.score += 10
                    self.team.remove(self.current_pkmn)
                    if not(self.team):
                        return "You win" 
                    self.change_pokemon()

            elif not opponent.atk_this_turn and self.atk_this_turn:
                self.score += 1
                opponent.score -= 1
                if self.pokemon_battle(self.current_pkmn, opponent.current_pkmn):
                    self.score += 10
                    opponent.team.remove(opponent.current_pkmn)
                    if not(opponent.team):
                        return "You lose" 
                    opponent.change_pokemon()

            elif self.atk_this_turn and opponent.atk_this_turn:
                if self.current_pkmn.speed > opponent.current_pkmn.speed:
                    self.score += 1
                    opponent.score -= 1

                    if self.pokemon_battle(self.current_pkmn, opponent.current_pkmn):
                        self.score += 10
                        opponent.team.remove(opponent.current_pkmn)
                        if not(opponent.team):
                            return "You lose" 
                        opponent.change_pokemon()
                        opponent.atk_this_turn = False
                    
                    if opponent.atk_this_turn:
                        if opponent.pokemon_battle(opponent.current_pkmn, self.current_pkmn):
                            opponent.score += 10
                            self.team.remove(self.current_pkmn)
                            if not(self.team):
                                return "You win" 
                            self.change_pokemon()

                else:
                    opponent.score += 1
                    self.score -= 1

                    if opponent.pokemon_battle(opponent.current_pkmn, self.current_pkmn):
                        opponent.score += 10
                        self.team.remove(self.current_pkmn)
                        if not(self.team):
                            return "You win" 
                        self.change_pokemon()
                        self.atk_this_turn = False

                    if self.atk_this_turn:
                        if self.pokemon_battle(self.current_pkmn, opponent.current_pkmn):
                            self.score += 10
                            opponent.team.remove(opponent.current_pkmn)
                            if not(opponent.team):
                                return "You lose" 
                            opponent.change_pokemon()
            
            self.current_move = 100
            opponent.current_move = 100
            self.atk_this_turn = True
            opponent.atk_this_turn = True


class Player(Trainer):
    def choose_move(self):
        print(f"{self.current_pkmn.name} moves:")

        while self.current_move < 0 or self.current_move > 3:
            for k in range(4):
                print(f"{k}: {moves_db[self.current_pkmn.moves[k]]['name']} - type: {moves_db[self.current_pkmn.moves[k]]['type']}")
            self.current_move = int(input('Choose your move [0-3]: '))
        print()

    def change_pokemon(self):
        print("Choose another pokemon:")
        if self.current_pkmn.hp > 0:
            self.print_team(1)
            pkmn_index = int(input(f'Choose your pkmn [1-{len(self.team) - 1}]: '))
            self.current_pkmn = self.team[pkmn_index]
            self.team[0], self.team[pkmn_index] = self.current_pkmn, self.team[0]
        else:
            self.print_team(0)
            pkmn_index = int(input(f'Choose your pkmn [0-{len(self.team) - 1}]: '))
            self.current_pkmn = self.team[pkmn_index]
        
        print(f"Go {self.current_pkmn.name}!")

    def battle_menu(self):
        if len(self.team) == 1:
            opt = 0

        call = {0: self.choose_move, 1: self.change_pokemon}
        opt = -1
        print("MENU:")
        while opt < 0 or opt > 1:
            opt = int(input("0: Attack\n1: Change pokemon\n\nChoose an option [0-1]: "))
        if opt != 0:
            self.atk_this_turn = False
        call[opt]()