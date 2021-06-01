from math import floor
from data.type_matrix import type_matrix

def get_effective_factor(atk_type:str, def_types:list) -> int:
        atk_factor = type_matrix['header'].index(atk_type[:3])
        effective_factor = 1

        for def_type in def_types:
            def_factor = type_matrix['header'].index(def_type[:3])
            effective_factor *= type_matrix['matrix'][atk_factor][def_factor]

        return int(effective_factor)

def get_damage(move_category, move_power, attacker, defender, effective_factor):
    if move_category[:3] == 'phy':
        damage = floor((((2 * attacker.level/5) + 20 * move_power * attacker.attack/50) / defender.defense) + 2) * effective_factor
    elif move_category[:3] == 'spe':
        damage = floor((((2 * attacker.level/5) + 20 * move_power * attacker.spatk/50) / defender.spdef) + 2) * effective_factor
    
    if damage <= 0 and effective_factor != 0:
        damage = 1