import requests
import json


def get_moves_data() -> int:
	url = "https://pokeapi.co/api/v2/move/"
	response = requests.get(url)
	content = json.loads(response.content)

	moves = dict()
	total_moves = 560 # all moves until gen 5

	print("Gathering moves data")

	for k in range(1,total_moves):
		response = requests.get(url + str(k))
		content = json.loads(response.content)

		# print(f"{content['id']}: {content['name']}: {content['generation']['name']}")

		moves[content['name']] = {
			'id': content['id'],
			'name': content['name'].title().replace('_',' '),
			'type': content['type']['name'],
			'category': content['damage_class']['name'],
			'power': content['power'],
			'pp': content['pp'],
			'accuracy': content['accuracy'],
			'priority': content['priority'],
			'description': content['effect_entries'][0]['effect'],
			'meta': {
				'ailment': {
					'name': content['meta']['ailment']['name'],
					'chance': content['meta']['ailment_chance']
				},
				'crit_rate': content['meta']['crit_rate'],
				'drain': content['meta']['drain'],
				'flinch_chance': content['meta']['flinch_chance'],
				'healing': content['meta']['healing'],
				'max_hits': content['meta']['max_hits'],
				'max_turns': content['meta']['max_turns'],
				'min_hits': content['meta']['min_hits'],
				'min_turns': content['meta']['min_turns'],
				'stat_chance': content['meta']['stat_chance'],
				'stat_changes': content['stat_changes']
			}
		}

	with open('moves_db.py','w') as f:
		f.write(f"moves = {moves}") 

	return moves


def get_pkmn_data(moves:int):
	url = 'https://pokeapi.co/api/v2/pokemon/'
	pokemon = dict()
	total_pokemon = 650 # until gen 5

	print("Gathering pokemon data")

	for k in range(1,total_pokemon):
		response = requests.get(url + str(k))
		content = json.loads(response.content)

		# print(f"{content['id']}: {content['name']}")

		pokemon[content['name']] = {
			'id': content['id'],
			'name': content['name'].title().replace('-',' '),
			'types': list(),
			'stats': {
				'hp': content['stats'][0]['base_stat'],
				'atk': content['stats'][1]['base_stat'],
				'def': content['stats'][2]['base_stat'],
				'spatk': content['stats'][3]['base_stat'],
				'spdef': content['stats'][4]['base_stat'],
				'spd': content['stats'][5]['base_stat']
			},
			'moves': list()
		}

		for pkmn_type in content['types']:
			pokemon[content['name']]['types'].append(pkmn_type['type']['name'])

		for move in content['moves']:
			# print(move['move']['name'])
			if move['move']['name'] in moves:
				pokemon[content['name']]['moves'].append(move['move']['name'])

	with open('pokemon_db.py','w') as f:
		f.write(f"pokemons = {pokemon}") 


if __name__ == '__main__':
	# get moves data
	moves = get_moves_data()

	# from moves_db import moves
	# get pokemon data
	get_pkmn_data(moves)

	
