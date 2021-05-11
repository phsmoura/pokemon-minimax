from random import choice


class Trainer:
    def __init__(self, trainer):
        self.name = trainer['name']
        self.team = trainer['team']
        self.points = 0

    def print_team(self, change_pkmn=''):
        print(f"{self.name} team:")
        for pkmn in self.team:
            if pkmn is not change_pkmn:
                print(f"{self.team.index(pkmn)}: {pkmn.name}-LVL:{pkmn.level}")
        print()

    def change_pokemon(self, change_pkmn):
        self.print_team(change_pkmn)
        opt_pkmn = int(input(f"Choose an option: "))
        pkmn = self.team[opt_pkmn]
        return pkmn

    def pokemon_battle(self, first, second):
        first.fight(second)
        if second.hp <= 0: 
            print(f"{second.name} defeated...")
            return True
        return False

    def trainer_battle(self, opponent):
        self.print_team()
        opponent.print_team()

        pkmn_1 = self.team[0]
        pkmn_2 = opponent.team[0]
        # pkmn_2.print_call_pokemon()
        pkmn_1.print_call_pokemon()

        while True:
            pkmn_2.print_battle()
            pkmn_1.print_battle()

            opt = bool(int(input("Change pokemon?\n0: No\n1: Yes\n\nChoose an option [0-1]: ")))

            if opt:
                pkmn_1 = self.change_pokemon(pkmn_1.name)
                pkmn_1.print_call_pokemon()
                pkmn_2.print_battle()
                pkmn_1.print_battle()

            if pkmn_2.speed > pkmn_1.speed or opt:
                if opponent.pokemon_battle(pkmn_2,pkmn_1):
                    opponent.points += 1
                    self.team.remove(pkmn_1)
                    if not(self.team):
                        return "You lose" 
                    print("Choose another pokemon:")
                    pkmn_1 = self.change_pokemon(change_pkmn='')
                    pkmn_1.print_call_pokemon()

                pkmn_2.print_battle()
                pkmn_1.print_battle()

                if self.pokemon_battle(pkmn_1,pkmn_2):
                    self.points += 1
                    opponent.team.remove(pkmn_2)
                    if not(opponent.team):
                        return "You won" 
                    pkmn_2 = choice(opponent.team)
                    print(f"{opponent.name} sent out {pkmn_2.name}!\n")
            else:
                if self.pokemon_battle(pkmn_1,pkmn_2):
                    self.points += 1
                    opponent.team.remove(pkmn_2)
                    if not(opponent.team):
                        return "You won" 
                    pkmn_2 = choice(opponent.team)
                    print(f"{opponent.name} sent out {pkmn_2.name}!\n")

                pkmn_2.print_battle()
                pkmn_1.print_battle()
                
                if opponent.pokemon_battle(pkmn_2,pkmn_1): 
                    opponent.points += 1
                    self.team.remove(pkmn_1)
                    if not(self.team):
                        return "You lose" 
                    print("Choose another pokemon:")
                    pkmn_1 = self.change_pokemon(change_pkmn='')
                    pkmn_1.print_call_pokemon()
