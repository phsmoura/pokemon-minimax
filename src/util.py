from data.type_matrix import type_matrix

def get_effective_factor(atk_type:str, def_types:list) -> int:
        atk_factor = type_matrix['header'].index(atk_type[:3])
        effective_factor = 1

        for def_type in def_types:
            def_factor = type_matrix['header'].index(def_type[:3])
            effective_factor *= type_matrix['matrix'][atk_factor][def_factor]

        return int(effective_factor)