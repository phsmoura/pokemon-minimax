from util import get_effective_factor, get_damage
from data.moves_db import moves as moves_db

SCORE = 10
INFINITY = 10000

class Node:
    def __init__(self, data) -> None:
        self.children = []
        self.data = data
        self.decision = {
            'change_pkmn': False,
            'best_pkmn': '',
            'best_move': ''
        }
        self.ai_wins = False
        self.gameover = False

class Graph:
    def __init__(self) -> None:
        self.root = None
        self.frontier = []
        self.depth = 0
        self.limit = 10

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
            if get_effective_factor(move_type, player_types) >= 1:
                score_to_attack += SCORE
                if moves_db[move]['power'] > moves_db[best_move]['power']:
                    best_move = move
            else:
                score_to_change_pkmn += SCORE

        # choosing pkmn
        best_pkmn = data['ai']['team'][0]
        for pkmn in data['ai']['team']:
            ai_types = pkmn.types
            for move in self.data['player']['team'][0].moves:
                move_type = moves_db[move]['type']
                if get_effective_factor(move_type, ai_types) < 1:
                    score_to_attack += SCORE
                    best_pkmn = pkmn
                else:
                    score_to_change_pkmn += SCORE

        self.root = Node(data)
        if score_to_attack >= score_to_change_pkmn:
            self.root.decision['move'] = best_move
        else:
            self.root.decision['change_pkmn'] = True
            self.root.decision['pkmn'] = best_pkmn

    def set_states(self, node: Node, attacker, defender):
        new_node = Node(node.data)

        for pkmn in node.data[defender]['team']:
            defender_types = pkmn.types

            for move in self.data[attacker]['team'][0].moves:
                move_type = moves_db[move]['type']
                move_category = moves_db[move]['type']
                move_power = moves_db[move]['power']
                
                effective_factor = get_effective_factor(move_type, defender_types)
                pkmn.hp -= get_damage(move_category, move_power, attacker, defender, effective_factor)

                if pkmn.hp <= 0:
                    new_node.data[defender]['team'].remove(pkmn)

                if not node.data[defender]['team']:
                    if defender == 'player':
                        new_node.ai_wins = True
                    new_node.gameover = True
 
                new_node.decision['move'] = move
                node.children.append(new_node)
                self.frontier.append(new_node)
        
        # change pkmn
        for def_pkmn in node.data[defender]['team']:
            new_node.decision['change_pkmn'] = True
            new_node.decision['pkmn'] = def_pkmn
            node.children.append(new_node)
            self.frontier.append(new_node)

    def explore(self, data):
        if not self.root:
            self.set_root_node(data)
            self.frontier.append(self.root)

        for node in self.frontier:
            self.set_states(node, 'player', 'ai')
            self.set_states(node, 'ai', 'player')
            self.depth += 1

    def minimax(self, position, depth, maximizing_player):
        if depth == 0 or position.gameover:
            return
        
        if maximizing_player:
            max_eval = -INFINITY
            for child in position.children:
                eval = self.minimax(child, depth - 1, False)
                max_eval = max(eval, max_eval)
            return max_eval
        else:
            min_eval = INFINITY
            for child in position.children:
                eval = self.minimax(child, depth - 1, True)
                min_eval = min(eval, min_eval)
            return min_eval
