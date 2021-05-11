from random import randint, choice
from pokemon import Pokemon, PokemonAI
from trainer import Trainer
from data.pokemon_db import pokemons as pokemon_db



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

def main():
    red = {
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
                pokemon_db['steelix'],
                50,
                [ 
                    pokemon_db['steelix']['moves'][pokemon_db['steelix']['moves'].index('dig')],
                    pokemon_db['steelix']['moves'][pokemon_db['steelix']['moves'].index('iron-tail')],
                    pokemon_db['steelix']['moves'][pokemon_db['steelix']['moves'].index('rock-slide')],
                    pokemon_db['steelix']['moves'][pokemon_db['steelix']['moves'].index('earthquake')]
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
    }

    blue = {
        'name': 'Blue',
        'team': [
            Pokemon(
                pokemon_db['blastoise'],
                50,
                [ 
                    pokemon_db['blastoise']['moves'][pokemon_db['blastoise']['moves'].index('earthquake')],
                    pokemon_db['blastoise']['moves'][pokemon_db['blastoise']['moves'].index('hydro-pump')],
                    pokemon_db['blastoise']['moves'][pokemon_db['blastoise']['moves'].index('bite')],
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
                pokemon_db['jolteon'],
                50,
                [ 
                    pokemon_db['jolteon']['moves'][pokemon_db['jolteon']['moves'].index('quick-attack')],
                    pokemon_db['jolteon']['moves'][pokemon_db['jolteon']['moves'].index('shadow-ball')],
                    pokemon_db['jolteon']['moves'][pokemon_db['jolteon']['moves'].index('double-kick')],
                    pokemon_db['jolteon']['moves'][pokemon_db['jolteon']['moves'].index('thunder')]
                ]
            ),
        ]
    }
    
    red = Trainer(red)
    blue = Trainer(blue)

    result = red.trainer_battle(blue)
    print(result)


if __name__ == '__main__':
    main()
