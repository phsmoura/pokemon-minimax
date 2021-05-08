moves = {
    'growl': {
        'name': 'Growl',
        'type': 'normal',
        'category': 'buff',
        'power': 0,
        'accuracy': 100,
        'pp': 15,
        'description': 'Lowers opponent\'s Attack.',
        'buff': {
            'hp': 1,
            'atk': 0.9,
            'def': 1,
            'spatk': 1,
            'spdef': 1,
            'spd': 1
        }
    },
    'tackle': {
        'name': 'Tackle',
        'type': 'normal',
        'category': 'physical',
        'power': 40,
        'accuracy': 100,
        'pp': 15,
        'description': 'Attack',
    }
}

type_matrix = {
    'header': ['nor','fir','wat','ele','gra','ice','fig','poi','gro','fly','psi','bug','roc','gho','dra','dar','ste','fai'],
    'matrix': [
        # rows: attack / cols: defense
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.0, 1.0, 1.0, 0.5, 1.0], # nor
        [1.0, 0.5, 0.5, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 0.5, 1.0, 2.0, 1.0], # fir
        [1.0, 2.0, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0, 1.0, 1.0], # wat
        [1.0, 1.0, 2.0, 0.5, 0.5, 1.0, 1.0, 1.0, 0.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0], # ele
        [1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 1.0, 0.5, 2.0, 0.5, 1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 0.5, 1.0], # gra
        [1.0, 0.5, 0.5, 1.0, 2.0, 0.5, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 0.0, 2.0, 1.0, 0.5, 1.0], # ice
        [2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0, 0.5, 0.5, 0.5, 2.0, 0.0, 1.0, 2.0, 2.0, 0.5], # fig
        [1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.0, 2.0], # poi
        [1.0, 2.0, 1.0, 2.0, 0.5, 1.0, 1.0, 2.0, 1.0, 0.0, 1.0, 0.5, 2.0, 1.0, 1.0, 1.0, 2.0, 1.0], # gro
        [1.0, 1.0, 1.0, 0.5, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0], # fly
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 0.5, 1.0, 1.0, 2.0, 1.0, 0.0, 0.5, 1.0], # psi
        [1.0, 0.5, 1.0, 1.0, 2.0, 1.0, 0.5, 0.5, 1.0, 0.5, 2.0, 1.0, 1.0, 0.5, 1.0, 2.0, 0.5, 0.5], # bug
        [1.0, 2.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 0.5, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0], # roc
        [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0, 1.0], # gho
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.5, 0.0], # dra
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0, 0.5], # dar
        [1.0, 0.5, 0.5, 0.5, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0], # ste
        [1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 0.5, 1.0]  # fai
    ]
}

pkmndb = {
    'bulbasaur': {
        'name': 'Bulbasaur',
        'types': (
            type_matrix['header'].index('gra'), 
            type_matrix['header'].index('poi')
        ),
        'stats': {
            'hp': 45,
            'atk': 49,
            'def': 49,
            'spatk': 65,
            'spdef': 65,
            'spd': 45
        },
        'moves': {
            # lvl: move
            1: moves['growl'],
            1: moves['tackle'],
            3: moves['vine_whip'],
            6: moves['growth'],
            9: moves['leech_seed'],
            12: moves['razor_leaf'],
            15: moves['poison_powder'],
            15: moves['sleep_powder'],
            18: moves['seed_bomb'],
            21: moves['take_down'],
            24: moves['sweet_scent'],
            27: moves['syntesis'],
            30: moves['worry_seed'],
            33: moves['double_edge'],
            36: moves['solarbeam']
        }
    },
    'charmander': {
        'name': 'Charmander',
        'types': (
            type_matrix['header'].index('fir')
        ),
        'stats': {
            'hp': 39,
            'atk': 52,
            'def': 43,
            'spatk': 60,
            'spdef': 50,
            'spd': 65
        },
        'moves': {
            # lvl: move
            1: moves['growl'],
            1: moves['tackle'],
            4: moves['ember'],
            8: moves['smokescreen'],
            12: moves['dragon_breath'],
            17: moves['fire_fang'],
            20: moves['slash'],
            24: moves['flamethrower'],
            28: moves['scary_face'],
            32: moves['fire_spin'],
            36: moves['inferno'],
            40: moves['flare_blitz']
        }
    },
    'squirtle': {
        'name': 'Squirtle',
        'types': (
            type_matrix['header'].index('wat')
        ),
        'stats': {
            'hp': 44,
            'atk': 48,
            'def': 65,
            'spatk': 50,
            'spdef': 64,
            'spd': 43
        },
        'moves': {
            # lvl: move
            1: moves['tail_whip'],
            1: moves['tackle'],
            3: moves['water_gun'],
            6: moves['withdraw'],
            9: moves['rapid_spin'],
            12: moves['bite'],
            15: moves['water_pulse'],
            18: moves['protect'],
            21: moves['rain_dance'],
            24: moves['aqua_tail'],
            27: moves['shell_smash'],
            30: moves['iron_defense'],
            33: moves['hydro_pump'],
            36: moves['skull_bash']
        }
    },
}

print(pkmndb['bulbasaur'])