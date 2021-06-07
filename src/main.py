from trainer import AI, Player
from pokemon import Pokemon
from data.pokemon_db import pokemons as pokemon_db


TEAM = {
    'red': {
        'name': 'Red',
        'team': [
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
            Pokemon(
                pokemon_db['snorlax'],
                50,
                [ 
                    pokemon_db['snorlax']['moves'][pokemon_db['snorlax']['moves'].index('earthquake')],
                    pokemon_db['snorlax']['moves'][pokemon_db['snorlax']['moves'].index('ice-punch')],
                    pokemon_db['snorlax']['moves'][pokemon_db['snorlax']['moves'].index('thunder-punch')],
                    pokemon_db['snorlax']['moves'][pokemon_db['snorlax']['moves'].index('fire-punch')]
                ]
            ),
            Pokemon(
                pokemon_db['charizard'],
                50,
                [ 
                    pokemon_db['charizard']['moves'][pokemon_db['charizard']['moves'].index('air-slash')],
                    pokemon_db['charizard']['moves'][pokemon_db['charizard']['moves'].index('solar-beam')],
                    pokemon_db['charizard']['moves'][pokemon_db['charizard']['moves'].index('focus-blast')],
                    pokemon_db['charizard']['moves'][pokemon_db['charizard']['moves'].index('fire-blast')]
                ]
            ),
        ]
    },
    'blue': {
        'name': 'Blue',
        'team': [
            Pokemon(
                pokemon_db['blastoise'],
                50,
                [ 
                    pokemon_db['blastoise']['moves'][pokemon_db['blastoise']['moves'].index('ice-beam')],
                    pokemon_db['blastoise']['moves'][pokemon_db['blastoise']['moves'].index('hydro-pump')],
                    pokemon_db['blastoise']['moves'][pokemon_db['blastoise']['moves'].index('earthquake')],
                    pokemon_db['blastoise']['moves'][pokemon_db['blastoise']['moves'].index('blizzard')]
                ]
            ),
            Pokemon(
                pokemon_db['machamp'],
                50,
                [ 
                    pokemon_db['machamp']['moves'][pokemon_db['machamp']['moves'].index('earthquake')],
                    pokemon_db['machamp']['moves'][pokemon_db['machamp']['moves'].index('ice-punch')],
                    pokemon_db['machamp']['moves'][pokemon_db['machamp']['moves'].index('karate-chop')],
                    pokemon_db['machamp']['moves'][pokemon_db['machamp']['moves'].index('focus-blast')]
                ]
            ),
            Pokemon(
                pokemon_db['rhydon'],
                50,
                [ 
                    pokemon_db['rhydon']['moves'][pokemon_db['rhydon']['moves'].index('rock-slide')],
                    pokemon_db['rhydon']['moves'][pokemon_db['rhydon']['moves'].index('megahorn')],
                    pokemon_db['rhydon']['moves'][pokemon_db['rhydon']['moves'].index('brick-break')],
                    pokemon_db['rhydon']['moves'][pokemon_db['rhydon']['moves'].index('thunderbolt')]
                ]
            ),
        ]
    },
}

def main():
    player = Player(TEAM['red']['name'], TEAM['red']['team'])
    ai = AI(TEAM['blue']['name'], TEAM['blue']['team'])

    result = ai.main_battle(player)
    print(result)



if __name__ == '__main__':
    main()
