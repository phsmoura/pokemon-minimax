from random import choice, randint
from minimax import Graph
from data.moves_db import moves as moves_db
from util import get_effective_factor, get_damage


class Trainer:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.current_pkmn = team[0]
        self.current_move = 100
        self.atk_this_turn = True
        self.current_state = None

    def print_team(self, k):
        print(f"{self.name}\'s team:")
        aux = self.team[k:]
        for pkmn in aux:
            print(f"{k}: {pkmn.name} - HP: {pkmn.hp}/{pkmn.hp_full}")
            k += 1
        print()

    def pokemon_battle(self, first, second):
        move_type = moves_db[first.moves[self.current_move]]['type']
        move_category = moves_db[first.moves[self.current_move]]['category']
        move_power = moves_db[first.moves[self.current_move]]['power']
        move_chosen = moves_db[first.moves[self.current_move]]['name']
        
        effective_factor = get_effective_factor(move_type, second.types)
        second.hp -= get_damage(move_category, move_power, first, second, effective_factor)

        print(f"{first.name} used {move_chosen} and caused {second.hp_full - second.hp} points of damage!")
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
        
        print(f"\nGo {self.current_pkmn.name}!")

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

class AI(Trainer):
    def battle_ai(self, opponent: Player):
        data = {
            'ai': {
                'team': self.team
            },
            'player': {
                'team': opponent.team
            }
        }

        if (not self.current_state or not self.current_state.children) or \
        (self.current_state.decision['change_pkmn'] or not opponent.current_state.decision['change_pkmn']) or \
            self.current_pkmn.hp <= 0:
            graph = Graph()
            self.current_state = graph.explore(data, 'player', 'ai')

            if opponent.atk_this_turn:
                opponent_decision = {
                    'change_pkmn': False,
                    'pkmn': '',
                    'move': moves_db[opponent.current_pkmn.moves[opponent.current_move]]['name'].lower()
                }
            else:
                opponent_decision = {
                    'change_pkmn': True,
                    'pkmn': opponent.current_pkmn.name.lower(),
                    'move': ''
                }

            for child in self.current_state.children:
                if child.decision == opponent_decision:
                    opponent.current_state = child
                    break
        else:
            for child in opponent.current_state.children:
                if child.score > self.current_state.score:
                    self.current_state = child

        # ai change pkmn - ai atk
        if self.current_state.decision['change_pkmn']:
            self.atk_this_turn = False
            pkmn_index = self.team.index(self.current_state.decision['pkmn'])
            self.current_pkmn = self.team[pkmn_index]
            self.team[0], self.team[pkmn_index] = self.current_pkmn, self.team[0]
            print(f"{self.name} sent out {self.current_pkmn.name}!")
        else:
            self.current_move = self.current_pkmn.moves.index(self.current_state.decision['move'])
        # print(self.current_state.decision)

    def main_battle(self, opponent: Player):
        self.print_team(0)
        opponent.print_team(0)

        print(f"{self.name} sent out {self.current_pkmn.name}!")
        print(f"Go {opponent.current_pkmn.name}!\n")

        while True:
            self.current_pkmn.print_battle()
            opponent.current_pkmn.print_battle()

            opponent.battle_menu()
            self.battle_ai(opponent)
            
            if not self.atk_this_turn:
                self.current_pkmn.print_battle()
                opponent.current_pkmn.print_battle()

            if not self.atk_this_turn and opponent.atk_this_turn:
                if opponent.pokemon_battle(opponent.current_pkmn, self.current_pkmn):
                    self.team.remove(self.current_pkmn)
                    if not(self.team):
                        return "You win" 
                    self.current_pkmn = self.team[0]

            elif not opponent.atk_this_turn and self.atk_this_turn:
                if self.pokemon_battle(self.current_pkmn, opponent.current_pkmn):
                    opponent.team.remove(opponent.current_pkmn)
                    if not(opponent.team):
                        return "You lose" 
                    opponent.change_pokemon()

            elif self.atk_this_turn and opponent.atk_this_turn:
                if self.current_pkmn.speed > opponent.current_pkmn.speed:

                    if self.pokemon_battle(self.current_pkmn, opponent.current_pkmn):
                        opponent.team.remove(opponent.current_pkmn)
                        if not(opponent.team):
                            return "You lose" 
                        opponent.change_pokemon()
                        opponent.atk_this_turn = False
                    
                    if opponent.atk_this_turn:
                        if opponent.pokemon_battle(opponent.current_pkmn, self.current_pkmn):
                            self.team.remove(self.current_pkmn)
                            if not(self.team):
                                return "You win" 
                            self.current_pkmn = self.team[0]

                else:

                    if opponent.pokemon_battle(opponent.current_pkmn, self.current_pkmn):
                        self.team.remove(self.current_pkmn)
                        if not(self.team):
                            return "You win" 
                        self.current_pkmn = self.team[0]
                        self.atk_this_turn = False

                    if self.atk_this_turn:
                        if self.pokemon_battle(self.current_pkmn, opponent.current_pkmn):
                            opponent.team.remove(opponent.current_pkmn)
                            if not(opponent.team):
                                return "You lose" 
                            opponent.change_pokemon()
            
            self.current_move = 100
            opponent.current_move = 100
            self.atk_this_turn = True
            opponent.atk_this_turn = True


