class Pokemon:
    def __init__(self, name, lvl, types, moves, hp, atk, dfs, spatk, spdef, spd):
        self.name = name
        self.level = lvl
        self.types = types
        self.moves = moves
        self.attack = atk
        self.defense = dfs
        self.spatk = spatk
        self.spdef = spdef
        self.speed = spd

    def print_pokemon(self):
        print(f"{self.name}:")
        print(f"LVL: {self.level}")
        print(f"Types: {self.types}")
        print(f"Atk: {self.attack}")
        print(f"Def: {self.defense}")
        print(f"Sp. Atk: {self.spatk}")
        print(f"Sp. Def: {self.spdef}")
        print(f"Spd: {self.speed}")

    