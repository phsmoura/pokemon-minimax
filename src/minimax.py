from util import get_effective_factor, get_damage
from pokemon import Pokemon
from data.moves_db import moves as moves_db

SCORE = 10
INFINITY = 100

class Node:
    def __init__(self, data) -> None:
        self.children = []
        self.data = data
        self.decision = {
            'change_pkmn': False,
            'pkmn': '',
            'move': ''
        }
        self.score = 0
        self.ai_wins = False
        self.gameover = False

class Graph:
    def __init__(self) -> None:
        self.root = None
        self.frontier = []
        self.depth = 0
        self.minimax_depth = 4
        self.limit = 12 * self.minimax_depth - 1 # nodes_1st_turn + total_nodes_next_turn * n

    def set_root_node(self, data):
        score_to_attack = 0
        score_to_change_pkmn = 0

        if data['ai']['team'][0].speed > data['player']['team'][0].speed:
            score_to_attack += SCORE
        else:
            score_to_change_pkmn += SCORE

        # choosing move
        player_types = data['player']['team'][0].types
        best_move = data['ai']['team'][0].moves[0]

        for move in data['ai']['team'][0].moves:
            move_type = moves_db[move]['type']
            if get_effective_factor(move_type, player_types) >= 2:
                score_to_attack += SCORE 
                if moves_db[move]['power'] > moves_db[best_move]['power']:
                    best_move = move
            else:
                score_to_change_pkmn += SCORE

        # choosing pkmn
        best_pkmn = data['ai']['team'][0]
        for pkmn in data['ai']['team'][1:]:
            ai_types = pkmn.types
            for move in data['player']['team'][0].moves:
                move_type = moves_db[move]['type']
                if get_effective_factor(move_type, ai_types) < 1:
                    score_to_attack += SCORE
                    best_pkmn = pkmn
                else:
                    score_to_change_pkmn += SCORE

        self.root = Node(data)
        if score_to_attack >= score_to_change_pkmn or len(data['ai']['team']) == 1:
            self.root.decision['move'] = best_move
        else:
            self.root.decision['change_pkmn'] = True
            self.root.decision['pkmn'] = best_pkmn

    def set_states(self, node: Node, attacker, defender):
        pkmn = node.data[defender]['team'][0]
        defender_types = pkmn.types

        for move in node.data[attacker]['team'][0].moves:
            move_type = moves_db[move]['type']
            move_category = moves_db[move]['type']
            move_power = moves_db[move]['power']
            
            effective_factor = get_effective_factor(move_type, defender_types)
            damage = get_damage(move_category, move_power, node.data[attacker]['team'][0], pkmn, effective_factor)
            # pkmn.hp -= damage

            new_node = Node(node.data)
            if effective_factor >= 2 and damage >= 70:
                new_node.score += SCORE * 6
            if effective_factor >= 2:
                new_node.score += SCORE * 4
            if damage >= pkmn.hp:
                new_node.score += SCORE * 2
            if len(node.data[defender]['team']) == 1 or effective_factor == 1:
                new_node.score += SCORE

            if pkmn.hp <= 0 and len(node.data[defender]['team']) <= 1:
                if defender == 'player':
                    new_node.ai_wins = True
                new_node.score += SCORE * INFINITY
                new_node.gameover = True

            new_node.decision['move'] = move
            node.children.append(new_node)
            self.frontier.append(new_node)
        
        # change pkmn
        for def_pkmn in node.data[attacker]['team'][1:]:
            if def_pkmn.hp <= def_pkmn.hp_full*0.15 and len(node.data[attacker]['team']) > 1:
                new_node.score += SCORE * 6

            new_node = Node(node.data)
            new_node.decision['change_pkmn'] = True
            new_node.decision['pkmn'] = def_pkmn
            node.children.append(new_node)
            self.frontier.append(new_node)

    def minimax(self, position: Node, depth, maximizing_player):
        if depth == 0 or position.gameover:
            return position.score
        
        if maximizing_player:
            max_eval = -INFINITY
            for child in position.children:
                eval = -self.minimax(child, depth - 1, False)
                max_eval = max(eval, max_eval)
                position.score -= max_eval
                # print(position.score)
            return max_eval
        else:
            min_eval = INFINITY
            for child in position.children:
                eval = self.minimax(child, depth - 1, True)
                min_eval = min(eval, min_eval)
                position.score += min_eval
                # print(position.score)
            return min_eval

    def explore(self, data, active, wait):
        self.set_root_node(data)
        self.set_states(self.root, active, wait)

        self.minimax(self.root, self.minimax_depth, True)

        return self.root