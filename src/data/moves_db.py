moves = {
    'pound': {
        'id': 1,
        'name': 'Pound',
        'type': 'normal',
        'category': 'physical',
        'power': 40,
        'pp': 35,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'karate-chop': {
        'id': 2,
        'name': 'Karate-Chop',
        'type': 'fighting',
        'category': 'physical',
        'power': 50,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'double-slap': {
        'id': 3,
        'name': 'Double-Slap',
        'type': 'normal',
        'category': 'physical',
        'power': 15,
        'pp': 10,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits 2–5 times in one turn.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 5,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'comet-punch': {
        'id': 4,
        'name': 'Comet-Punch',
        'type': 'normal',
        'category': 'physical',
        'power': 18,
        'pp': 15,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits 2–5 times in one turn.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 5,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'mega-punch': {
        'id': 5,
        'name': 'Mega-Punch',
        'type': 'normal',
        'category': 'physical',
        'power': 80,
        'pp': 20,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'pay-day': {
        'id': 6,
        'name': 'Pay-Day',
        'type': 'normal',
        'category': 'physical',
        'power': 40,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  After the battle ends, the winner receives five times the user's level in extra money for each time this move was used.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fire-punch': {
        'id': 7,
        'name': 'Fire-Punch',
        'type': 'fire',
        'category': 'physical',
        'power': 75,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'ice-punch': {
        'id': 8,
        'name': 'Ice-Punch',
        'type': 'ice',
        'category': 'physical',
        'power': 75,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to freeze the target.',
        'meta': {
            'ailment': {
                'name': 'freeze',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'thunder-punch': {
        'id': 9,
        'name': 'Thunder-Punch',
        'type': 'electric',
        'category': 'physical',
        'power': 75,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'scratch': {
        'id': 10,
        'name': 'Scratch',
        'type': 'normal',
        'category': 'physical',
        'power': 40,
        'pp': 35,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'vice-grip': {
        'id': 11,
        'name': 'Vice-Grip',
        'type': 'normal',
        'category': 'physical',
        'power': 55,
        'pp': 30,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'guillotine': {
        'id': 12,
        'name': 'Guillotine',
        'type': 'normal',
        'category': 'physical',
        'power': None,
        'pp': 5,
        'accuracy': 30,
        'priority': 0,
        'description': "Inflicts damage equal to the target's max HP.  Ignores accuracy and evasion modifiers.  This move's accuracy is 30% plus 1% for each level the user is higher than the target.  If the user is a lower level than the target, this move will fail.\n\nBecause this move inflicts a specific and finite amount of damage, endure still prevents the target from fainting.\n\nThe effects of lock on, mind reader, and no guard still apply, as long as the user is equal or higher level than the target.  However, they will not give this move a chance to break through detect or protect.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'razor-wind': {
        'id': 13,
        'name': 'Razor-Wind',
        'type': 'normal',
        'category': 'special',
        'power': 80,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.  User charges for one turn before attacking.\n\nThis move cannot be selected by sleep talk.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'swords-dance': {
        'id': 14,
        'name': 'Swords-Dance',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Attack by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 2,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }]
        }
    },
    'cut': {
        'id': 15,
        'name': 'Cut',
        'type': 'normal',
        'category': 'physical',
        'power': 50,
        'pp': 30,
        'accuracy': 95,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'gust': {
        'id': 16,
        'name': 'Gust',
        'type': 'flying',
        'category': 'special',
        'power': 40,
        'pp': 35,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.\n\nIf the target is under the effect of bounce, fly, or sky drop, this move will hit with double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'wing-attack': {
        'id': 17,
        'name': 'Wing-Attack',
        'type': 'flying',
        'category': 'physical',
        'power': 60,
        'pp': 35,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'whirlwind': {
        'id': 18,
        'name': 'Whirlwind',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': -6,
        'description': "Switches the target out for another of its trainer's Pokémon selected at random.  Wild battles end immediately.\n\nDoesn't affect Pokémon with suction cups or under the effect of ingrain.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fly': {
        'id': 19,
        'name': 'Fly',
        'type': 'flying',
        'category': 'physical',
        'power': 90,
        'pp': 15,
        'accuracy': 95,
        'priority': 0,
        'description': 'Inflicts regular damage.  User flies high into the air for one turn, becoming immune to attack, and hits on the second turn.\n\nDuring the immune turn, gust, hurricane, sky uppercut, smack down, thunder, twister, and whirlwind still hit the user normally.  gust and twister also have double power against the user.\n\nThe damage from hail and sandstorm still applies during the immune turn.\n\nThe user may be hit during its immune turn if under the effect of lock on, mind reader, or no guard.\n\nThis move cannot be used while gravity is in effect.\n\nThis move cannot be selected by sleep talk.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'bind': {
        'id': 20,
        'name': 'Bind',
        'type': 'normal',
        'category': 'physical',
        'power': 15,
        'pp': 20,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  For the next 2–5 turns, the target cannot leave the field and is damaged for 1/16 its max HP at the end of each turn.  The user continues to use other moves during this time.  If the user leaves the field, this effect ends.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.\n\nrapid spin cancels this effect.',
        'meta': {
            'ailment': {
                'name': 'trap',
                'chance': 100
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 6,
            'min_hits': None,
            'min_turns': 5,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'slam': {
        'id': 21,
        'name': 'Slam',
        'type': 'normal',
        'category': 'physical',
        'power': 80,
        'pp': 20,
        'accuracy': 75,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'vine-whip': {
        'id': 22,
        'name': 'Vine-Whip',
        'type': 'grass',
        'category': 'physical',
        'power': 45,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'stomp': {
        'id': 23,
        'name': 'Stomp',
        'type': 'normal',
        'category': 'physical',
        'power': 65,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.\n\nPower is doubled against Pokémon that have used minimize since entering the field.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'double-kick': {
        'id': 24,
        'name': 'Double-Kick',
        'type': 'fighting',
        'category': 'physical',
        'power': 30,
        'pp': 30,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits twice in one turn.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 2,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'mega-kick': {
        'id': 25,
        'name': 'Mega-Kick',
        'type': 'normal',
        'category': 'physical',
        'power': 120,
        'pp': 5,
        'accuracy': 75,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'jump-kick': {
        'id': 26,
        'name': 'Jump-Kick',
        'type': 'fighting',
        'category': 'physical',
        'power': 100,
        'pp': 10,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  If this move misses, is blocked by protect or detect, or has no effect, the user takes half the damage it would have inflicted in recoil.  This recoil damage will not exceed half the user's max HP.\n\nThis move cannot be used while gravity is in effect.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'rolling-kick': {
        'id': 27,
        'name': 'Rolling-Kick',
        'type': 'fighting',
        'category': 'physical',
        'power': 60,
        'pp': 15,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sand-attack': {
        'id': 28,
        'name': 'Sand-Attack',
        'type': 'ground',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's accuracy by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'accuracy',
                    'url': 'https://pokeapi.co/api/v2/stat/7/'
                }
            }]
        }
    },
    'headbutt': {
        'id': 29,
        'name': 'Headbutt',
        'type': 'normal',
        'category': 'physical',
        'power': 70,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'horn-attack': {
        'id': 30,
        'name': 'Horn-Attack',
        'type': 'normal',
        'category': 'physical',
        'power': 65,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fury-attack': {
        'id': 31,
        'name': 'Fury-Attack',
        'type': 'normal',
        'category': 'physical',
        'power': 15,
        'pp': 20,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits 2–5 times in one turn.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 5,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'horn-drill': {
        'id': 32,
        'name': 'Horn-Drill',
        'type': 'normal',
        'category': 'physical',
        'power': None,
        'pp': 5,
        'accuracy': 30,
        'priority': 0,
        'description': "Inflicts damage equal to the target's max HP.  Ignores accuracy and evasion modifiers.  This move's accuracy is 30% plus 1% for each level the user is higher than the target.  If the user is a lower level than the target, this move will fail.\n\nBecause this move inflicts a specific and finite amount of damage, endure still prevents the target from fainting.\n\nThe effects of lock on, mind reader, and no guard still apply, as long as the user is equal or higher level than the target.  However, they will not give this move a chance to break through detect or protect.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'tackle': {
        'id': 33,
        'name': 'Tackle',
        'type': 'normal',
        'category': 'physical',
        'power': 40,
        'pp': 35,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'body-slam': {
        'id': 34,
        'name': 'Body-Slam',
        'type': 'normal',
        'category': 'physical',
        'power': 85,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'wrap': {
        'id': 35,
        'name': 'Wrap',
        'type': 'normal',
        'category': 'physical',
        'power': 15,
        'pp': 20,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  For the next 2–5 turns, the target cannot leave the field and is damaged for 1/16 its max HP at the end of each turn.  The user continues to use other moves during this time.  If the user leaves the field, this effect ends.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.\n\nrapid spin cancels this effect.',
        'meta': {
            'ailment': {
                'name': 'trap',
                'chance': 100
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 6,
            'min_hits': None,
            'min_turns': 5,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'take-down': {
        'id': 36,
        'name': 'Take-Down',
        'type': 'normal',
        'category': 'physical',
        'power': 90,
        'pp': 20,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  User takes 1/4 the damage it inflicts in recoil.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': -25,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'thrash': {
        'id': 37,
        'name': 'Thrash',
        'type': 'normal',
        'category': 'physical',
        'power': 120,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User is forced to attack with this move for 2–3 turns,selected at random.  After the last hit, the user becomes confused.\n\nsafeguard does not protect against the confusion from this move.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'double-edge': {
        'id': 38,
        'name': 'Double-Edge',
        'type': 'normal',
        'category': 'physical',
        'power': 120,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User takes 1/3 the damage it inflicts in recoil.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': -33,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'tail-whip': {
        'id': 39,
        'name': 'Tail-Whip',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'poison-sting': {
        'id': 40,
        'name': 'Poison-Sting',
        'type': 'poison',
        'category': 'physical',
        'power': 15,
        'pp': 35,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to poison the target.',
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'twineedle': {
        'id': 41,
        'name': 'Twineedle',
        'type': 'bug',
        'category': 'physical',
        'power': 25,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits twice in the same turn.  Has a $effect_chance% chance to poison the target.',
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 20
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 2,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'pin-missile': {
        'id': 42,
        'name': 'Pin-Missile',
        'type': 'bug',
        'category': 'physical',
        'power': 25,
        'pp': 20,
        'accuracy': 95,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits 2–5 times in one turn.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 5,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'leer': {
        'id': 43,
        'name': 'Leer',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'bite': {
        'id': 44,
        'name': 'Bite',
        'type': 'dark',
        'category': 'physical',
        'power': 60,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'growl': {
        'id': 45,
        'name': 'Growl',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's Attack by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }]
        }
    },
    'roar': {
        'id': 46,
        'name': 'Roar',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': -6,
        'description': "Switches the target out for another of its trainer's Pokémon selected at random.  Wild battles end immediately.\n\nDoesn't affect Pokémon with suction cups or under the effect of ingrain.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sing': {
        'id': 47,
        'name': 'Sing',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 55,
        'priority': 0,
        'description': 'Puts the target to sleep.',
        'meta': {
            'ailment': {
                'name': 'sleep',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 4,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'supersonic': {
        'id': 48,
        'name': 'Supersonic',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 55,
        'priority': 0,
        'description': 'Confuses the target.',
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sonic-boom': {
        'id': 49,
        'name': 'Sonic-Boom',
        'type': 'normal',
        'category': 'special',
        'power': None,
        'pp': 20,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts exactly 20 damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'disable': {
        'id': 50,
        'name': 'Disable',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Disables the target's last used move, preventing its use for 4–7 turns, selected at random, or until the target leaves the field.  If the target hasn't used a move since entering the field, if it tried to use a move this turn and failed,  if its last used move has 0 PP remaining, or if it already has a move disabled, this move will fail.",
        'meta': {
            'ailment': {
                'name': 'disable',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 4,
            'min_hits': None,
            'min_turns': 4,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'acid': {
        'id': 51,
        'name': 'Acid',
        'type': 'poison',
        'category': 'special',
        'power': 40,
        'pp': 30,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Special Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'ember': {
        'id': 52,
        'name': 'Ember',
        'type': 'fire',
        'category': 'special',
        'power': 40,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'flamethrower': {
        'id': 53,
        'name': 'Flamethrower',
        'type': 'fire',
        'category': 'special',
        'power': 90,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'mist': {
        'id': 54,
        'name': 'Mist',
        'type': 'ice',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': None,
        'priority': 0,
        'description': "Pokémon on the user's side of the field are immune to stat-lowering effects for five turns.\n\nguard swap, heart swap, and power swap may still be used.\n\ndefog used by an opponent will end this effect.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'water-gun': {
        'id': 55,
        'name': 'Water-Gun',
        'type': 'water',
        'category': 'special',
        'power': 40,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'hydro-pump': {
        'id': 56,
        'name': 'Hydro-Pump',
        'type': 'water',
        'category': 'special',
        'power': 110,
        'pp': 5,
        'accuracy': 80,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'surf': {
        'id': 57,
        'name': 'Surf',
        'type': 'water',
        'category': 'special',
        'power': 90,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.\n\nIf the target is in the first turn of dive, this move will hit with double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'ice-beam': {
        'id': 58,
        'name': 'Ice-Beam',
        'type': 'ice',
        'category': 'special',
        'power': 90,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to freeze the target.',
        'meta': {
            'ailment': {
                'name': 'freeze',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'blizzard': {
        'id': 59,
        'name': 'Blizzard',
        'type': 'ice',
        'category': 'special',
        'power': 110,
        'pp': 5,
        'accuracy': 70,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to freeze the target.\n\nDuring hail, this move has 100% accuracy.  It also has a (100 - accuracy)% chance to break through the protection of protect and detect.',
        'meta': {
            'ailment': {
                'name': 'freeze',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'psybeam': {
        'id': 60,
        'name': 'Psybeam',
        'type': 'psychic',
        'category': 'special',
        'power': 65,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to confuse the target.',
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'bubble-beam': {
        'id': 61,
        'name': 'Bubble-Beam',
        'type': 'water',
        'category': 'special',
        'power': 65,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Speed by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'aurora-beam': {
        'id': 62,
        'name': 'Aurora-Beam',
        'type': 'ice',
        'category': 'special',
        'power': 65,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Attack by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }]
        }
    },
    'hyper-beam': {
        'id': 63,
        'name': 'Hyper-Beam',
        'type': 'normal',
        'category': 'special',
        'power': 150,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  User loses its next turn to "recharge", and cannot attack or switch out during that turn.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'peck': {
        'id': 64,
        'name': 'Peck',
        'type': 'flying',
        'category': 'physical',
        'power': 35,
        'pp': 35,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'drill-peck': {
        'id': 65,
        'name': 'Drill-Peck',
        'type': 'flying',
        'category': 'physical',
        'power': 80,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'submission': {
        'id': 66,
        'name': 'Submission',
        'type': 'fighting',
        'category': 'physical',
        'power': 80,
        'pp': 20,
        'accuracy': 80,
        'priority': 0,
        'description': 'Inflicts regular damage.  User takes 1/4 the damage it inflicts in recoil.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': -25,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'low-kick': {
        'id': 67,
        'name': 'Low-Kick',
        'type': 'fighting',
        'category': 'physical',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power increases with the target's weight in kilograms, to a maximum of 120.\n\nTarget's weight | Power\n--------------- | ----:\nUp to 10kg      |    20\nUp to 25kg      |    40\nUp to 50kg      |    60\nUp to 100kg     |    80\nUp to 200kg     |   100\nAbove 200kg     |   120\n",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'counter': {
        'id': 68,
        'name': 'Counter',
        'type': 'fighting',
        'category': 'physical',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': -5,
        'description': 'Targets the last opposing Pokémon to hit the user with a physical move this turn.  Inflicts twice the damage that move did to the user.  If there is no eligible target, this move will fail.  Type immunity applies, but other type effects are ignored.\n\nThis move cannot be copied by mirror move, nor selected by assist or metronome.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'seismic-toss': {
        'id': 69,
        'name': 'Seismic-Toss',
        'type': 'fighting',
        'category': 'physical',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts damage equal to the user's level.  Type immunity applies, but other type effects are ignored.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'strength': {
        'id': 70,
        'name': 'Strength',
        'type': 'normal',
        'category': 'physical',
        'power': 80,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'absorb': {
        'id': 71,
        'name': 'Absorb',
        'type': 'grass',
        'category': 'special',
        'power': 20,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Drains half the damage inflicted to heal the user.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 50,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'mega-drain': {
        'id': 72,
        'name': 'Mega-Drain',
        'type': 'grass',
        'category': 'special',
        'power': 40,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Drains half the damage inflicted to heal the user.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 50,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'leech-seed': {
        'id': 73,
        'name': 'Leech-Seed',
        'type': 'grass',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': 'Plants a seed on the target that drains 1/8 of its max HP at the end of every turn and heals the user for the amount taken.  Has no effect on grass Pokémon.  The seed remains until the target leaves the field.\n\nThe user takes damage instead of being healed if the target has liquid ooze.\n\nrapid spin will remove this effect.\n\nThis effect is passed on by baton pass.',
        'meta': {
            'ailment': {
                'name': 'leech-seed',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'growth': {
        'id': 74,
        'name': 'Growth',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Attack and Special Attack by one stage each.  During sunny day, raises both stats by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'razor-leaf': {
        'id': 75,
        'name': 'Razor-Leaf',
        'type': 'grass',
        'category': 'physical',
        'power': 55,
        'pp': 25,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'solar-beam': {
        'id': 76,
        'name': 'Solar-Beam',
        'type': 'grass',
        'category': 'special',
        'power': 120,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User charges for one turn before attacking.\n\nDuring sunny day, the charge turn is skipped.\n\nDuring hail, rain dance, or sandstorm, power is halved.\n\nThis move cannot be selected by sleep talk.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'poison-powder': {
        'id': 77,
        'name': 'Poison-Powder',
        'type': 'poison',
        'category': 'status',
        'power': None,
        'pp': 35,
        'accuracy': 75,
        'priority': 0,
        'description': 'Poisons the target.',
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'stun-spore': {
        'id': 78,
        'name': 'Stun-Spore',
        'type': 'grass',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': 75,
        'priority': 0,
        'description': 'Paralyzes the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sleep-powder': {
        'id': 79,
        'name': 'Sleep-Powder',
        'type': 'grass',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 75,
        'priority': 0,
        'description': 'Puts the target to sleep.',
        'meta': {
            'ailment': {
                'name': 'sleep',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 4,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'petal-dance': {
        'id': 80,
        'name': 'Petal-Dance',
        'type': 'grass',
        'category': 'special',
        'power': 120,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User is forced to attack with this move for 2–3 turns,selected at random.  After the last hit, the user becomes confused.\n\nsafeguard does not protect against the confusion from this move.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'string-shot': {
        'id': 81,
        'name': 'String-Shot',
        'type': 'bug',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': 95,
        'priority': 0,
        'description': "Lowers the target's Speed by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'dragon-rage': {
        'id': 82,
        'name': 'Dragon-Rage',
        'type': 'dragon',
        'category': 'special',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts exactly 40 damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fire-spin': {
        'id': 83,
        'name': 'Fire-Spin',
        'type': 'fire',
        'category': 'special',
        'power': 35,
        'pp': 15,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  For the next 2–5 turns, the target cannot leave the field and is damaged for 1/16 its max HP at the end of each turn.  The user continues to use other moves during this time.  If the user leaves the field, this effect ends.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.\n\nrapid spin cancels this effect.',
        'meta': {
            'ailment': {
                'name': 'trap',
                'chance': 100
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 6,
            'min_hits': None,
            'min_turns': 5,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'thunder-shock': {
        'id': 84,
        'name': 'Thunder-Shock',
        'type': 'electric',
        'category': 'special',
        'power': 40,
        'pp': 30,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'thunderbolt': {
        'id': 85,
        'name': 'Thunderbolt',
        'type': 'electric',
        'category': 'special',
        'power': 90,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'thunder-wave': {
        'id': 86,
        'name': 'Thunder-Wave',
        'type': 'electric',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 90,
        'priority': 0,
        'description': 'Paralyzes the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'thunder': {
        'id': 87,
        'name': 'Thunder',
        'type': 'electric',
        'category': 'special',
        'power': 110,
        'pp': 10,
        'accuracy': 70,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target.\n\nDuring rain dance, this move has 100% accuracy.  It also has a (100 - accuracy)% chance to break through the protection of protect and detect.\n\nDuring sunny day, this move has 50% accuracy.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'rock-throw': {
        'id': 88,
        'name': 'Rock-Throw',
        'type': 'rock',
        'category': 'physical',
        'power': 50,
        'pp': 15,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'earthquake': {
        'id': 89,
        'name': 'Earthquake',
        'type': 'ground',
        'category': 'physical',
        'power': 100,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.\n\nIf the target is in the first turn of dig, this move will hit with double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fissure': {
        'id': 90,
        'name': 'Fissure',
        'type': 'ground',
        'category': 'physical',
        'power': None,
        'pp': 5,
        'accuracy': 30,
        'priority': 0,
        'description': "Inflicts damage equal to the target's max HP.  Ignores accuracy and evasion modifiers.  This move's accuracy is 30% plus 1% for each level the user is higher than the target.  If the user is a lower level than the target, this move will fail.\n\nBecause this move inflicts a specific and finite amount of damage, endure still prevents the target from fainting.\n\nThe effects of lock on, mind reader, and no guard still apply, as long as the user is equal or higher level than the target.  However, they will not give this move a chance to break through detect or protect.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'dig': {
        'id': 91,
        'name': 'Dig',
        'type': 'ground',
        'category': 'physical',
        'power': 80,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User digs underground for one turn, becoming immune to attack, and hits on the second turn.\n\nDuring the immune turn, earthquake, fissure, and magnitude still hit the user normally, and their power is doubled if appropriate.\n\nThe user may be hit during its immune turn if under the effect of lock on, mind reader, or no guard.\n\nThis move cannot be selected by sleep talk.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'toxic': {
        'id': 92,
        'name': 'Toxic',
        'type': 'poison',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': 'Badly poisons the target.  Never misses when used by a poison-type Pokémon.',
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 15,
            'min_hits': None,
            'min_turns': 15,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'confusion': {
        'id': 93,
        'name': 'Confusion',
        'type': 'psychic',
        'category': 'special',
        'power': 50,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to confuse the target.',
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'psychic': {
        'id': 94,
        'name': 'Psychic',
        'type': 'psychic',
        'category': 'special',
        'power': 90,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Special Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'hypnosis': {
        'id': 95,
        'name': 'Hypnosis',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 60,
        'priority': 0,
        'description': 'Puts the target to sleep.',
        'meta': {
            'ailment': {
                'name': 'sleep',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 4,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'meditate': {
        'id': 96,
        'name': 'Meditate',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Attack by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }]
        }
    },
    'agility': {
        'id': 97,
        'name': 'Agility',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Speed by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 2,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'quick-attack': {
        'id': 98,
        'name': 'Quick-Attack',
        'type': 'normal',
        'category': 'physical',
        'power': 40,
        'pp': 30,
        'accuracy': 100,
        'priority': 1,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'rage': {
        'id': 99,
        'name': 'Rage',
        'type': 'normal',
        'category': 'physical',
        'power': 20,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Every time the user is hit after it uses this move but before its next action, its Attack raises by one stage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'teleport': {
        'id': 100,
        'name': 'Teleport',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Does nothing.  Wild battles end immediately.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'night-shade': {
        'id': 101,
        'name': 'Night-Shade',
        'type': 'ghost',
        'category': 'special',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts damage equal to the user's level.  Type immunity applies, but other type effects are ignored.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'mimic': {
        'id': 102,
        'name': 'Mimic',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "This move is replaced by the target's last successfully used move, and its PP changes to 5.  If the target hasn't used a move since entering the field, if it tried to use a move this turn and failed, or if the user already knows the targeted move, this move will fail.  This effect vanishes when the user leaves the field.\n\nIf chatter, metronome, mimic, sketch, or struggle is selected, this move will fail.\n\nThis move cannot be copied by mirror move, nor selected by assist or metronome, nor forced by encore.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'screech': {
        'id': 103,
        'name': 'Screech',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': 85,
        'priority': 0,
        'description': "Lowers the target's Defense by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'double-team': {
        'id': 104,
        'name': 'Double-Team',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's evasion by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'evasion',
                    'url': 'https://pokeapi.co/api/v2/stat/8/'
                }
            }]
        }
    },
    'recover': {
        'id': 105,
        'name': 'Recover',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'Heals the user for half its max HP.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 50,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'harden': {
        'id': 106,
        'name': 'Harden',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'minimize': {
        'id': 107,
        'name': 'Minimize',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's evasion by two stages.\n\nstomp and steamroller have double power against Pokémon that have used this move since entering the field.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 2,
                'stat': {
                    'name': 'evasion',
                    'url': 'https://pokeapi.co/api/v2/stat/8/'
                }
            }]
        }
    },
    'smokescreen': {
        'id': 108,
        'name': 'Smokescreen',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's accuracy by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'accuracy',
                    'url': 'https://pokeapi.co/api/v2/stat/7/'
                }
            }]
        }
    },
    'confuse-ray': {
        'id': 109,
        'name': 'Confuse-Ray',
        'type': 'ghost',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Confuses the target.',
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'withdraw': {
        'id': 110,
        'name': 'Withdraw',
        'type': 'water',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'defense-curl': {
        'id': 111,
        'name': 'Defense-Curl',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': None,
        'priority': 0,
        'description': "Raises user's Defense by one stage.\n\nAfter this move is used, the power of ice ball and rollout are doubled until the user leaves the field.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'barrier': {
        'id': 112,
        'name': 'Barrier',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Defense by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 2,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'light-screen': {
        'id': 113,
        'name': 'Light-Screen',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': None,
        'priority': 0,
        'description': "Erects a barrier around the user's side of the field that reduces damage from special attacks by half for five turns.  In double battles, the reduction is 1/3.  Critical hits are not affected by the barrier.\n\nIf the user is holding light clay, the barrier lasts for eight turns.\n\nbrick break or defog used by an opponent will destroy the barrier.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'haze': {
        'id': 114,
        'name': 'Haze',
        'type': 'ice',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': None,
        'priority': 0,
        'description': 'Removes stat, accuracy, and evasion modifiers from every Pokémon on the field.\n\nThis does not count as a stat reduction for the purposes of clear body or white smoke.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'reflect': {
        'id': 115,
        'name': 'Reflect',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Erects a barrier around the user's side of the field that reduces damage from physical attacks by half for five turns.  In double battles, the reduction is 1/3.  Critical hits are not affected by the barrier.\n\nIf the user is holding light clay, the barrier lasts for eight turns.\n\nbrick break or defog used by an opponent will destroy the barrier.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'focus-energy': {
        'id': 116,
        'name': 'Focus-Energy',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': None,
        'priority': 0,
        'description': "User's critical hit rate is two levels higher until it leaves the field.  If the user has already used focus energy since entering the field, this move will fail.\n\nThis effect is passed on by baton pass.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'bide': {
        'id': 117,
        'name': 'Bide',
        'type': 'normal',
        'category': 'physical',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 1,
        'description': 'User waits for two turns.  On the second turn, the user inflicts twice the damage it accumulated on the last Pokémon to hit it.  Damage inflicted is typeless.\n\nThis move cannot be selected by sleep talk.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'metronome': {
        'id': 118,
        'name': 'Metronome',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'Selects any move at random and uses it.  Moves the user already knows are not eligible.  Assist, meta, protection, and reflection moves are also not eligible; specifically, assist, chatter, copycat, counter, covet, destiny bond, detect, endure, feint, focus punch, follow me, helping hand, me first, metronome, mimic, mirror coat, mirror move, protect, quick guard, sketch, sleep talk, snatch, struggle, switcheroo, thief, trick, and wide guard will not be selected by this move.\n\nThis move cannot be copied by mimic or mirror move, nor selected by assist, metronome, or sleep talk.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'mirror-move': {
        'id': 119,
        'name': 'Mirror-Move',
        'type': 'flying',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Uses the last move targeted at the user by a Pokémon still on the field.  A move counts as targeting the user even if it hit multiple Pokémon, as long as the user was one of them; however, moves targeting the field itself do not count.  If the user has not been targeted by an appropriate move since entering the field, or if no Pokémon that targeted the user remains on the field, this move will fail.\n\nMoves that failed, missed, had no effect, or were blocked are still copied.\n\nAssist moves, time-delayed moves, “meta” moves that operate on other moves/Pokémon/abilities, and some other special moves cannot be copied and are ignored; if the last move to hit the user was such a move, the previous move will be used instead.  The full list of ignored moves is: acid armor, acupressure, after you, agility, ally switch, amnesia, aqua ring, aromatherapy, aromatic mist, assist, autotomize, barrier, baton pass, belch, belly drum, bide, bulk up, calm mind, camouflage, celebrate, charge, coil, conversion, conversion 2, copycat, cosmic power, cotton guard, counter, crafty shield, curse, defend order, defense curl, destiny bond, detect, doom desire, double team, dragon dance, electric terrain, endure, final gambit, flower shield, focus energy, focus punch, follow me, future sight, geomancy, grassy terrain, gravity, growth, grudge, guard split, hail, happy hour, harden, haze, heal bell, heal order, heal pulse, healing wish, helping hand, hold hands, hone claws, howl, imprison, ingrain, ion deluge, iron defense, kings shield, light screen, lucky chant, lunar dance, magic coat, magnet rise, magnetic flux, mat block, me first, meditate, metronome, milk drink, mimic, minimize, mirror coat, mirror move, mist, misty terrain, moonlight, morning sun, mud sport, nasty plot, nature power, perish song, power split, power trick, protect, psych up, quick guard, quiver dance, rage powder, rain dance, recover, recycle, reflect, reflect type, refresh, rest, rock polish, role play, roost, rototiller, safeguard, sandstorm, shadow blast, shadow bolt, shadow half, shadow rush, shadow shed, shadow sky, shadow storm, shadow wave, sharpen, shell smash, shift gear, sketch, slack off, sleep talk, snatch, soft boiled, spikes, spiky shield, spit up, splash, stealth rock, sticky web, stockpile, struggle, substitute, sunny day, swallow, swords dance, synthesis, tail glow, tailwind, teleport, toxic spikes, transform, water sport, wide guard, wish, withdraw and work up.\n\nThis move cannot be selected by assist, metronome, or sleep talk, nor forced by encore.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'self-destruct': {
        'id': 120,
        'name': 'Self-Destruct',
        'type': 'normal',
        'category': 'physical',
        'power': 200,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': 'User faints, even if the attack fails or misses.  Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'egg-bomb': {
        'id': 121,
        'name': 'Egg-Bomb',
        'type': 'normal',
        'category': 'physical',
        'power': 100,
        'pp': 10,
        'accuracy': 75,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'lick': {
        'id': 122,
        'name': 'Lick',
        'type': 'ghost',
        'category': 'physical',
        'power': 30,
        'pp': 30,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'smog': {
        'id': 123,
        'name': 'Smog',
        'type': 'poison',
        'category': 'special',
        'power': 30,
        'pp': 20,
        'accuracy': 70,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to poison the target.',
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 40
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sludge': {
        'id': 124,
        'name': 'Sludge',
        'type': 'poison',
        'category': 'special',
        'power': 65,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to poison the target.',
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'bone-club': {
        'id': 125,
        'name': 'Bone-Club',
        'type': 'ground',
        'category': 'physical',
        'power': 65,
        'pp': 20,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 10,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fire-blast': {
        'id': 126,
        'name': 'Fire-Blast',
        'type': 'fire',
        'category': 'special',
        'power': 110,
        'pp': 5,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'waterfall': {
        'id': 127,
        'name': 'Waterfall',
        'type': 'water',
        'category': 'physical',
        'power': 80,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 20,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'clamp': {
        'id': 128,
        'name': 'Clamp',
        'type': 'water',
        'category': 'physical',
        'power': 35,
        'pp': 15,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  For the next 2–5 turns, the target cannot leave the field and is damaged for 1/16 its max HP at the end of each turn.  The user continues to use other moves during this time.  If the user leaves the field, this effect ends.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.\n\nrapid spin cancels this effect.',
        'meta': {
            'ailment': {
                'name': 'trap',
                'chance': 100
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 6,
            'min_hits': None,
            'min_turns': 5,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'swift': {
        'id': 129,
        'name': 'Swift',
        'type': 'normal',
        'category': 'special',
        'power': 60,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Inflicts regular damage.  Ignores accuracy and evasion modifiers.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'skull-bash': {
        'id': 130,
        'name': 'Skull-Bash',
        'type': 'normal',
        'category': 'physical',
        'power': 130,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Raises the user's Defense by one stage.  User then charges for one turn before attacking.\n\nThis move cannot be selected by sleep talk.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 100
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'spike-cannon': {
        'id': 131,
        'name': 'Spike-Cannon',
        'type': 'normal',
        'category': 'physical',
        'power': 20,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits 2–5 times in one turn.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 5,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'constrict': {
        'id': 132,
        'name': 'Constrict',
        'type': 'normal',
        'category': 'physical',
        'power': 10,
        'pp': 35,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Speed by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'amnesia': {
        'id': 133,
        'name': 'Amnesia',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Special Defense by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 2,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'kinesis': {
        'id': 134,
        'name': 'Kinesis',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 80,
        'priority': 0,
        'description': "Lowers the target's accuracy by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'accuracy',
                    'url': 'https://pokeapi.co/api/v2/stat/7/'
                }
            }]
        }
    },
    'soft-boiled': {
        'id': 135,
        'name': 'Soft-Boiled',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'Heals the user for half its max HP.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 50,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'high-jump-kick': {
        'id': 136,
        'name': 'High-Jump-Kick',
        'type': 'fighting',
        'category': 'physical',
        'power': 130,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': "Inflicts regular damage.  If this move misses, is blocked by protect or detect, or has no effect, the user takes half the damage it would have inflicted in recoil.  This recoil damage will not exceed half the user's max HP.\n\nThis move cannot be used while gravity is in effect.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'glare': {
        'id': 137,
        'name': 'Glare',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': 100,
        'priority': 0,
        'description': 'Paralyzes the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'dream-eater': {
        'id': 138,
        'name': 'Dream-Eater',
        'type': 'psychic',
        'category': 'special',
        'power': 100,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Fails if not used on a sleeping Pokémon.  Inflicts regular damage.  Drains half the damage inflicted to heal the user.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 50,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'poison-gas': {
        'id': 139,
        'name': 'Poison-Gas',
        'type': 'poison',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': 90,
        'priority': 0,
        'description': 'Poisons the target.',
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'barrage': {
        'id': 140,
        'name': 'Barrage',
        'type': 'normal',
        'category': 'physical',
        'power': 15,
        'pp': 20,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits 2–5 times in one turn.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 5,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'leech-life': {
        'id': 141,
        'name': 'Leech-Life',
        'type': 'bug',
        'category': 'physical',
        'power': 80,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Drains half the damage inflicted to heal the user.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 50,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'lovely-kiss': {
        'id': 142,
        'name': 'Lovely-Kiss',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 75,
        'priority': 0,
        'description': 'Puts the target to sleep.',
        'meta': {
            'ailment': {
                'name': 'sleep',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 4,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sky-attack': {
        'id': 143,
        'name': 'Sky-Attack',
        'type': 'flying',
        'category': 'physical',
        'power': 140,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  User charges for one turn before attacking.  Critical hit chance is one level higher than normal.  Has a $effect_chance% chance to make the target flinch.\n\nThis move cannot be selected by sleep talk.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'transform': {
        'id': 144,
        'name': 'Transform',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "User copies the target's species, weight, type, ability, calculated stats (except HP), and moves.  Copied moves will all have 5 PP remaining.  IVs are copied for the purposes of hidden power, but stats are not recalculated.\n\nchoice band, choice scarf, and choice specs stay in effect, and the user must select a new move.\n\nThis move cannot be copied by mirror move, nor forced by encore.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'bubble': {
        'id': 145,
        'name': 'Bubble',
        'type': 'water',
        'category': 'special',
        'power': 40,
        'pp': 30,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Speed by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'dizzy-punch': {
        'id': 146,
        'name': 'Dizzy-Punch',
        'type': 'normal',
        'category': 'physical',
        'power': 70,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to confuse the target.',
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 20
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'spore': {
        'id': 147,
        'name': 'Spore',
        'type': 'grass',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Puts the target to sleep.',
        'meta': {
            'ailment': {
                'name': 'sleep',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 4,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'flash': {
        'id': 148,
        'name': 'Flash',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's accuracy by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'accuracy',
                    'url': 'https://pokeapi.co/api/v2/stat/7/'
                }
            }]
        }
    },
    'psywave': {
        'id': 149,
        'name': 'Psywave',
        'type': 'psychic',
        'category': 'special',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts typeless damage between 50% and 150% of the user's level, selected at random in increments of 10%.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'splash': {
        'id': 150,
        'name': 'Splash',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': None,
        'priority': 0,
        'description': 'Does nothing.\n\nThis move cannot be used while gravity is in effect.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'acid-armor': {
        'id': 151,
        'name': 'Acid-Armor',
        'type': 'poison',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Defense by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 2,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'crabhammer': {
        'id': 152,
        'name': 'Crabhammer',
        'type': 'water',
        'category': 'physical',
        'power': 100,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'explosion': {
        'id': 153,
        'name': 'Explosion',
        'type': 'normal',
        'category': 'physical',
        'power': 250,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': 'User faints, even if the attack fails or misses.  Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fury-swipes': {
        'id': 154,
        'name': 'Fury-Swipes',
        'type': 'normal',
        'category': 'physical',
        'power': 18,
        'pp': 15,
        'accuracy': 80,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits 2–5 times in one turn.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 5,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'bonemerang': {
        'id': 155,
        'name': 'Bonemerang',
        'type': 'ground',
        'category': 'physical',
        'power': 50,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits twice in one turn.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 2,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'rest': {
        'id': 156,
        'name': 'Rest',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'User falls to sleep and immediately regains all its HP.  If the user has another major status effect, sleep will replace it.  The user will always wake up after two turns, or one turn with early bird.\n\nThis move fails if the Pokémon cannot fall asleep due to uproar, insomnia, or vital spirit.  It also fails if the Pokémon is at full health or is already asleep.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'rock-slide': {
        'id': 157,
        'name': 'Rock-Slide',
        'type': 'rock',
        'category': 'physical',
        'power': 75,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'hyper-fang': {
        'id': 158,
        'name': 'Hyper-Fang',
        'type': 'normal',
        'category': 'physical',
        'power': 80,
        'pp': 15,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 10,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sharpen': {
        'id': 159,
        'name': 'Sharpen',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Attack by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }]
        }
    },
    'conversion': {
        'id': 160,
        'name': 'Conversion',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': None,
        'priority': 0,
        'description': "User's type changes to the type of one of its moves, selected at random.  hidden power and weather ball are treated as normal.  Only moves with a different type are eligible, and curse is never eligible.  If the user has no suitable moves, this move will fail.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'tri-attack': {
        'id': 161,
        'name': 'Tri-Attack',
        'type': 'normal',
        'category': 'special',
        'power': 80,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn, freeze, or paralyze the target.  One of these effects is selected at random; they do not each have independent chances to occur.',
        'meta': {
            'ailment': {
                'name': 'unknown',
                'chance': 20
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'super-fang': {
        'id': 162,
        'name': 'Super-Fang',
        'type': 'normal',
        'category': 'physical',
        'power': None,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': "Inflicts typeless damage equal to half the target's remaining HP.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'slash': {
        'id': 163,
        'name': 'Slash',
        'type': 'normal',
        'category': 'physical',
        'power': 70,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'substitute': {
        'id': 164,
        'name': 'Substitute',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "Transfers 1/4 the user's max HP into a doll that absorbs damage and causes most negative move effects to fail.  If the user leaves the field, the doll will vanish.  If the user cannot pay the HP cost, this move will fail.\n\nThe doll takes damage as normal, using the user's stats and types, and will break when its HP reaches zero.  Self-inflicted damage from confusion or recoil is not absorbed.  Healing effects from opponents ignore the doll and heal the user as normal.  Moves that work based on the user's HP still do so; the doll's HP does not influence any move.\n\nThe doll will block major status effects, confusion, and flinching.  The effects of smelling salts and wake up slap do not trigger against a doll, even if the Pokémon behind the doll has the appropriate major status effect.  Multi-turn trapping moves like wrap will hit the doll for their regular damage, but the multi-turn trapping and damage effects will not activate.\n\nMoves blocked or damage absorbed by the doll do not count as hitting the user or inflicting damage for any effects that respond to such, e.g., avalanche, counter, or a rowap berry.  magic coat still works as normal, even against moves the doll would block.  Opposing Pokémon that damage the doll with a leech move like absorb are healed as normal.\n\nIt will also block acupressure, block, the curse effect of curse, dream eater, embargo, flatter, gastro acid, grudge, heal block, leech seed, lock on, mean look, mimic, mind reader, nightmare, pain split, psycho shift, spider web, sketch, swagger, switcheroo, trick, worry seed, and yawn.  A Pokémon affected by yawn before summoning the doll will still fall to sleep.\n\nThe doll blocks intimidate, but all other abilities act as though the doll did not exist.  If the user has an ability that absorbs moves of a certain type for HP (such as volt absorb absorbing thunder wave), such moves will not be blocked.\n\nlife orb and berries that cause confusion still work as normal, but their respective HP loss and confusion are absorbed/blocked by the doll.\n\nThe user is still vulnerable to damage inflicted when entering or leaving the field, such as by pursuit or spikes; however, the doll will block the poison effect of toxic spikes.\n\nThe doll is passed on by baton pass.  It keeps its existing HP, but uses the replacement Pokémon's stats and types for damage calculation.\n\nAll other effects work as normal.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'struggle': {
        'id': 165,
        'name': 'Struggle',
        'type': 'normal',
        'category': 'physical',
        'power': 50,
        'pp': 1,
        'accuracy': None,
        'priority': 0,
        'description': "Inflicts typeless regular damage.  User takes 1/4 its max HP in recoil.  Ignores accuracy and evasion modifiers.\n\nThis move is used automatically when a Pokémon cannot use any other move legally, e.g., due to having no PP remaining or being under the effect of both encore and torment at the same time.\n\nThis move's recoil is not treated as recoil for the purposes of anything that affects recoil, such as the ability rock head.  It also is not prevented by magic guard.\n\nThis move cannot be copied by mimic, mirror move, or sketch, nor selected by assist or metronome, nor forced by encore.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': -25,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sketch': {
        'id': 166,
        'name': 'Sketch',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 1,
        'accuracy': None,
        'priority': 0,
        'description': "Permanently replaces itself with the target's last used move.  If that move is chatter or struggle, this move will fail.\n\nThis move cannot be copied by mimic or mirror move, nor selected by assist or metronome, nor forced by encore.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'triple-kick': {
        'id': 167,
        'name': 'Triple-Kick',
        'type': 'fighting',
        'category': 'physical',
        'power': 10,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits three times in the same turn.  The second hit has double power, and the third hit has triple power.  Each hit has a separate accuracy check, and this move stops if a hit misses.\n\nskill link does not apply.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 3,
            'max_turns': None,
            'min_hits': 3,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'thief': {
        'id': 168,
        'name': 'Thief',
        'type': 'dark',
        'category': 'physical',
        'power': 60,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If the target is holding an item and the user is not, the user will permanently take the item.  Damage is still inflicted if an item cannot be taken.\n\nPokémon with sticky hold or multitype are immune to the item theft effect.\n\nThe target cannot recover its item with recycle.\n\nThis move cannot be selected by assist or metronome.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'spider-web': {
        'id': 169,
        'name': 'Spider-Web',
        'type': 'bug',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'The target cannot switch out normally.  Ignores accuracy and evasion modifiers.  This effect ends when the user leaves the field.\n\nThe target may still escape by using baton pass, u turn, or a shed shell.\n\nBoth the user and the target pass on this effect with baton pass.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'mind-reader': {
        'id': 170,
        'name': 'Mind-Reader',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': 'If the user targets the same target again before the end of the next turn, the move it uses is guaranteed to hit.  This move itself also ignores accuracy and evasion modifiers.\n\nOne-hit KO moves are also guaranteed to hit, as long as the user is equal or higher level than the target.  This effect also allows the user to hit Pokémon that are off the field due to moves such as dig or fly.\n\nIf the target uses detect or protect while under the effect of this move, the user is not guaranteed to hit, but has a (100 - accuracy)% chance to break through the protection.\n\nThis effect is passed on by baton pass.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'nightmare': {
        'id': 171,
        'name': 'Nightmare',
        'type': 'ghost',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Only works on sleeping Pokémon.  Gives the target a nightmare, damaging it for 1/4 its max HP every turn.  If the target wakes up or leaves the field, this effect ends.',
        'meta': {
            'ailment': {
                'name': 'nightmare',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'flame-wheel': {
        'id': 172,
        'name': 'Flame-Wheel',
        'type': 'fire',
        'category': 'physical',
        'power': 60,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target.  Frozen Pokémon may use this move, in which case they will thaw.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'snore': {
        'id': 173,
        'name': 'Snore',
        'type': 'normal',
        'category': 'special',
        'power': 50,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Only usable if the user is sleeping.  Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'curse': {
        'id': 174,
        'name': 'Curse',
        'type': 'ghost',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "If the user is a ghost: user pays half its max HP to place a curse on the target, damaging it for 1/4 its max HP every turn.\nOtherwise: Lowers the user's Speed by one stage, and raises its Attack and Defense by one stage each.\n\nThe curse effect is passed on by baton pass.\n\nThis move cannot be copied by mirror move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'flail': {
        'id': 175,
        'name': 'Flail',
        'type': 'normal',
        'category': 'physical',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power varies inversely with the user's proportional remaining HP.\n\n64 * current HP / max HP | Power\n-----------------------: | ----:\n 0– 1                    |  200\n 2– 5                    |  150\n 6–12                    |  100\n13–21                    |   80\n22–42                    |   40\n43–64                    |   20\n",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'conversion-2': {
        'id': 176,
        'name': 'Conversion-2',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': None,
        'priority': 0,
        'description': "Changes the user's type to a type either resistant or immune to the last damaging move that hit it.  The new type is selected at random and cannot be a type the user already is.  If there is no eligible new type, this move will fail.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'aeroblast': {
        'id': 177,
        'name': 'Aeroblast',
        'type': 'flying',
        'category': 'special',
        'power': 100,
        'pp': 5,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'cotton-spore': {
        'id': 178,
        'name': 'Cotton-Spore',
        'type': 'grass',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's Speed by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'reversal': {
        'id': 179,
        'name': 'Reversal',
        'type': 'fighting',
        'category': 'physical',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power varies inversely with the user's proportional remaining HP.\n\n64 * current HP / max HP | Power\n-----------------------: | ----:\n 0– 1                    |  200\n 2– 5                    |  150\n 6–12                    |  100\n13–21                    |   80\n22–42                    |   40\n43–64                    |   20\n",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'spite': {
        'id': 180,
        'name': 'Spite',
        'type': 'ghost',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the PP of the target's last used move by 4.  If the target hasn't used a move since entering the field, if it tried to use a move this turn and failed, or if its last used move has 0 PP remaining, this move will fail.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'powder-snow': {
        'id': 181,
        'name': 'Powder-Snow',
        'type': 'ice',
        'category': 'special',
        'power': 40,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to freeze the target.',
        'meta': {
            'ailment': {
                'name': 'freeze',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'protect': {
        'id': 182,
        'name': 'Protect',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 4,
        'description': "No moves will hit the user for the remainder of this turn.  If the user is last to act this turn, this move will fail.\n\nIf the user successfully used detect, endure, protect, quick guard, or wide guard on the last turn, this move has a 50% chance to fail.\n\nlock on, mind reader, and no guard provide a (100 – accuracy)% chance for moves to break through this move.  This does not apply to one-hit KO moves (fissure, guillotine, horn drill, and sheer cold); those are always blocked by this move.\n\nthunder during rain dance and blizzard during hail have a 30% chance to break through this move.\n\nThe following effects are not prevented by this move:\n\n* acupressure from an ally\n* curse's curse effect\n* Delayed damage from doom desire and future sight; however, these moves will be prevented if they are used this turn\n* feint, which will also end this move's protection after it hits\n* imprison\n* perish song\n* shadow force\n* Moves that merely copy the user, such as transform or psych up\n\nThis move cannot be selected by assist or metronome.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'mach-punch': {
        'id': 183,
        'name': 'Mach-Punch',
        'type': 'fighting',
        'category': 'physical',
        'power': 40,
        'pp': 30,
        'accuracy': 100,
        'priority': 1,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'scary-face': {
        'id': 184,
        'name': 'Scary-Face',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's Speed by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'feint-attack': {
        'id': 185,
        'name': 'Feint-Attack',
        'type': 'dark',
        'category': 'physical',
        'power': 60,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Inflicts regular damage.  Ignores accuracy and evasion modifiers.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sweet-kiss': {
        'id': 186,
        'name': 'Sweet-Kiss',
        'type': 'fairy',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 75,
        'priority': 0,
        'description': 'Confuses the target.',
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'belly-drum': {
        'id': 187,
        'name': 'Belly-Drum',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'User pays half its max HP to raise its Attack to +6 stages.  If the user cannot pay the HP cost, this move will fail.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sludge-bomb': {
        'id': 188,
        'name': 'Sludge-Bomb',
        'type': 'poison',
        'category': 'special',
        'power': 90,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to poison the target.',
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'mud-slap': {
        'id': 189,
        'name': 'Mud-Slap',
        'type': 'ground',
        'category': 'special',
        'power': 20,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's accuracy by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'accuracy',
                    'url': 'https://pokeapi.co/api/v2/stat/7/'
                }
            }]
        }
    },
    'octazooka': {
        'id': 190,
        'name': 'Octazooka',
        'type': 'water',
        'category': 'special',
        'power': 65,
        'pp': 10,
        'accuracy': 85,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's accuracy by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 50,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'accuracy',
                    'url': 'https://pokeapi.co/api/v2/stat/7/'
                }
            }]
        }
    },
    'spikes': {
        'id': 191,
        'name': 'Spikes',
        'type': 'ground',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Scatters spikes around the opposing field, which damage opposing Pokémon that enter the field for 1/8 of their max HP.  Pokémon immune to ground moves are immune to this damage, except during gravity.  Up to three layers of spikes may be laid down, adding 1/16 to the damage done: two layers of spikes damage for 3/16 max HP, and three layers damage for 1/4 max HP.\n\nwonder guard does not block damage from this effect.\n\nrapid spin removes this effect from its user's side of the field.  defog removes this effect from its target's side of the field.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'zap-cannon': {
        'id': 192,
        'name': 'Zap-Cannon',
        'type': 'electric',
        'category': 'special',
        'power': 120,
        'pp': 5,
        'accuracy': 50,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 100
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'foresight': {
        'id': 193,
        'name': 'Foresight',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': None,
        'priority': 0,
        'description': "Resets the target's evasion to normal and prevents any further boosting until the target leaves the field.  A ghost under this effect takes normal damage from normal and fighting moves.  This move itself ignores accuracy and evasion modifiers.",
        'meta': {
            'ailment': {
                'name': 'no-type-immunity',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'destiny-bond': {
        'id': 194,
        'name': 'Destiny-Bond',
        'type': 'ghost',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': 'If the user faints before its next move, the Pokémon that fainted it will automatically faint.  End-of-turn damage is ignored.\n\nThis move cannot be selected by assist or metronome.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'perish-song': {
        'id': 195,
        'name': 'Perish-Song',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': "Every Pokémon is given a counter that starts at 3 and decreases by 1 at the end of every turn, including this one.  When a Pokémon's counter reaches zero, that Pokémon faints.  A Pokémon that leaves the field will lose its counter; its replacement does not inherit the effect, and other Pokémon's counters remain.\n\nThis effect is passed on by baton pass.\n\nThis move cannot be copied by mirror move.",
        'meta': {
            'ailment': {
                'name': 'perish-song',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 4,
            'min_hits': None,
            'min_turns': 4,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'icy-wind': {
        'id': 196,
        'name': 'Icy-Wind',
        'type': 'ice',
        'category': 'special',
        'power': 55,
        'pp': 15,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Speed by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'detect': {
        'id': 197,
        'name': 'Detect',
        'type': 'fighting',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 4,
        'description': "No moves will hit the user for the remainder of this turn.  If the user is last to act this turn, this move will fail.\n\nIf the user successfully used detect, endure, protect, quick guard, or wide guard on the last turn, this move has a 50% chance to fail.\n\nlock on, mind reader, and no guard provide a (100 – accuracy)% chance for moves to break through this move.  This does not apply to one-hit KO moves (fissure, guillotine, horn drill, and sheer cold); those are always blocked by this move.\n\nthunder during rain dance and blizzard during hail have a 30% chance to break through this move.\n\nThe following effects are not prevented by this move:\n\n* acupressure from an ally\n* curse's curse effect\n* Delayed damage from doom desire and future sight; however, these moves will be prevented if they are used this turn\n* feint, which will also end this move's protection after it hits\n* imprison\n* perish song\n* shadow force\n* Moves that merely copy the user, such as transform or psych up\n\nThis move cannot be selected by assist or metronome.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'bone-rush': {
        'id': 198,
        'name': 'Bone-Rush',
        'type': 'ground',
        'category': 'physical',
        'power': 25,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits 2–5 times in one turn.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 5,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'lock-on': {
        'id': 199,
        'name': 'Lock-On',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': 'If the user targets the same target again before the end of the next turn, the move it uses is guaranteed to hit.  This move itself also ignores accuracy and evasion modifiers.\n\nOne-hit KO moves are also guaranteed to hit, as long as the user is equal or higher level than the target.  This effect also allows the user to hit Pokémon that are off the field due to moves such as dig or fly.\n\nIf the target uses detect or protect while under the effect of this move, the user is not guaranteed to hit, but has a (100 - accuracy)% chance to break through the protection.\n\nThis effect is passed on by baton pass.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'outrage': {
        'id': 200,
        'name': 'Outrage',
        'type': 'dragon',
        'category': 'physical',
        'power': 120,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User is forced to attack with this move for 2–3 turns,selected at random.  After the last hit, the user becomes confused.\n\nsafeguard does not protect against the confusion from this move.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sandstorm': {
        'id': 201,
        'name': 'Sandstorm',
        'type': 'rock',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "Changes the weather to a sandstorm for five turns.  Pokémon that are not ground, rock, or steel take 1/16 their max HP at the end of every turn.  Every rock Pokémon's original Special Defense is raised by 50% for the duration of this effect.\n\nsolar beam's power is halved.\n\nmoonlight, morning sun, and synthesis only heal 1/4 the user's max HP.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'giga-drain': {
        'id': 202,
        'name': 'Giga-Drain',
        'type': 'grass',
        'category': 'special',
        'power': 75,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Drains half the damage inflicted to heal the user.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 50,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'endure': {
        'id': 203,
        'name': 'Endure',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 4,
        'description': "The user's HP cannot be lowered below 1 by any means for the remainder of this turn.\n\nIf the user successfully used detect, endure, protect, quick guard, or wide guard on the last turn, this move has a 50% chance to fail.\n\nThis move cannot be selected by assist or metronome.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'charm': {
        'id': 204,
        'name': 'Charm',
        'type': 'fairy',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's Attack by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }]
        }
    },
    'rollout': {
        'id': 205,
        'name': 'Rollout',
        'type': 'rock',
        'category': 'physical',
        'power': 30,
        'pp': 20,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  User is forced to use this move for five turns.  Power doubles every time this move is used in succession to a maximum of 16x, and resets to normal after the lock-in ends.  If this move misses or becomes unusable, the lock-in ends.\n\nIf the user has used defense curl since entering the field, this move has double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'false-swipe': {
        'id': 206,
        'name': 'False-Swipe',
        'type': 'normal',
        'category': 'physical',
        'power': 40,
        'pp': 40,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Will not reduce the target's HP below 1.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'swagger': {
        'id': 207,
        'name': 'Swagger',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 85,
        'priority': 0,
        'description': "Raises the target's Attack by two stages, then confuses it.  If the target's Attack cannot be raised by two stages, the confusion is not applied.",
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 2,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }]
        }
    },
    'milk-drink': {
        'id': 208,
        'name': 'Milk-Drink',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'Heals the user for half its max HP.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 50,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'spark': {
        'id': 209,
        'name': 'Spark',
        'type': 'electric',
        'category': 'physical',
        'power': 65,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fury-cutter': {
        'id': 210,
        'name': 'Fury-Cutter',
        'type': 'bug',
        'category': 'physical',
        'power': 40,
        'pp': 20,
        'accuracy': 95,
        'priority': 0,
        'description': 'Inflicts regular damage.  Power doubles after every time this move is used, whether consecutively or not, maxing out at 16x.  If this move misses or the user leaves the field, power resets.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'steel-wing': {
        'id': 211,
        'name': 'Steel-Wing',
        'type': 'steel',
        'category': 'physical',
        'power': 70,
        'pp': 25,
        'accuracy': 90,
        'priority': 0,
        'description': "Inflicts regular damage. Has a $effect_chance% chance to raise the user's Defense one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'mean-look': {
        'id': 212,
        'name': 'Mean-Look',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': 'The target cannot switch out normally.  Ignores accuracy and evasion modifiers.  This effect ends when the user leaves the field.\n\nThe target may still escape by using baton pass, u turn, or a shed shell.\n\nBoth the user and the target pass on this effect with baton pass.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'attract': {
        'id': 213,
        'name': 'Attract',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Causes the target to fall in love with the user, giving it a 50% chance to do nothing each turn.  If the user and target are the same gender, or either is genderless, this move will fail.  If either Pokémon leaves the field, this effect ends.',
        'meta': {
            'ailment': {
                'name': 'infatuation',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sleep-talk': {
        'id': 214,
        'name': 'Sleep-Talk',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "Only usable if the user is sleeping.  Randomly selects and uses one of the user's other three moves.  Use of the selected move requires and costs 0 PP.\n\nThis move will not select assist, bide, bounce, chatter, copycat, dig, dive, fly, focus punch, me first, metronome, mirror move, shadow force, skull bash, sky attack, sky drop, sleep talk, solar beam, razor wind, or uproar.\n\nIf the selected move requires a recharge turn—i.e., one of blast burn, frenzy plant, giga impact, hydro cannon, hyper beam, roar of time, or rock wrecker—and the user is still sleeping next turn, then it's forced to use this move again and pay another PP for the recharge turn.\n\nThis move cannot be copied by mirror move, nor selected by assist, metronome, or sleep talk.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'heal-bell': {
        'id': 215,
        'name': 'Heal-Bell',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': "Removes major status effects and confusion from every Pokémon in the user's party.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'return': {
        'id': 216,
        'name': 'Return',
        'type': 'normal',
        'category': 'physical',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Power increases with happiness, given by `happiness * 2 / 5`, to a maximum of 102.  Power bottoms out at 1.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'present': {
        'id': 217,
        'name': 'Present',
        'type': 'normal',
        'category': 'physical',
        'power': None,
        'pp': 15,
        'accuracy': 90,
        'priority': 0,
        'description': 'Randomly uses one of the following effects.\n\nEffect                                             | Chance\n-------------------------------------------------- | -----:\nInflicts regular damage with 40 power  |    40%\nInflicts regular damage with 80 power  |    30%\nInflicts regular damage with 120 power |    10%\nHeals the target for 1/4 its max HP    |    20%\n\nOn average, this move inflicts regular damage with 52 power and heals the target for 1/20 its max HP.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'frustration': {
        'id': 218,
        'name': 'Frustration',
        'type': 'normal',
        'category': 'physical',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Power increases inversely with happiness, given by `(255 - happiness) * 2 / 5`, to a maximum of 102.  Power bottoms out at 1.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'safeguard': {
        'id': 219,
        'name': 'Safeguard',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 25,
        'accuracy': None,
        'priority': 0,
        'description': "Protects Pokémon on the user's side of the field from major status effects and confusion for five turns.  Does not cancel existing ailments.  This effect remains even if the user leaves the field.\n\nIf yawn is used while this move is in effect, it will immediately fail.\n\ndefog used by an opponent will end this effect.\n\nThis effect does not prevent the confusion caused by outrage, petal dance, or thrash.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'pain-split': {
        'id': 220,
        'name': 'Pain-Split',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Changes the user's and target's remaining HP to the average of their current remaining HP.  Ignores accuracy and evasion modifiers.  This effect does not count as inflicting damage for other moves and effects that respond to damage taken.\n\nThis effect fails against a substitute.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sacred-fire': {
        'id': 221,
        'name': 'Sacred-Fire',
        'type': 'fire',
        'category': 'physical',
        'power': 100,
        'pp': 5,
        'accuracy': 95,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target.  Frozen Pokémon may use this move, in which case they will thaw.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 50
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'magnitude': {
        'id': 222,
        'name': 'Magnitude',
        'type': 'ground',
        'category': 'physical',
        'power': None,
        'pp': 30,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Power is selected at random between 10 and 150, with an average of 71:\n\nMagnitude | Power | Chance\n--------: | ----: | -----:\n        4 |    10 |     5%\n        5 |    30 |    10%\n        6 |    50 |    20%\n        7 |    70 |    30%\n        8 |    90 |    20%\n        9 |   110 |    10%\n       10 |   150 |     5%\n\nThis move has double power against Pokémon currently underground due to dig.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'dynamic-punch': {
        'id': 223,
        'name': 'Dynamic-Punch',
        'type': 'fighting',
        'category': 'physical',
        'power': 100,
        'pp': 5,
        'accuracy': 50,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to confuse the target.',
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 100
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'megahorn': {
        'id': 224,
        'name': 'Megahorn',
        'type': 'bug',
        'category': 'physical',
        'power': 120,
        'pp': 10,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'dragon-breath': {
        'id': 225,
        'name': 'Dragon-Breath',
        'type': 'dragon',
        'category': 'special',
        'power': 60,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'baton-pass': {
        'id': 226,
        'name': 'Baton-Pass',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': None,
        'priority': 0,
        'description': "User switches out, and the trainer selects a replacement Pokémon from the party.  Stat changes, confusion, and persistent move effects are passed along to the replacement Pokémon.\n\nThe following move effects are passed:\n\n* aqua ring\n* both the user's and target's effect of block, mean look, and spider web\n* the curse effect of curse\n* embargo\n* focus energy or an activated lansat berry\n* gastro acid\n* ingrain\n* being sapped by leech seed\n* being targeted by lock on or mind reader\n* magnet rise\n* perish song's counter\n* power trick\n* substitute; the doll's HP is unchanged\n\nThe replacement Pokémon does not trigger effects that respond to Pokémon switching in.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'encore': {
        'id': 227,
        'name': 'Encore',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "The next 4–8 times (selected at random) the target attempts to move, it is forced to repeat its last used move.  If the selected move allows the trainer to select a target, an opponent will be selected at random each turn.  If the target is prevented from using the selected move by some other effect, struggle will be used instead.  This effect ends if the selected move runs out of PP.\n\nIf the target hasn't used a move since entering the field, if it tried to use a move this turn and failed, if it does not know the selected move, or if the selected move has 0 PP remaining, this move will fail.  If the target's last used move was encore, mimic, mirror move, sketch, struggle, or transform, this move will fail.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'pursuit': {
        'id': 228,
        'name': 'Pursuit',
        'type': 'dark',
        'category': 'physical',
        'power': 40,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If the target attempts to switch out this turn before the user acts, this move hits the target before it leaves and has double power.\n\nThis effect can still hit a Pokémon that switches out when it has a substitute up or when an ally has used follow me.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'rapid-spin': {
        'id': 229,
        'name': 'Rapid-Spin',
        'type': 'normal',
        'category': 'physical',
        'power': 50,
        'pp': 40,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Removes leech seed from the user, frees the user from bind, clamp, fire spin, magma storm, sand tomb, whirlpool, and wrap, and clears spikes, stealth rock, and toxic spikes from the user's side of the field.  If this move misses or has no effect, its effect doesn't activate.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sweet-scent': {
        'id': 230,
        'name': 'Sweet-Scent',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's evasion by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'evasion',
                    'url': 'https://pokeapi.co/api/v2/stat/8/'
                }
            }]
        }
    },
    'iron-tail': {
        'id': 231,
        'name': 'Iron-Tail',
        'type': 'steel',
        'category': 'physical',
        'power': 100,
        'pp': 15,
        'accuracy': 75,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 30,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'metal-claw': {
        'id': 232,
        'name': 'Metal-Claw',
        'type': 'steel',
        'category': 'physical',
        'power': 50,
        'pp': 35,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage. Has a $effect_chance% chance to raise the user's Attack one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }]
        }
    },
    'vital-throw': {
        'id': 233,
        'name': 'Vital-Throw',
        'type': 'fighting',
        'category': 'physical',
        'power': 70,
        'pp': 10,
        'accuracy': None,
        'priority': -1,
        'description': 'Inflicts regular damage.  Ignores accuracy and evasion modifiers.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'morning-sun': {
        'id': 234,
        'name': 'Morning-Sun',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': 'Heals the user for half its max HP.\n\nDuring sunny day, the healing is increased to 2/3 max HP.\n\nDuring hail, rain dance, or sandstorm, the healing is decreased to 1/4 max HP.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 50,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'synthesis': {
        'id': 235,
        'name': 'Synthesis',
        'type': 'grass',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': 'Heals the user for half its max HP.\n\nDuring sunny day, the healing is increased to 2/3 max HP.\n\nDuring hail, rain dance, or sandstorm, the healing is decreased to 1/4 max HP.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 50,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'moonlight': {
        'id': 236,
        'name': 'Moonlight',
        'type': 'fairy',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': 'Heals the user for half its max HP.\n\nDuring sunny day, the healing is increased to 2/3 max HP.\n\nDuring hail, rain dance, or sandstorm, the healing is decreased to 1/4 max HP.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 50,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'hidden-power': {
        'id': 237,
        'name': 'Hidden-Power',
        'type': 'normal',
        'category': 'special',
        'power': 60,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power and type are determined by the user's IVs.\n\nPower is given by `x * 40 / 63 + 30`.  `x` is obtained by arranging bit 1 from the IV for each of Special Defense, Special Attack, Speed, Defense, Attack, and HP in that order.  (Bit 1 is 1 if the IV is of the form `4n + 2` or `4n + 3`.  `x` is then 64 * Special Defense IV bit 1, plus 32 * Special Attack IV bit 1, etc.)\n\nPower is always between 30 and 70, inclusive.  Average power is 49.5.\n\nType is given by `y * 15 / 63`, where `y` is similar to `x` above, except constructed from bit 0.  (Bit 0 is 1 if the IV is odd.)  The result is looked up in the following table.\n\nValue | Type\n----: | --------\n    0 | fighting\n    1 | flying\n    2 | poison\n    3 | ground\n    4 | rock\n    5 | bug\n    6 | ghost\n    7 | steel\n    8 | fire\n    9 | water\n   10 | grass\n   11 | electric\n   12 | psychic\n   13 | ice\n   14 | dragon\n   15 | dark\n\nThis move thus cannot be normal.  Most other types have an equal 1/16 chance to be selected, given random IVs.  However, due to the flooring used here, bug, fighting, and grass appear 5/64 of the time, and dark only 1/64 of the time.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'cross-chop': {
        'id': 238,
        'name': 'Cross-Chop',
        'type': 'fighting',
        'category': 'physical',
        'power': 100,
        'pp': 5,
        'accuracy': 80,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'twister': {
        'id': 239,
        'name': 'Twister',
        'type': 'dragon',
        'category': 'special',
        'power': 40,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make each target flinch.\n\nIf the target is under the effect of bounce, fly, or sky drop, this move will hit with double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 20,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'rain-dance': {
        'id': 240,
        'name': 'Rain-Dance',
        'type': 'water',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': "Changes the weather to rain for five turns, during which water moves inflict 50% extra damage, and fire moves inflict half damage.\n\nIf the user is holding damp rock, this effect lasts for eight turns.\n\nthunder has 100% accuracy.  If the target has used detect or protect, thunder has a (100 - accuracy)% chance to break through the protection.\n\nsolar beam has half power.\n\nmoonlight, morning sun, and synthesis heal only 1/4 of the user's max HP.\n\nPokémon with swift swim have doubled original Speed.\n\nPokémon with forecast become water.\n\nPokémon with dry skin heal 1/8 max HP, Pokémon with hydration are cured of major status effects, and Pokémon with rain dish heal 1/16 max HP at the end of each turn.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sunny-day': {
        'id': 241,
        'name': 'Sunny-Day',
        'type': 'fire',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': "Changes the weather to sunshine for five turns, during which fire moves inflict 50% extra damage, and water moves inflict half damage.\n\nIf the user is holding heat rock, this effect lasts for eight turns.\n\nPokémon cannot become frozen.\n\nthunder has 50% accuracy.\n\nsolar beam skips its charge turn.\n\nmoonlight, morning sun, and synthesis heal 2/3 of the user's max HP.\n\nPokémon with chlorophyll have doubled original Speed.\n\nPokémon with forecast become fire.\n\nPokémon with leaf guard are not affected by major status effects.\n\nPokémon with flower gift change form; every Pokémon on their side of the field have their original Attack and Special Attack increased by 50%.\n\nPokémon with dry skin lose 1/8 max HP at the end of each turn.\n\nPokémon with solar power have their original Special Attack raised by 50% but lose 1/8 their max HP at the end of each turn.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'crunch': {
        'id': 242,
        'name': 'Crunch',
        'type': 'dark',
        'category': 'physical',
        'power': 80,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 20,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'mirror-coat': {
        'id': 243,
        'name': 'Mirror-Coat',
        'type': 'psychic',
        'category': 'special',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': -5,
        'description': 'Targets the last opposing Pokémon to hit the user with a special move this turn.  Inflicts twice the damage that move did to the user.  If there is no eligible target, this move will fail.  Type immunity applies, but other type effects are ignored.\n\nThis move cannot be copied by mirror move, nor selected by assist or metronome.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'psych-up': {
        'id': 244,
        'name': 'Psych-Up',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "Discards the user's stat changes and copies the target's.\n\nThis move cannot be copied by mirror move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'extreme-speed': {
        'id': 245,
        'name': 'Extreme-Speed',
        'type': 'normal',
        'category': 'physical',
        'power': 80,
        'pp': 5,
        'accuracy': 100,
        'priority': 2,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'ancient-power': {
        'id': 246,
        'name': 'Ancient-Power',
        'type': 'rock',
        'category': 'special',
        'power': 60,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage. Has a $effect_chance% chance to raise all of the user's stats one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'hp',
                    'url': 'https://pokeapi.co/api/v2/stat/1/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'shadow-ball': {
        'id': 247,
        'name': 'Shadow-Ball',
        'type': 'ghost',
        'category': 'special',
        'power': 80,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Special Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 20,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'future-sight': {
        'id': 248,
        'name': 'Future-Sight',
        'type': 'psychic',
        'category': 'special',
        'power': 120,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts typeless regular damage at the end of the third turn, starting with this one.  This move cannot score a critical hit.  If the target switches out, its replacement will be hit instead.  Damage is calculated at the time this move is used; stat changes and switching out during the delay won't change the damage inflicted.  No move with this effect can be used against the same target again until after the end of the third turn.\n\nThis effect breaks through wonder guard.\n\nIf the target is protected by protect or detect on the turn this move is used, this move will fail.  However, the damage on the third turn will break through protection.\n\nThe damage is applied at the end of the turn, so it ignores endure and focus sash.\n\nThis move cannot be copied by mirror move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'rock-smash': {
        'id': 249,
        'name': 'Rock-Smash',
        'type': 'fighting',
        'category': 'physical',
        'power': 40,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 50,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'whirlpool': {
        'id': 250,
        'name': 'Whirlpool',
        'type': 'water',
        'category': 'special',
        'power': 35,
        'pp': 15,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  For the next 2–5 turns, the target cannot leave the field and is damaged for 1/16 its max HP at the end of each turn.  The user continues to use other moves during this time.  If the user leaves the field, this effect ends.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.\n\nIf the target is in the first turn of dive, this move will hit with double power.',
        'meta': {
            'ailment': {
                'name': 'trap',
                'chance': 100
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 6,
            'min_hits': None,
            'min_turns': 5,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'beat-up': {
        'id': 251,
        'name': 'Beat-Up',
        'type': 'dark',
        'category': 'physical',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts typeless regular damage.  Every Pokémon in the user's party, excepting those that have fainted or have a major status effect, attacks the target.  Calculated stats are ignored; the base stats for the target and assorted attackers are used instead.  The random factor in the damage formula is not used.  dark Pokémon still get STAB.\n\nThis effect breaks through wonder guard.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 6,
            'max_turns': None,
            'min_hits': 6,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fake-out': {
        'id': 252,
        'name': 'Fake-Out',
        'type': 'normal',
        'category': 'physical',
        'power': 40,
        'pp': 10,
        'accuracy': 100,
        'priority': 3,
        'description': "Inflicts regular damage.  Causes the target to flinch.  Can only be used on the user's first turn after entering the field.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 100,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'uproar': {
        'id': 253,
        'name': 'Uproar',
        'type': 'normal',
        'category': 'special',
        'power': 90,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User is forced to use this move for 2–5 turns, selected at random.  All Pokémon on the field wake up, and none can fall to sleep until the lock-in ends.\n\nPokémon cannot use rest during this effect.\n\nThis move cannot be selected by sleep talk.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'stockpile': {
        'id': 254,
        'name': 'Stockpile',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Defense and Special Defense by one stage each.  Stores energy for use with spit up and swallow.  Up to three levels of energy can be stored, and all are lost if the user leaves the field.  Energy is still stored even if the stat boosts cannot be applied.\n\nIf the user uses baton pass, the stat boosts are passed as normal, but the stored energy is not.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'spit-up': {
        'id': 255,
        'name': 'Spit-Up',
        'type': 'normal',
        'category': 'special',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power is equal to 100 times the amount of energy stored by stockpile.  Ignores the random factor in the damage formula.  Stored energy is consumed, and the user's Defense and Special Defense are reset to what they would be if stockpile had not been used.  If the user has no energy stored, this move will fail.\n\nThis move cannot be copied by mirror move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'swallow': {
        'id': 256,
        'name': 'Swallow',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "Heals the user depending on the amount of energy stored by stockpile: 1/4 its max HP after one use, 1/2 its max HP after two uses, or fully after three uses.  Stored energy is consumed, and the user's Defense and Special Defense are reset to what they would be if stockpile had not been used.  If the user has no energy stored, this move will fail.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 25,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'heat-wave': {
        'id': 257,
        'name': 'Heat-Wave',
        'type': 'fire',
        'category': 'special',
        'power': 95,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'hail': {
        'id': 258,
        'name': 'Hail',
        'type': 'ice',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "Changes the weather to hail for five turns, during which non-ice Pokémon are damaged for 1/16 their max HP at the end of every turn.\n\nIf the user is holding icy rock, this effect lasts for eight turns.\n\nblizzard has 100% accuracy.  If the target has used detect or protect, blizzard has a (100 - accuracy)% chance to break through the protection.\n\nmoonlight, morning sun, and synthesis heal only 1/4 of the user's max HP.\n\nPokémon with snow cloak are exempt from this effect's damage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'torment': {
        'id': 259,
        'name': 'Torment',
        'type': 'dark',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Prevents the target from attempting to use the same move twice in a row.  When the target leaves the field, this effect ends.\n\nIf the target is forced to attempt a repeated move due to choice band, choice scarf, choice specs, disable, encore, taunt, only having PP remaining for one move, or any other effect, the target will use struggle instead.  The target is then free to use the forced move next turn, as it didn't use that move this turn.",
        'meta': {
            'ailment': {
                'name': 'torment',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'flatter': {
        'id': 260,
        'name': 'Flatter',
        'type': 'dark',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Raises the target's Special Attack by one stage, then confuses it.",
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'will-o-wisp': {
        'id': 261,
        'name': 'Will-O-Wisp',
        'type': 'fire',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 85,
        'priority': 0,
        'description': 'Burns the target.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'memento': {
        'id': 262,
        'name': 'Memento',
        'type': 'dark',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's Attack and Special Attack by two stages.  User faints.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'facade': {
        'id': 263,
        'name': 'Facade',
        'type': 'normal',
        'category': 'physical',
        'power': 70,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If the user is burned, paralyzed, or poisoned, this move has double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'focus-punch': {
        'id': 264,
        'name': 'Focus-Punch',
        'type': 'fighting',
        'category': 'physical',
        'power': 150,
        'pp': 20,
        'accuracy': 100,
        'priority': -3,
        'description': 'Inflicts regular damage.  If the user takes damage this turn before hitting, this move will fail.\n\nThis move cannot be copied by mirror move, nor selected by assist, metronome, or sleep talk.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'smelling-salts': {
        'id': 265,
        'name': 'Smelling-Salts',
        'type': 'normal',
        'category': 'physical',
        'power': 70,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If the target is paralyzed, this move has double power, and the target is cured of its paralysis.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'follow-me': {
        'id': 266,
        'name': 'Follow-Me',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 2,
        'description': "Until the end of this turn, any moves that opposing Pokémon target solely at the user's ally will instead target the user.  If both Pokémon on the same side of the field use this move on the same turn, the Pokémon that uses it last will become the target.\n\nThis effect takes priority over lightning rod and storm drain.\n\nIf the user's ally switches out, opposing Pokémon may still hit it with pursuit.\n\nThis move cannot be selected by assist or metronome.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'nature-power': {
        'id': 267,
        'name': 'Nature-Power',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Uses another move chosen according to the terrain.\n\nTerrain                   | Selected move\n------------------------- | ------------------\nBuilding                  | tri attack\nCave                      | rock slide\nDeep water                | hydro pump\nDesert                    | earthquake\nGrass                     | seed bomb\nMountain                  | rock slide\nRoad                      | earthquake\nShallow water             | hydro pump\nSnow                      | blizzard\nTall grass                | seed bomb\nelectric terrain | thunderbolt\ngrassy terrain   | energy ball\nmisty terrain    | moonblast\n\nIn Pokémon Battle Revolution:\n\nTerrain        | Selected move\n-------------- | ------------------\nCourtyard      | tri attack\nCrystal        | rock slide\nGateway        | hydro pump\nMagma          | rock slide\nMain Street    | tri attack\nNeon           | tri attack\nStargazer      | rock slide\nSunny Park     | seed bomb\nSunset         | earthquake\nWaterfall      | seed bomb\n\nThis move cannot be copied by mirror move.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'charge': {
        'id': 268,
        'name': 'Charge',
        'type': 'electric',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Special Defense by one stage.  If the user uses an electric move next turn, its power will be doubled.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'taunt': {
        'id': 269,
        'name': 'Taunt',
        'type': 'dark',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Target is forced to only use damaging moves for the next 3–5 turns, selected at random.  Moves that select other moves not known in advance do not count as damaging.\n\nassist, copycat, me first, metronome, mirror move, and sleep talk do not directly inflict damage and thus may not be used.\n\nbide, counter, endeavor, metal burst, and mirror coat are allowed.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'helping-hand': {
        'id': 270,
        'name': 'Helping-Hand',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 5,
        'description': "Boosts the power of the target's moves by 50% until the end of this turn.\n\nThis move cannot be copied by mirror move, nor selected by assist or metronome.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'trick': {
        'id': 271,
        'name': 'Trick',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "User and target permanently swap held items.  Works even if one of the Pokémon isn't holding anything.  If either Pokémon is holding mail, this move will fail.\n\nIf either Pokémon has multitype or sticky hold, this move will fail.\n\nIf this move results in a Pokémon obtaining choice band, choice scarf, or choice specs, and that Pokémon was the latter of the pair to move this turn, then the move it used this turn becomes its chosen forced move.  This applies even if both Pokémon had a choice item before this move was used.  If the first of the two Pokémon gains a choice item, it may select whatever choice move it wishes next turn.\n\nNeither the user nor the target can recover its item with recycle.\n\nThis move cannot be selected by assist or metronome.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'role-play': {
        'id': 272,
        'name': 'Role-Play',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "User's ability is replaced with the target's until the user leaves the field.  Ignores accuracy and evasion modifiers.\n\nIf the target has flower gift, forecast, illusion, imposter, multitype, stance change, trace, wonder guard, or zen mode, this move will fail.\n\nThis move cannot be copied by mirror move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'wish': {
        'id': 273,
        'name': 'Wish',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "At the end of the next turn, user will be healed for half its max HP.  If the user is switched out, its replacement will be healed instead for half of the user's max HP.  If the user faints or is forcefully switched by roar or whirlwind, this effect will not activate.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'assist': {
        'id': 274,
        'name': 'Assist',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Uses a move from another Pokémon in the user's party, both selected at random.  Moves from fainted Pokémon can be used.  If there are no eligible Pokémon or moves, this move will fail.\n\nThis move will not select assist, chatter, circle throw, copycat, counter, covet, destiny bond, detect, dig, dive, dragon tail, endure, feint, fly focus punch, follow me, helping hand, me first, metronome, mimic, mirror coat, mirror move, phantom force protect, quick guard, roar shadow force, sketch, sleep talk, snatch, struggle, switcheroo, thief, trick, whirlwind, or wide guard.\n\nThis move cannot be copied by mirror move, nor selected by metronome or sleep talk.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'ingrain': {
        'id': 275,
        'name': 'Ingrain',
        'type': 'grass',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Prevents the user from switching out.  User regains 1/16 of its max HP at the end of every turn.  If the user was immune to ground attacks, it will now take normal damage from them.\n\nroar and whirlwind will not affect the user.  The user cannot use magnet rise.\n\nThe user may still use u turn to leave the field.\n\nThis effect can be passed with baton pass.',
        'meta': {
            'ailment': {
                'name': 'ingrain',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'superpower': {
        'id': 276,
        'name': 'Superpower',
        'type': 'fighting',
        'category': 'physical',
        'power': 120,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage, then lowers the user's Attack and Defense by one stage each.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }, {
                'change': -1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'magic-coat': {
        'id': 277,
        'name': 'Magic-Coat',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 4,
        'description': 'The first non-damaging move targeting the user this turn that inflicts major status effects, stat changes, or trapping effects will be reflected at its user.\n\ndefog, memento, and teeter dance are not reflected.\n\nattract, flatter, gastro acid, leech seed, swagger, worry seed, and yawn are reflected.\n\nThis move cannot be copied by mirror move.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'recycle': {
        'id': 278,
        'name': 'Recycle',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'User recovers the last item consumed by the user or a Pokémon in its position on the field.  The item must be used again before it can be recovered by this move again.  If the user is holding an item, this move fails.\n\nItems taken or given away by covet, knock off, switcheroo, thief, or trick may not be recovered.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'revenge': {
        'id': 279,
        'name': 'Revenge',
        'type': 'fighting',
        'category': 'physical',
        'power': 60,
        'pp': 10,
        'accuracy': 100,
        'priority': -4,
        'description': 'Inflicts regular damage.  If the target damaged the user this turn and was the last to do so, this move has double power.\n\npain split does not count as damaging the user.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'brick-break': {
        'id': 280,
        'name': 'Brick-Break',
        'type': 'fighting',
        'category': 'physical',
        'power': 75,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Destroys any light screen or reflect on the target's side of the field, then inflicts regular damage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'yawn': {
        'id': 281,
        'name': 'Yawn',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'Puts the target to sleep at the end of the next turn.  Ignores accuracy and evasion modifiers.  If the target leaves the field, this effect is canceled.  If the target has a status effect when this move is used, this move will fail.\n\nIf the target is protected by safeguard when this move is used, this move will fail.\n\ninsomnia and vital spirit prevent the sleep if the target has either at the end of the next turn, but will not cause this move to fail on use.',
        'meta': {
            'ailment': {
                'name': 'yawn',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 2,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'knock-off': {
        'id': 282,
        'name': 'Knock-Off',
        'type': 'dark',
        'category': 'physical',
        'power': 65,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Target loses its held item.\n\nNeither the user nor the target can recover its item with recycle.\n\nIf the target has multitype or sticky hold, it will take damage but not lose its item.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'endeavor': {
        'id': 283,
        'name': 'Endeavor',
        'type': 'normal',
        'category': 'physical',
        'power': None,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts exactly enough damage to lower the target's HP to equal the user's.  If the target's HP is not higher than the user's, this move has no effect.  Type immunity applies, but other type effects are ignored.  This effect counts as damage for moves that respond to damage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'eruption': {
        'id': 284,
        'name': 'Eruption',
        'type': 'fire',
        'category': 'special',
        'power': 150,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power increases with the user's remaining HP and is given by `150 * HP / max HP`, to a maximum of 150 when the user has full HP.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'skill-swap': {
        'id': 285,
        'name': 'Skill-Swap',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'User and target switch abilities.  Ignores accuracy and evasion modifiers.\n\nIf either Pokémon has multitype or wonder guard, this move will fail.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'imprison': {
        'id': 286,
        'name': 'Imprison',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "Prevents any Pokémon on the opposing side of the field from using any move the user knows until the user leaves the field.  This effect is live; if the user obtains new moves while on the field, these moves become restricted.  If no opposing Pokémon knows any of the user's moves when this move is used, this move will fail.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'refresh': {
        'id': 287,
        'name': 'Refresh',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Removes a burn, paralysis, or poison from the user.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'grudge': {
        'id': 288,
        'name': 'Grudge',
        'type': 'ghost',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': 'If the user faints before it next acts, the move that fainted it will have its PP dropped to 0.  End-of-turn damage does not trigger this effect.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'snatch': {
        'id': 289,
        'name': 'Snatch',
        'type': 'dark',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 4,
        'description': 'The next time a Pokémon uses a beneficial move on itself or itself and its ally this turn, the user of this move will steal the move and use it itself.  Moves which may be stolen by this move are identified by the "snatchable" flag.\n\nIf two Pokémon use this move on the same turn, the faster Pokémon will steal the first beneficial move, and the slower Pokémon will then steal it again—thus, only the slowest Pokémon using this move ultimately gains a stolen move\'s effect.\n\nIf the user steals psych up, it will target the Pokémon that used psych up.  If the user was the original target of psych up, and the Pokémon that originally used it\'s affected by pressure, it will only lose 1 PP.\n\nThis move cannot be copied by mirror move, nor selected by assist or metronome.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'secret-power': {
        'id': 290,
        'name': 'Secret-Power',
        'type': 'normal',
        'category': 'physical',
        'power': 70,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to inflict an effect chosen according to the terrain.\n\nTerrain        | Effect\n-------------- | -------------------------------------------------------------\nBuilding       | Paralyzes target\nCave           | Makes target flinch\nDeep water     | Lowers target's Attack by one stage\nDesert         | Lowers target's accuracy by one stage\nGrass          | Puts target to sleep\nMountain       | Makes target flinch\nRoad           | Lowers target's accuracy by one stage\nShallow water  | Lowers target's Attack by one stage\nSnow           | Freezes target\nTall grass     | Puts target to sleep\n\nIn Pokémon Battle Revolution:\n\nTerrain        | Effect\n-------------- | -------------------------------------------------------------\nCourtyard      | Paralyzes target\nCrystal        | Makes target flinch\nGateway        | Lowers target's Attack by one stage\nMagma          | Makes target flinch\nMain Street    | Paralyzes target\nNeon           | Paralyzes target\nStargazer      | Makes target flinch\nSunny Park     | Puts target to sleep\nSunset         | Lowers target's accuracy by one stage\nWaterfall      | Puts target to sleep\n",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'dive': {
        'id': 291,
        'name': 'Dive',
        'type': 'water',
        'category': 'physical',
        'power': 80,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User dives underwater for one turn, becoming immune to attack, and hits on the second turn.\n\nDuring the immune turn, surf, and whirlpool still hit the user normally, and their power is doubled if appropriate.\n\nThe user may be hit during its immune turn if under the effect of lock on, mind reader, or no guard.\n\nThis move cannot be selected by sleep talk.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'arm-thrust': {
        'id': 292,
        'name': 'Arm-Thrust',
        'type': 'fighting',
        'category': 'physical',
        'power': 15,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits 2–5 times in one turn.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 5,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'camouflage': {
        'id': 293,
        'name': 'Camouflage',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "User's type changes according to the terrain.\n\nTerrain        | New type\n-------------- | --------------\nBuilding       | normal\nCave           | rock\nDesert         | ground\nGrass          | grass\nMountain       | rock\nOcean          | water\nPond           | water\nRoad           | ground\nSnow           | ice\nTall grass     | grass\n\nIn Pokémon Battle Revolution:\n\nTerrain        | New type\n-------------- | --------------\nCourtyard      | normal\nCrystal        | rock\nGateway        | water\nMagma          | rock\nMain Street    | normal\nNeon           | normal\nStargazer      | rock\nSunny Park     | grass\nSunset         | ground\nWaterfall      | grass\n",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'tail-glow': {
        'id': 294,
        'name': 'Tail-Glow',
        'type': 'bug',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Special Attack by three stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 3,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'luster-purge': {
        'id': 295,
        'name': 'Luster-Purge',
        'type': 'psychic',
        'category': 'special',
        'power': 70,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Special Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 50,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'mist-ball': {
        'id': 296,
        'name': 'Mist-Ball',
        'type': 'psychic',
        'category': 'special',
        'power': 70,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Special Attack by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 50,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'feather-dance': {
        'id': 297,
        'name': 'Feather-Dance',
        'type': 'flying',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's Attack by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }]
        }
    },
    'teeter-dance': {
        'id': 298,
        'name': 'Teeter-Dance',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Confuses all targets.',
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'blaze-kick': {
        'id': 299,
        'name': 'Blaze-Kick',
        'type': 'fire',
        'category': 'physical',
        'power': 85,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move. Has a $effect_chance% chance to burn the target.",
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 10
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'mud-sport': {
        'id': 300,
        'name': 'Mud-Sport',
        'type': 'ground',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': 'electric moves inflict half damage, regardless of target.  If the user leaves the field, this effect ends.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'ice-ball': {
        'id': 301,
        'name': 'Ice-Ball',
        'type': 'ice',
        'category': 'physical',
        'power': 30,
        'pp': 20,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  User is forced to use this move for five turns.  Power doubles every time this move is used in succession to a maximum of 16x, and resets to normal after the lock-in ends.  If this move misses or becomes unusable, the lock-in ends.\n\nIf the user has used defense curl since entering the field, this move has double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'needle-arm': {
        'id': 302,
        'name': 'Needle-Arm',
        'type': 'grass',
        'category': 'physical',
        'power': 60,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'slack-off': {
        'id': 303,
        'name': 'Slack-Off',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'Heals the user for half its max HP.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 50,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'hyper-voice': {
        'id': 304,
        'name': 'Hyper-Voice',
        'type': 'normal',
        'category': 'special',
        'power': 90,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'poison-fang': {
        'id': 305,
        'name': 'Poison-Fang',
        'type': 'poison',
        'category': 'physical',
        'power': 50,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to badly poison the target.',
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 50
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 15,
            'min_hits': None,
            'min_turns': 15,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'crush-claw': {
        'id': 306,
        'name': 'Crush-Claw',
        'type': 'normal',
        'category': 'physical',
        'power': 75,
        'pp': 10,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 50,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'blast-burn': {
        'id': 307,
        'name': 'Blast-Burn',
        'type': 'fire',
        'category': 'special',
        'power': 150,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  User loses its next turn to "recharge", and cannot attack or switch out during that turn.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'hydro-cannon': {
        'id': 308,
        'name': 'Hydro-Cannon',
        'type': 'water',
        'category': 'special',
        'power': 150,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  User loses its next turn to "recharge", and cannot attack or switch out during that turn.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'meteor-mash': {
        'id': 309,
        'name': 'Meteor-Mash',
        'type': 'steel',
        'category': 'physical',
        'power': 90,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': "Inflicts regular damage. Has a $effect_chance% chance to raise the user's Attack one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 20,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }]
        }
    },
    'astonish': {
        'id': 310,
        'name': 'Astonish',
        'type': 'ghost',
        'category': 'physical',
        'power': 30,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'weather-ball': {
        'id': 311,
        'name': 'Weather-Ball',
        'type': 'normal',
        'category': 'special',
        'power': 50,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If a weather move is active, this move has double power, and its type becomes the type of the weather move.  shadow sky is typeless for the purposes of this move.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'aromatherapy': {
        'id': 312,
        'name': 'Aromatherapy',
        'type': 'grass',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': "Removes major status effects and confusion from every Pokémon in the user's party.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fake-tears': {
        'id': 313,
        'name': 'Fake-Tears',
        'type': 'dark',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's Special Defense by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'air-cutter': {
        'id': 314,
        'name': 'Air-Cutter',
        'type': 'flying',
        'category': 'special',
        'power': 60,
        'pp': 25,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'overheat': {
        'id': 315,
        'name': 'Overheat',
        'type': 'fire',
        'category': 'special',
        'power': 130,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': "Inflicts regular damage, then lowers the user's Special Attack by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'odor-sleuth': {
        'id': 316,
        'name': 'Odor-Sleuth',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': None,
        'priority': 0,
        'description': "Resets the target's evasion to normal and prevents any further boosting until the target leaves the field.  A ghost under this effect takes normal damage from normal and fighting moves.  This move itself ignores accuracy and evasion modifiers.",
        'meta': {
            'ailment': {
                'name': 'no-type-immunity',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'rock-tomb': {
        'id': 317,
        'name': 'Rock-Tomb',
        'type': 'rock',
        'category': 'physical',
        'power': 60,
        'pp': 15,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Speed by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'silver-wind': {
        'id': 318,
        'name': 'Silver-Wind',
        'type': 'bug',
        'category': 'special',
        'power': 60,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage. Has a $effect_chance% chance to raise all of the user's stats one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'hp',
                    'url': 'https://pokeapi.co/api/v2/stat/1/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'metal-sound': {
        'id': 319,
        'name': 'Metal-Sound',
        'type': 'steel',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': 85,
        'priority': 0,
        'description': "Lowers the target's Special Defense by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'grass-whistle': {
        'id': 320,
        'name': 'Grass-Whistle',
        'type': 'grass',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 55,
        'priority': 0,
        'description': 'Puts the target to sleep.',
        'meta': {
            'ailment': {
                'name': 'sleep',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 4,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'tickle': {
        'id': 321,
        'name': 'Tickle',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's Attack and Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }, {
                'change': -1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'cosmic-power': {
        'id': 322,
        'name': 'Cosmic-Power',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Defense and Special Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'water-spout': {
        'id': 323,
        'name': 'Water-Spout',
        'type': 'water',
        'category': 'special',
        'power': 150,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power increases with the user's remaining HP and is given by `150 * HP / max HP`, to a maximum of 150 when the user has full HP.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'signal-beam': {
        'id': 324,
        'name': 'Signal-Beam',
        'type': 'bug',
        'category': 'special',
        'power': 75,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to confuse the target.',
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'shadow-punch': {
        'id': 325,
        'name': 'Shadow-Punch',
        'type': 'ghost',
        'category': 'physical',
        'power': 60,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Inflicts regular damage.  Ignores accuracy and evasion modifiers.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'extrasensory': {
        'id': 326,
        'name': 'Extrasensory',
        'type': 'psychic',
        'category': 'special',
        'power': 80,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 10,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sky-uppercut': {
        'id': 327,
        'name': 'Sky-Uppercut',
        'type': 'fighting',
        'category': 'physical',
        'power': 85,
        'pp': 15,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.\n\nThis move can hit Pokémon under the effect of bounce, fly, or sky drop.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sand-tomb': {
        'id': 328,
        'name': 'Sand-Tomb',
        'type': 'ground',
        'category': 'physical',
        'power': 35,
        'pp': 15,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  For the next 2–5 turns, the target cannot leave the field and is damaged for 1/16 its max HP at the end of each turn.  The user continues to use other moves during this time.  If the user leaves the field, this effect ends.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.\n\nrapid spin cancels this effect.',
        'meta': {
            'ailment': {
                'name': 'trap',
                'chance': 100
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 6,
            'min_hits': None,
            'min_turns': 5,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sheer-cold': {
        'id': 329,
        'name': 'Sheer-Cold',
        'type': 'ice',
        'category': 'special',
        'power': None,
        'pp': 5,
        'accuracy': 30,
        'priority': 0,
        'description': "Inflicts damage equal to the target's max HP.  Ignores accuracy and evasion modifiers.  This move's accuracy is 30% plus 1% for each level the user is higher than the target.  If the user is a lower level than the target, this move will fail.\n\nBecause this move inflicts a specific and finite amount of damage, endure still prevents the target from fainting.\n\nThe effects of lock on, mind reader, and no guard still apply, as long as the user is equal or higher level than the target.  However, they will not give this move a chance to break through detect or protect.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'muddy-water': {
        'id': 330,
        'name': 'Muddy-Water',
        'type': 'water',
        'category': 'special',
        'power': 90,
        'pp': 10,
        'accuracy': 85,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's accuracy by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 30,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'accuracy',
                    'url': 'https://pokeapi.co/api/v2/stat/7/'
                }
            }]
        }
    },
    'bullet-seed': {
        'id': 331,
        'name': 'Bullet-Seed',
        'type': 'grass',
        'category': 'physical',
        'power': 25,
        'pp': 30,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits 2–5 times in one turn.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 5,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'aerial-ace': {
        'id': 332,
        'name': 'Aerial-Ace',
        'type': 'flying',
        'category': 'physical',
        'power': 60,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Inflicts regular damage.  Ignores accuracy and evasion modifiers.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'icicle-spear': {
        'id': 333,
        'name': 'Icicle-Spear',
        'type': 'ice',
        'category': 'physical',
        'power': 25,
        'pp': 30,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits 2–5 times in one turn.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 5,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'iron-defense': {
        'id': 334,
        'name': 'Iron-Defense',
        'type': 'steel',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Defense by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 2,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'block': {
        'id': 335,
        'name': 'Block',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': 'The target cannot switch out normally.  Ignores accuracy and evasion modifiers.  This effect ends when the user leaves the field.\n\nThe target may still escape by using baton pass, u turn, or a shed shell.\n\nBoth the user and the target pass on this effect with baton pass.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'howl': {
        'id': 336,
        'name': 'Howl',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Attack by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }]
        }
    },
    'dragon-claw': {
        'id': 337,
        'name': 'Dragon-Claw',
        'type': 'dragon',
        'category': 'physical',
        'power': 80,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'frenzy-plant': {
        'id': 338,
        'name': 'Frenzy-Plant',
        'type': 'grass',
        'category': 'special',
        'power': 150,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  User loses its next turn to "recharge", and cannot attack or switch out during that turn.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'bulk-up': {
        'id': 339,
        'name': 'Bulk-Up',
        'type': 'fighting',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Attack and Defense by one stage each.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'bounce': {
        'id': 340,
        'name': 'Bounce',
        'type': 'flying',
        'category': 'physical',
        'power': 85,
        'pp': 5,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  User bounces high into the air for one turn, becoming immune to attack, and hits on the second turn.  Has a $effect_chance% chance to paralyze the target.\n\nDuring the immune turn, gust, hurricane, sky uppercut, smack down, thunder, and twister still hit the user normally.  gust and twister also have double power against the user.\n\nThe damage from hail and sandstorm still applies during the immune turn.\n\nThe user may be hit during its immune turn if under the effect of lock on, mind reader, or no guard.\n\nThis move cannot be used while gravity is in effect.\n\nThis move cannot be selected by sleep talk.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'mud-shot': {
        'id': 341,
        'name': 'Mud-Shot',
        'type': 'ground',
        'category': 'special',
        'power': 55,
        'pp': 15,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Speed by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'poison-tail': {
        'id': 342,
        'name': 'Poison-Tail',
        'type': 'poison',
        'category': 'physical',
        'power': 50,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move. Has a $effect_chance% chance to poison the target.",
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 10
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'covet': {
        'id': 343,
        'name': 'Covet',
        'type': 'normal',
        'category': 'physical',
        'power': 60,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If the target is holding an item and the user is not, the user will permanently take the item.  Damage is still inflicted if an item cannot be taken.\n\nPokémon with sticky hold or multitype are immune to the item theft effect.\n\nThe target cannot recover its item with recycle.\n\nThis move cannot be selected by assist or metronome.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'volt-tackle': {
        'id': 344,
        'name': 'Volt-Tackle',
        'type': 'electric',
        'category': 'physical',
        'power': 120,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User takes 1/3 the damage it inflicts in recoil.  Has a $effect_chance% chance to paralyze the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': -33,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'magical-leaf': {
        'id': 345,
        'name': 'Magical-Leaf',
        'type': 'grass',
        'category': 'special',
        'power': 60,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Inflicts regular damage.  Ignores accuracy and evasion modifiers.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'water-sport': {
        'id': 346,
        'name': 'Water-Sport',
        'type': 'water',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': 'fire moves inflict half damage, regardless of target.  If the user leaves the field, this effect ends.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'calm-mind': {
        'id': 347,
        'name': 'Calm-Mind',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Special Attack and Special Defense by one stage each.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'leaf-blade': {
        'id': 348,
        'name': 'Leaf-Blade',
        'type': 'grass',
        'category': 'physical',
        'power': 90,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'dragon-dance': {
        'id': 349,
        'name': 'Dragon-Dance',
        'type': 'dragon',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Attack and Speed by one stage each.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'rock-blast': {
        'id': 350,
        'name': 'Rock-Blast',
        'type': 'rock',
        'category': 'physical',
        'power': 25,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits 2–5 times in one turn.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 5,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'shock-wave': {
        'id': 351,
        'name': 'Shock-Wave',
        'type': 'electric',
        'category': 'special',
        'power': 60,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Inflicts regular damage.  Ignores accuracy and evasion modifiers.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'water-pulse': {
        'id': 352,
        'name': 'Water-Pulse',
        'type': 'water',
        'category': 'special',
        'power': 60,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to confuse the target.',
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 20
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'doom-desire': {
        'id': 353,
        'name': 'Doom-Desire',
        'type': 'steel',
        'category': 'special',
        'power': 140,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts typeless regular damage at the end of the third turn, starting with this one.  This move cannot score a critical hit.  If the target switches out, its replacement will be hit instead.  Damage is calculated at the time this move is used; stat changes and switching out during the delay won't change the damage inflicted.  No move with this effect can be used against the same target again until after the end of the third turn.\n\nThis effect breaks through wonder guard.\n\nIf the target is protected by protect or detect on the turn this move is used, this move will fail.  However, the damage on the third turn will break through protection.\n\nThe damage is applied at the end of the turn, so it ignores endure and focus sash.\n\nThis move cannot be copied by mirror move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'psycho-boost': {
        'id': 354,
        'name': 'Psycho-Boost',
        'type': 'psychic',
        'category': 'special',
        'power': 140,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': "Inflicts regular damage, then lowers the user's Special Attack by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'roost': {
        'id': 355,
        'name': 'Roost',
        'type': 'flying',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'Heals the user for half its max HP.  If the user is flying, its flying type is ignored until the end of this turn.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 50,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'gravity': {
        'id': 356,
        'name': 'Gravity',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': "For five turns (including this one), all immunities to ground moves are disabled.  For the duration of this effect, the evasion of every Pokémon on the field is lowered by two stages.  Cancels the effects of bounce, fly, and sky drop.\n\nSpecifically, flying Pokémon and those with levitate or that have used magnet rise are no longer immune to ground attacks, arena trap, spikes, or toxic spikes.\n\nbounce, fly, sky drop, high jump kick, jump kick, and splash cannot be used while this move is in effect.\n\n*Bug*: If this move is used during a double or triple battle while Pokémon are under the effect of sky drop, Sky Drop's effect is not correctly canceled on its target, and it remains high in the air indefinitely.  As Sky Drop prevents the target from acting, the only way to subsequently remove it from the field is to faint it.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'miracle-eye': {
        'id': 357,
        'name': 'Miracle-Eye',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 40,
        'accuracy': None,
        'priority': 0,
        'description': "Resets the target's evasion to normal and prevents any further boosting until the target leaves the field.  A dark Pokémon under this effect takes normal damage from psychic moves.  This move itself ignores accuracy and evasion modifiers.",
        'meta': {
            'ailment': {
                'name': 'no-type-immunity',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'wake-up-slap': {
        'id': 358,
        'name': 'Wake-Up-Slap',
        'type': 'fighting',
        'category': 'physical',
        'power': 70,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If the target is sleeping, this move has double power, and the target wakes up.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'hammer-arm': {
        'id': 359,
        'name': 'Hammer-Arm',
        'type': 'fighting',
        'category': 'physical',
        'power': 100,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': "Inflicts regular damage, then lowers the user's Speed by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'gyro-ball': {
        'id': 360,
        'name': 'Gyro-Ball',
        'type': 'steel',
        'category': 'physical',
        'power': None,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power increases with the target's current Speed compared to the user, given by `1 + 25 * target Speed / user Speed`, capped at 150.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'healing-wish': {
        'id': 361,
        'name': 'Healing-Wish',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "User faints.  Its replacement's HP is fully restored, and any major status effect is removed.  If the replacement Pokémon is immediately fainted by a switch-in effect, the next replacement is healed by this move instead.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'brine': {
        'id': 362,
        'name': 'Brine',
        'type': 'water',
        'category': 'special',
        'power': 65,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If the target has less than half its max HP remaining, this move has double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'natural-gift': {
        'id': 363,
        'name': 'Natural-Gift',
        'type': 'normal',
        'category': 'physical',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power and type are determined by the user's held berry.  The berry is consumed.  If the user is not holding a berry, this move will fail.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'feint': {
        'id': 364,
        'name': 'Feint',
        'type': 'normal',
        'category': 'physical',
        'power': 30,
        'pp': 10,
        'accuracy': 100,
        'priority': 2,
        'description': 'Inflicts regular damage.  Removes the effects of detect or protect from the target before hitting.\n\nThis move cannot be copied by mirror move, nor selected by assist or metronome.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'pluck': {
        'id': 365,
        'name': 'Pluck',
        'type': 'flying',
        'category': 'physical',
        'power': 60,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  If the target is holding a berry, this move has double power, and the user takes the berry and uses it immediately.\n\nIf the target is holding a jaboca berry or rowap berry, the berry is still removed, but has no effect.\n\nIf this move is super effective and the target is holding a berry that can reduce this move's damage, it will do so, and will not be stolen.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'tailwind': {
        'id': 366,
        'name': 'Tailwind',
        'type': 'flying',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': "For the next three turns, all Pokémon on the user's side of the field have their original Speed doubled.  This effect remains if the user leaves the field.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'acupressure': {
        'id': 367,
        'name': 'Acupressure',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': None,
        'priority': 0,
        'description': "Raises one of the target's stats by two stages.  The raised stat is chosen at random from any stats that can be raised by two stages.  If no stat is eligible, this move will fail.\n\nIf the target has a substitute, this move will have no effect, even if the user is the target.\n\nThis move cannot be copied by mirror move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'metal-burst': {
        'id': 368,
        'name': 'Metal-Burst',
        'type': 'steel',
        'category': 'physical',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Targets the last opposing Pokémon to hit the user with a damaging move this turn.  Inflicts 1.5× the damage that move did to the user.  If there is no eligible target, this move will fail.  Type immunity applies, but other type effects are ignored.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'u-turn': {
        'id': 369,
        'name': 'U-Turn',
        'type': 'bug',
        'category': 'physical',
        'power': 70,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage, then the user immediately switches out, and the trainer selects a replacement Pokémon from the party.  If the target faints from this attack, the user's trainer selects the new Pokémon to send out first.  If the user is the last Pokémon in its party that can battle, it will not switch out.\n\nThe user may be hit by pursuit when it switches out, if it has been targeted and pursuit has not yet been used.\n\nThis move may be used even if the user is under the effect of ingrain.  ingrain's effect will end.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'close-combat': {
        'id': 370,
        'name': 'Close-Combat',
        'type': 'fighting',
        'category': 'physical',
        'power': 120,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage, then lowers the user's Defense and Special Defense by one stage each.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }, {
                'change': -1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'payback': {
        'id': 371,
        'name': 'Payback',
        'type': 'dark',
        'category': 'physical',
        'power': 50,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If the target uses a move or switches out this turn before this move is used, this move has double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'assurance': {
        'id': 372,
        'name': 'Assurance',
        'type': 'dark',
        'category': 'physical',
        'power': 60,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If the target takes damage this turn for any reason before this move is used, this move has double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'embargo': {
        'id': 373,
        'name': 'Embargo',
        'type': 'dark',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Target cannot use its held item for five turns.  If the target leaves the field, this effect ends.\n\nIf a Pokémon under this effect uses bug bite or pluck on a Pokémon holding a berry, the berry is destroyed but not used.  If a Pokémon under this effect uses fling, it will fail.\n\nThis effect is passed by baton pass.',
        'meta': {
            'ailment': {
                'name': 'embargo',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 5,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fling': {
        'id': 374,
        'name': 'Fling',
        'type': 'dark',
        'category': 'physical',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power and type are determined by the user's held item.  The item is consumed.  If the user is not holding an item, or its item has no set type and power, this move will fail.\n\nThis move ignores sticky hold.\n\nIf the user is under the effect of embargo, this move will fail.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'psycho-shift': {
        'id': 375,
        'name': 'Psycho-Shift',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "If the user has a major status effect and the target does not, the user's status is transferred to the target.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'trump-card': {
        'id': 376,
        'name': 'Trump-Card',
        'type': 'normal',
        'category': 'special',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': 0,
        'description': "Inflicts regular damage.  Power is determined by the PP remaining for this move, after its PP cost is deducted.  Ignores accuracy and evasion modifiers.\n\nPP remaining | Power\n------------ | ----:\n4 or more    |    40\n3            |    50\n2            |    60\n1            |    80\n0            |   200\n\nIf this move is activated by another move, the activating move's PP is used to calculate power.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'heal-block': {
        'id': 377,
        'name': 'Heal-Block',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'For the next five turns, the target may not use any moves that only restore HP, and move effects that heal the target are disabled.  Moves that steal HP may still be used, but will only inflict damage and not heal the target.',
        'meta': {
            'ailment': {
                'name': 'heal-block',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 5,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'wring-out': {
        'id': 378,
        'name': 'Wring-Out',
        'type': 'normal',
        'category': 'special',
        'power': None,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power directly relates to the target's relative remaining HP, given by `1 + 120 * current HP / max HP`, to a maximum of 121.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'power-trick': {
        'id': 379,
        'name': 'Power-Trick',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "The user's original Attack and Defense are swapped.\n\nThis effect is passed on by baton pass.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'gastro-acid': {
        'id': 380,
        'name': 'Gastro-Acid',
        'type': 'poison',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "The target's ability is disabled as long as it remains on the field.\n\nThis effect is passed on by baton pass.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'lucky-chant': {
        'id': 381,
        'name': 'Lucky-Chant',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': None,
        'priority': 0,
        'description': 'For five turns, opposing Pokémon cannot score critical hits.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'me-first': {
        'id': 382,
        'name': 'Me-First',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'If the target has selected a damaging move this turn, the user will copy that move and use it against the target, with a 50% increase in power.\n\nIf the target moves before the user, this move will fail.\n\nThis move cannot be copied by mirror move, nor selected by assist, metronome, or sleep talk.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'copycat': {
        'id': 383,
        'name': 'Copycat',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Uses the last move that was used successfully by any Pokémon, including the user.\n\nThis move cannot copy itself, nor roar nor whirlwind.\n\nThis move cannot be copied by mirror move, nor selected by assist, metronome, or sleep talk.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'power-swap': {
        'id': 384,
        'name': 'Power-Swap',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'User swaps its Attack and Special Attack stat modifiers modifiers with the target.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'guard-swap': {
        'id': 385,
        'name': 'Guard-Swap',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'User swaps its Defense and Special Defense modifiers with the target.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'punishment': {
        'id': 386,
        'name': 'Punishment',
        'type': 'dark',
        'category': 'physical',
        'power': None,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power starts at 60 and is increased by 20 for every stage any of the target's stats has been raised, capping at 200.  Accuracy and evasion modifiers do not increase this move's power.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'last-resort': {
        'id': 387,
        'name': 'Last-Resort',
        'type': 'normal',
        'category': 'physical',
        'power': 140,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  This move can only be used if each of the user's other moves has been used at least once since the user entered the field.  If this is the user's only move, this move will fail.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'worry-seed': {
        'id': 388,
        'name': 'Worry-Seed',
        'type': 'grass',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Changes the target's ability to insomnia.\n\nIf the target's ability is truant or multitype, this move will fail.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sucker-punch': {
        'id': 389,
        'name': 'Sucker-Punch',
        'type': 'dark',
        'category': 'physical',
        'power': 70,
        'pp': 5,
        'accuracy': 100,
        'priority': 1,
        'description': 'Inflicts regular damage.  If the target has not selected a damaging move this turn, or if the target has already acted this turn, this move will fail.\n\nThis move is not affected by iron fist.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'toxic-spikes': {
        'id': 390,
        'name': 'Toxic-Spikes',
        'type': 'poison',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Scatters poisoned spikes around the opposing field, which poison opposing Pokémon that enter the field.  A second layer of these spikes may be laid down, in which case Pokémon will be badly poisoned instead.  Pokémon immune to either ground moves or being poisoned are immune to this effect.  Pokémon otherwise immune to ground moves are affected during gravity.\n\nIf a poison Pokémon not immune to ground moves enters a field covered with poisoned spikes, the spikes are removed.\n\nrapid spin will remove this effect from its user's side of the field.  defog will remove this effect from its target's side of the field.\n\nThis move does not trigger synchronize, unless the Pokémon with synchronize was forced to enter the field by another effect such as roar.\n\nPokémon entering the field due to baton pass are not affected by this effect.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'heart-swap': {
        'id': 391,
        'name': 'Heart-Swap',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'User swaps its stat modifiers with the target.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'aqua-ring': {
        'id': 392,
        'name': 'Aqua-Ring',
        'type': 'water',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Restores 1/16 of the user's max HP at the end of each turn.  If the user leaves the field, this effect ends.\n\nThis effect is passed on by baton pass.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'magnet-rise': {
        'id': 393,
        'name': 'Magnet-Rise',
        'type': 'electric',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'For five turns, the user is immune to ground moves.\n\nIf the user is under the effect of ingrain or has levitate, this move will fail.\n\nThis effect is temporarily disabled by and cannot be used during gravity.\n\nThis effect is passed on by baton pass.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 5,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'flare-blitz': {
        'id': 394,
        'name': 'Flare-Blitz',
        'type': 'fire',
        'category': 'physical',
        'power': 120,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User takes 1/3 the damage it inflicts in recoil.  Has a $effect_chance% chance to burn the target.  Frozen Pokémon may use this move, in which case they will thaw.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': -33,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'force-palm': {
        'id': 395,
        'name': 'Force-Palm',
        'type': 'fighting',
        'category': 'physical',
        'power': 60,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'aura-sphere': {
        'id': 396,
        'name': 'Aura-Sphere',
        'type': 'fighting',
        'category': 'special',
        'power': 80,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Inflicts regular damage.  Ignores accuracy and evasion modifiers.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'rock-polish': {
        'id': 397,
        'name': 'Rock-Polish',
        'type': 'rock',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Speed by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 2,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'poison-jab': {
        'id': 398,
        'name': 'Poison-Jab',
        'type': 'poison',
        'category': 'physical',
        'power': 80,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to poison the target.',
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'dark-pulse': {
        'id': 399,
        'name': 'Dark-Pulse',
        'type': 'dark',
        'category': 'special',
        'power': 80,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 20,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'night-slash': {
        'id': 400,
        'name': 'Night-Slash',
        'type': 'dark',
        'category': 'physical',
        'power': 70,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'aqua-tail': {
        'id': 401,
        'name': 'Aqua-Tail',
        'type': 'water',
        'category': 'physical',
        'power': 90,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'seed-bomb': {
        'id': 402,
        'name': 'Seed-Bomb',
        'type': 'grass',
        'category': 'physical',
        'power': 80,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'air-slash': {
        'id': 403,
        'name': 'Air-Slash',
        'type': 'flying',
        'category': 'special',
        'power': 75,
        'pp': 15,
        'accuracy': 95,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'x-scissor': {
        'id': 404,
        'name': 'X-Scissor',
        'type': 'bug',
        'category': 'physical',
        'power': 80,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'bug-buzz': {
        'id': 405,
        'name': 'Bug-Buzz',
        'type': 'bug',
        'category': 'special',
        'power': 90,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Special Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'dragon-pulse': {
        'id': 406,
        'name': 'Dragon-Pulse',
        'type': 'dragon',
        'category': 'special',
        'power': 85,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'dragon-rush': {
        'id': 407,
        'name': 'Dragon-Rush',
        'type': 'dragon',
        'category': 'physical',
        'power': 100,
        'pp': 10,
        'accuracy': 75,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 20,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'power-gem': {
        'id': 408,
        'name': 'Power-Gem',
        'type': 'rock',
        'category': 'special',
        'power': 80,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'drain-punch': {
        'id': 409,
        'name': 'Drain-Punch',
        'type': 'fighting',
        'category': 'physical',
        'power': 75,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Drains half the damage inflicted to heal the user.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 50,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'vacuum-wave': {
        'id': 410,
        'name': 'Vacuum-Wave',
        'type': 'fighting',
        'category': 'special',
        'power': 40,
        'pp': 30,
        'accuracy': 100,
        'priority': 1,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'focus-blast': {
        'id': 411,
        'name': 'Focus-Blast',
        'type': 'fighting',
        'category': 'special',
        'power': 120,
        'pp': 5,
        'accuracy': 70,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Special Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'energy-ball': {
        'id': 412,
        'name': 'Energy-Ball',
        'type': 'grass',
        'category': 'special',
        'power': 90,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Special Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'brave-bird': {
        'id': 413,
        'name': 'Brave-Bird',
        'type': 'flying',
        'category': 'physical',
        'power': 120,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User takes 1/3 the damage it inflicts in recoil.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': -33,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'earth-power': {
        'id': 414,
        'name': 'Earth-Power',
        'type': 'ground',
        'category': 'special',
        'power': 90,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Special Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'switcheroo': {
        'id': 415,
        'name': 'Switcheroo',
        'type': 'dark',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "User and target permanently swap held items.  Works even if one of the Pokémon isn't holding anything.  If either Pokémon is holding mail, this move will fail.\n\nIf either Pokémon has multitype or sticky hold, this move will fail.\n\nIf this move results in a Pokémon obtaining choice band, choice scarf, or choice specs, and that Pokémon was the latter of the pair to move this turn, then the move it used this turn becomes its chosen forced move.  This applies even if both Pokémon had a choice item before this move was used.  If the first of the two Pokémon gains a choice item, it may select whatever choice move it wishes next turn.\n\nNeither the user nor the target can recover its item with recycle.\n\nThis move cannot be selected by assist or metronome.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'giga-impact': {
        'id': 416,
        'name': 'Giga-Impact',
        'type': 'normal',
        'category': 'physical',
        'power': 150,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  User loses its next turn to "recharge", and cannot attack or switch out during that turn.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'nasty-plot': {
        'id': 417,
        'name': 'Nasty-Plot',
        'type': 'dark',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Special Attack by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 2,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'bullet-punch': {
        'id': 418,
        'name': 'Bullet-Punch',
        'type': 'steel',
        'category': 'physical',
        'power': 40,
        'pp': 30,
        'accuracy': 100,
        'priority': 1,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'avalanche': {
        'id': 419,
        'name': 'Avalanche',
        'type': 'ice',
        'category': 'physical',
        'power': 60,
        'pp': 10,
        'accuracy': 100,
        'priority': -4,
        'description': 'Inflicts regular damage.  If the target damaged the user this turn and was the last to do so, this move has double power.\n\npain split does not count as damaging the user.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'ice-shard': {
        'id': 420,
        'name': 'Ice-Shard',
        'type': 'ice',
        'category': 'physical',
        'power': 40,
        'pp': 30,
        'accuracy': 100,
        'priority': 1,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'shadow-claw': {
        'id': 421,
        'name': 'Shadow-Claw',
        'type': 'ghost',
        'category': 'physical',
        'power': 70,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'thunder-fang': {
        'id': 422,
        'name': 'Thunder-Fang',
        'type': 'electric',
        'category': 'physical',
        'power': 65,
        'pp': 15,
        'accuracy': 95,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target and a separate $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 10,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'ice-fang': {
        'id': 423,
        'name': 'Ice-Fang',
        'type': 'ice',
        'category': 'physical',
        'power': 65,
        'pp': 15,
        'accuracy': 95,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to freeze the target and a separate $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'freeze',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 10,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fire-fang': {
        'id': 424,
        'name': 'Fire-Fang',
        'type': 'fire',
        'category': 'physical',
        'power': 65,
        'pp': 15,
        'accuracy': 95,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target and a separate $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 10,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'shadow-sneak': {
        'id': 425,
        'name': 'Shadow-Sneak',
        'type': 'ghost',
        'category': 'physical',
        'power': 40,
        'pp': 30,
        'accuracy': 100,
        'priority': 1,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'mud-bomb': {
        'id': 426,
        'name': 'Mud-Bomb',
        'type': 'ground',
        'category': 'special',
        'power': 65,
        'pp': 10,
        'accuracy': 85,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's accuracy by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 30,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'accuracy',
                    'url': 'https://pokeapi.co/api/v2/stat/7/'
                }
            }]
        }
    },
    'psycho-cut': {
        'id': 427,
        'name': 'Psycho-Cut',
        'type': 'psychic',
        'category': 'physical',
        'power': 70,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'zen-headbutt': {
        'id': 428,
        'name': 'Zen-Headbutt',
        'type': 'psychic',
        'category': 'physical',
        'power': 80,
        'pp': 15,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 20,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'mirror-shot': {
        'id': 429,
        'name': 'Mirror-Shot',
        'type': 'steel',
        'category': 'special',
        'power': 65,
        'pp': 10,
        'accuracy': 85,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's accuracy by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 30,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'accuracy',
                    'url': 'https://pokeapi.co/api/v2/stat/7/'
                }
            }]
        }
    },
    'flash-cannon': {
        'id': 430,
        'name': 'Flash-Cannon',
        'type': 'steel',
        'category': 'special',
        'power': 80,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Special Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'rock-climb': {
        'id': 431,
        'name': 'Rock-Climb',
        'type': 'normal',
        'category': 'physical',
        'power': 90,
        'pp': 20,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to confuse the target.',
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 20
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'defog': {
        'id': 432,
        'name': 'Defog',
        'type': 'flying',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': "Lowers the target's evasion by one stage.  Clears away fog.  Removes the effects of mist, light screen, reflect, safeguard, spikes, stealth rock, and toxic spikes from the target's side of the field.\n\nIf the target is protected by mist, it will prevent the evasion change, then be removed by this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'trick-room': {
        'id': 433,
        'name': 'Trick-Room',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 5,
        'accuracy': None,
        'priority': -7,
        'description': 'For five turns (including this one), slower Pokémon will act before faster Pokémon.  Move priority is not affected.  Using this move when its effect is already active will end the effect.\n\nPokémon holding full incense, lagging tail, or quick claw and Pokémon with stall ignore this effect.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'draco-meteor': {
        'id': 434,
        'name': 'Draco-Meteor',
        'type': 'dragon',
        'category': 'special',
        'power': 130,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': "Inflicts regular damage, then lowers the user's Special Attack by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'discharge': {
        'id': 435,
        'name': 'Discharge',
        'type': 'electric',
        'category': 'special',
        'power': 80,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'lava-plume': {
        'id': 436,
        'name': 'Lava-Plume',
        'type': 'fire',
        'category': 'special',
        'power': 80,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'leaf-storm': {
        'id': 437,
        'name': 'Leaf-Storm',
        'type': 'grass',
        'category': 'special',
        'power': 130,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': "Inflicts regular damage, then lowers the user's Special Attack by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'power-whip': {
        'id': 438,
        'name': 'Power-Whip',
        'type': 'grass',
        'category': 'physical',
        'power': 120,
        'pp': 10,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'rock-wrecker': {
        'id': 439,
        'name': 'Rock-Wrecker',
        'type': 'rock',
        'category': 'physical',
        'power': 150,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  User loses its next turn to "recharge", and cannot attack or switch out during that turn.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'cross-poison': {
        'id': 440,
        'name': 'Cross-Poison',
        'type': 'poison',
        'category': 'physical',
        'power': 70,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move. Has a $effect_chance% chance to poison the target.",
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 10
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'gunk-shot': {
        'id': 441,
        'name': 'Gunk-Shot',
        'type': 'poison',
        'category': 'physical',
        'power': 120,
        'pp': 5,
        'accuracy': 80,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to poison the target.',
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'iron-head': {
        'id': 442,
        'name': 'Iron-Head',
        'type': 'steel',
        'category': 'physical',
        'power': 80,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'magnet-bomb': {
        'id': 443,
        'name': 'Magnet-Bomb',
        'type': 'steel',
        'category': 'physical',
        'power': 60,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': 'Inflicts regular damage.  Ignores accuracy and evasion modifiers.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'stone-edge': {
        'id': 444,
        'name': 'Stone-Edge',
        'type': 'rock',
        'category': 'physical',
        'power': 100,
        'pp': 5,
        'accuracy': 80,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'captivate': {
        'id': 445,
        'name': 'Captivate',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's Special Attack by two stages.  If the user and target are the same gender, or either is genderless, this move will fail.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'stealth-rock': {
        'id': 446,
        'name': 'Stealth-Rock',
        'type': 'rock',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Spreads sharp rocks around the opposing field, damaging any Pokémon that enters the field for 1/8 its max HP.  This damage is affected by the entering Pokémon's susceptibility to rock moves.\n\nrapid spin removes this effect from its user's side of the field.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'grass-knot': {
        'id': 447,
        'name': 'Grass-Knot',
        'type': 'grass',
        'category': 'special',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power increases with the target's weight in kilograms, to a maximum of 120.\n\nTarget's weight | Power\n--------------- | ----:\nUp to 10kg      |    20\nUp to 25kg      |    40\nUp to 50kg      |    60\nUp to 100kg     |    80\nUp to 200kg     |   100\nAbove 200kg     |   120\n",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'chatter': {
        'id': 448,
        'name': 'Chatter',
        'type': 'flying',
        'category': 'special',
        'power': 65,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has either a 1%, 11%, or 31% chance to confuse the target, based on the volume of the recording made for this move; louder recordings increase the chance of confusion.  If the user is not a chatot, this move will not cause confusion.\n\nThis move cannot be copied by mimic, mirror move, or sketch, nor selected by assist, metronome, or sleep talk.',
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 100
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'judgment': {
        'id': 449,
        'name': 'Judgment',
        'type': 'normal',
        'category': 'special',
        'power': 100,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  If the user is holding a plate or a drive, this move's type is the type corresponding to that item.\n\nNote: This effect is technically shared by both techno blast and judgment; however, Techno Blast is only affected by drives, and Judgment is only affected by plates.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'bug-bite': {
        'id': 450,
        'name': 'Bug-Bite',
        'type': 'bug',
        'category': 'physical',
        'power': 60,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  If the target is holding a berry, this move has double power, and the user takes the berry and uses it immediately.\n\nIf the target is holding a jaboca berry or rowap berry, the berry is still removed, but has no effect.\n\nIf this move is super effective and the target is holding a berry that can reduce this move's damage, it will do so, and will not be stolen.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'charge-beam': {
        'id': 451,
        'name': 'Charge-Beam',
        'type': 'electric',
        'category': 'special',
        'power': 50,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to raise the user's Special Attack by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 70,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'wood-hammer': {
        'id': 452,
        'name': 'Wood-Hammer',
        'type': 'grass',
        'category': 'physical',
        'power': 120,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User takes 1/3 the damage it inflicts in recoil.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': -33,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'aqua-jet': {
        'id': 453,
        'name': 'Aqua-Jet',
        'type': 'water',
        'category': 'physical',
        'power': 40,
        'pp': 20,
        'accuracy': 100,
        'priority': 1,
        'description': 'Inflicts regular damage.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'attack-order': {
        'id': 454,
        'name': 'Attack-Order',
        'type': 'bug',
        'category': 'physical',
        'power': 90,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'defend-order': {
        'id': 455,
        'name': 'Defend-Order',
        'type': 'bug',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Defense and Special Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'heal-order': {
        'id': 456,
        'name': 'Heal-Order',
        'type': 'bug',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'Heals the user for half its max HP.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 50,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'head-smash': {
        'id': 457,
        'name': 'Head-Smash',
        'type': 'rock',
        'category': 'physical',
        'power': 150,
        'pp': 5,
        'accuracy': 80,
        'priority': 0,
        'description': 'Inflicts regular damage.  User takes 1/2 the damage it inflicts in recoil.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': -50,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'double-hit': {
        'id': 458,
        'name': 'Double-Hit',
        'type': 'normal',
        'category': 'physical',
        'power': 35,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits twice in one turn.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 2,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'roar-of-time': {
        'id': 459,
        'name': 'Roar-Of-Time',
        'type': 'dragon',
        'category': 'special',
        'power': 150,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  User loses its next turn to "recharge", and cannot attack or switch out during that turn.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'spacial-rend': {
        'id': 460,
        'name': 'Spacial-Rend',
        'type': 'dragon',
        'category': 'special',
        'power': 100,
        'pp': 5,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'lunar-dance': {
        'id': 461,
        'name': 'Lunar-Dance',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "User faints.  Its replacement's HP and PP are fully restored, and any major status effect is removed.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'crush-grip': {
        'id': 462,
        'name': 'Crush-Grip',
        'type': 'normal',
        'category': 'physical',
        'power': None,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power directly relates to the target's relative remaining HP, given by `1 + 120 * current HP / max HP`, to a maximum of 121.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'magma-storm': {
        'id': 463,
        'name': 'Magma-Storm',
        'type': 'fire',
        'category': 'special',
        'power': 100,
        'pp': 5,
        'accuracy': 75,
        'priority': 0,
        'description': 'Inflicts regular damage.  For the next 2–5 turns, the target cannot leave the field and is damaged for 1/16 its max HP at the end of each turn.  The user continues to use other moves during this time.  If the user leaves the field, this effect ends.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.\n\nrapid spin cancels this effect.',
        'meta': {
            'ailment': {
                'name': 'trap',
                'chance': 100
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 6,
            'min_hits': None,
            'min_turns': 5,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'dark-void': {
        'id': 464,
        'name': 'Dark-Void',
        'type': 'dark',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': 50,
        'priority': 0,
        'description': 'Puts the target to sleep.',
        'meta': {
            'ailment': {
                'name': 'sleep',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 4,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'seed-flare': {
        'id': 465,
        'name': 'Seed-Flare',
        'type': 'grass',
        'category': 'special',
        'power': 120,
        'pp': 5,
        'accuracy': 85,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Special Defense by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 40,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'ominous-wind': {
        'id': 466,
        'name': 'Ominous-Wind',
        'type': 'ghost',
        'category': 'special',
        'power': 60,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage. Has a $effect_chance% chance to raise all of the user's stats one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 10,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'hp',
                    'url': 'https://pokeapi.co/api/v2/stat/1/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'shadow-force': {
        'id': 467,
        'name': 'Shadow-Force',
        'type': 'ghost',
        'category': 'physical',
        'power': 120,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User vanishes for one turn, becoming immune to attack, and hits on the second turn.\n\nThis move ignores the effects of detect and protect.\n\nThis move cannot be selected by sleep talk.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'hone-claws': {
        'id': 468,
        'name': 'Hone-Claws',
        'type': 'dark',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Attack and accuracy by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'accuracy',
                    'url': 'https://pokeapi.co/api/v2/stat/7/'
                }
            }]
        }
    },
    'wide-guard': {
        'id': 469,
        'name': 'Wide-Guard',
        'type': 'rock',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 3,
        'description': 'Moves with multiple targets will not hit friendly Pokémon for the remainder of this turn.  If the user is last to act this turn, this move will fail.\n\nThis move cannot be selected by assist or metronome.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'guard-split': {
        'id': 470,
        'name': 'Guard-Split',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "Averages the user's unmodified Defense with the target's unmodified Defense; the value becomes the unmodified Defense for both Pokémon. Unmodified Special Defense is averaged the same way.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'power-split': {
        'id': 471,
        'name': 'Power-Split',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "Averages the user's unmodified Attack with the target's unmodified Attack; the value becomes the unmodified Attack for both Pokémon. Unmodified Special Attack is averaged the same way.\n\nThis effect applies before any other persistent changes to unmodified Attack or Special Attack, such as flower gift during sunny day.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'wonder-room': {
        'id': 472,
        'name': 'Wonder-Room',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "For five turns (including this one), every Pokémon's Defense and Special Defense are swapped.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'psyshock': {
        'id': 473,
        'name': 'Psyshock',
        'type': 'psychic',
        'category': 'special',
        'power': 80,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Damage calculation always uses the target's Defense, regardless of this move's damage class.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'venoshock': {
        'id': 474,
        'name': 'Venoshock',
        'type': 'poison',
        'category': 'special',
        'power': 65,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If the target is poisoned, this move has double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'autotomize': {
        'id': 475,
        'name': 'Autotomize',
        'type': 'steel',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Speed by two stages.  Halves the user's weight; this effect does not stack.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 2,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'rage-powder': {
        'id': 476,
        'name': 'Rage-Powder',
        'type': 'bug',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 2,
        'description': "Until the end of this turn, any moves that opposing Pokémon target solely at the user's ally will instead target the user.  If both Pokémon on the same side of the field use this move on the same turn, the Pokémon that uses it last will become the target.\n\nThis effect takes priority over lightning rod and storm drain.\n\nIf the user's ally switches out, opposing Pokémon may still hit it with pursuit.\n\nThis move cannot be selected by assist or metronome.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'telekinesis': {
        'id': 477,
        'name': 'Telekinesis',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': 'For three turns (including this one), moves used against the target have 100% accuracy, but the target is immune to ground damage.  Accuracy of one-hit KO moves is exempt from this effect.\n\nThis effect is removed by gravity.  If Gravity is already in effect, this move will fail.',
        'meta': {
            'ailment': {
                'name': 'unknown',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 3,
            'min_hits': None,
            'min_turns': 3,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'magic-room': {
        'id': 478,
        'name': 'Magic-Room',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'For five turns (including this one), passive effects of held items are ignored, and Pokémon will not use their held items.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'smack-down': {
        'id': 479,
        'name': 'Smack-Down',
        'type': 'rock',
        'category': 'physical',
        'power': 50,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Removes the target's immunity to ground-type damage.  This effect removes any existing Ground immunity due to levitate, magnet rise, or telekinesis, and causes the target's flying type to be ignored when it takes Ground damage.\n\nIf the target isn't immune to Ground damage, this move will fail.\n\nThis move can hit Pokémon under the effect of bounce, fly, or sky drop, and ends the effect of Bounce or Fly.",
        'meta': {
            'ailment': {
                'name': 'unknown',
                'chance': 100
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'storm-throw': {
        'id': 480,
        'name': 'Storm-Throw',
        'type': 'fighting',
        'category': 'physical',
        'power': 60,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Always scores a critical hit.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 6,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'flame-burst': {
        'id': 481,
        'name': 'Flame-Burst',
        'type': 'fire',
        'category': 'special',
        'power': 70,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If this move successfully hits the target, any Pokémon adjacent to the target are damaged for 1/16 their max HP.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sludge-wave': {
        'id': 482,
        'name': 'Sludge-Wave',
        'type': 'poison',
        'category': 'special',
        'power': 95,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to poison the target.',
        'meta': {
            'ailment': {
                'name': 'poison',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'quiver-dance': {
        'id': 483,
        'name': 'Quiver-Dance',
        'type': 'bug',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Special Attack, Special Defense, and Speed by one stage each.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'heavy-slam': {
        'id': 484,
        'name': 'Heavy-Slam',
        'type': 'steel',
        'category': 'physical',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  The greater the user's weight compared to the target's, the higher power this move has, to a maximum of 120.\n\nUser's weight                    | Power\n-------------------------------- | ----:\nUp to 2× the target's weight     |    40\nUp to 3× the target's weight     |    60\nUp to 4× the target's weight     |    80\nUp to 5× the target's weight     |   100\nMore than 5× the target's weight |   120\n",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'synchronoise': {
        'id': 485,
        'name': 'Synchronoise',
        'type': 'psychic',
        'category': 'special',
        'power': 120,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Only Pokémon that share a type with the user will take damage from this move.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'electro-ball': {
        'id': 486,
        'name': 'Electro-Ball',
        'type': 'electric',
        'category': 'special',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  The greater the user's Speed compared to the target's, the higher power this move has, to a maximum of 150.\n\nUser's Speed                     | Power\n-------------------------------- | ----:\nUp to 2× the target's Speed      |    60\nUp to 3× the target's Speed      |    80\nUp to 4× the target's Speed      |   120\nMore than 4× the target's Speed  |   150\n",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'soak': {
        'id': 487,
        'name': 'Soak',
        'type': 'water',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Changes the target to pure water-type until it leaves the field.  If the target has multitype, this move will fail.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'flame-charge': {
        'id': 488,
        'name': 'Flame-Charge',
        'type': 'fire',
        'category': 'physical',
        'power': 50,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Raises the user's Speed by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'coil': {
        'id': 489,
        'name': 'Coil',
        'type': 'poison',
        'category': 'status',
        'power': None,
        'pp': 20,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Attack, Defense, and accuracy by one stage each.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'accuracy',
                    'url': 'https://pokeapi.co/api/v2/stat/7/'
                }
            }]
        }
    },
    'low-sweep': {
        'id': 490,
        'name': 'Low-Sweep',
        'type': 'fighting',
        'category': 'physical',
        'power': 65,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Lowers the target's Speed by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'acid-spray': {
        'id': 491,
        'name': 'Acid-Spray',
        'type': 'poison',
        'category': 'special',
        'power': 40,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Lowers the target's Special Defense by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -2,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }]
        }
    },
    'foul-play': {
        'id': 492,
        'name': 'Foul-Play',
        'type': 'dark',
        'category': 'physical',
        'power': 95,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Damage is calculated using the target's attacking stat rather than the user's.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'simple-beam': {
        'id': 493,
        'name': 'Simple-Beam',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Changes the target's ability to simple.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'entrainment': {
        'id': 494,
        'name': 'Entrainment',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Changes the target's ability to match the user's.  This effect ends when the target leaves battle.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'after-you': {
        'id': 495,
        'name': 'After-You',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': 'The target will act next this turn, regardless of Speed or move priority.\nIf the target has already acted this turn, this move will fail.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'round': {
        'id': 496,
        'name': 'Round',
        'type': 'normal',
        'category': 'special',
        'power': 60,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  If round has already been used this turn, this move's power is doubled.  After this move is used, any other Pokémon using it this turn will immediately do so (in the order they would otherwise act), regardless of Speed or priority.  Pokémon using other moves will then continue to act as usual.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'echoed-voice': {
        'id': 497,
        'name': 'Echoed-Voice',
        'type': 'normal',
        'category': 'special',
        'power': 40,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  If any friendly Pokémon used this move earlier this turn or on the previous turn, that use's power is added to this move's power, to a maximum of 200.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'chip-away': {
        'id': 498,
        'name': 'Chip-Away',
        'type': 'normal',
        'category': 'physical',
        'power': 70,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Damage calculation ignores the target's stat modifiers, including evasion.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'clear-smog': {
        'id': 499,
        'name': 'Clear-Smog',
        'type': 'poison',
        'category': 'special',
        'power': 50,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': "Inflicts regular damage.  All of the target's stat modifiers are reset to zero.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'stored-power': {
        'id': 500,
        'name': 'Stored-Power',
        'type': 'psychic',
        'category': 'special',
        'power': 20,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Power is increased by 100% its original value for every stage any of the user's stats have been raised.  Accuracy, evasion, and lowered stats do not affect this move's power.  For a Pokémon with all five stats modified to +6, this move's power is 31×.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'quick-guard': {
        'id': 501,
        'name': 'Quick-Guard',
        'type': 'fighting',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 3,
        'description': 'Moves with priority greater than 0 will not hit friendly Pokémon for the remainder of this turn.  If the user is last to act this turn, this move will fail.\n\nThis move cannot be selected by assist or metronome.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'ally-switch': {
        'id': 502,
        'name': 'Ally-Switch',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 2,
        'description': 'User switches position on the field with the friendly Pokémon opposite it.  If the user is in the middle position in a triple battle, or there are no other friendly Pokémon, this move will fail.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'scald': {
        'id': 503,
        'name': 'Scald',
        'type': 'water',
        'category': 'special',
        'power': 80,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'shell-smash': {
        'id': 504,
        'name': 'Shell-Smash',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Attack, Special Attack, and Speed by two stages each.  Lowers the user's Defense and Special Defense by one stage each.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'heal-pulse': {
        'id': 505,
        'name': 'Heal-Pulse',
        'type': 'psychic',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': 'Heals the target for half its max HP.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 50,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'hex': {
        'id': 506,
        'name': 'Hex',
        'type': 'ghost',
        'category': 'special',
        'power': 65,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If the target has a major status ailment, this move has double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sky-drop': {
        'id': 507,
        'name': 'Sky-Drop',
        'type': 'flying',
        'category': 'physical',
        'power': 60,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User carries the target high into the air for one turn, during which no moves will hit either Pokémon and neither can act.  On the following turn, the user drops the target, inflicting damage and ending the effect.\n\nIf the target is flying-type, this move will function as normal but inflict no damage.\n\ngust, hurricane, sky uppercut, smack down, thunder, twister, and whirlwind can hit both the user and the target during this effect.  gust and twister will additionally have double power.\n\nThe damage from hail and sandstorm still applies during this effect.\n\nEither Pokémon may be hit during this effect if also under the effect of lock on, mind reader, or no guard.\n\nThis move cannot be used while gravity is in effect.\n\nThis move cannot be selected by sleep talk.\n\n*Bug*: If gravity is used during a double or triple battle while this move is in effect, this move is not correctly canceled on the target, and it remains high in the air indefinitely.  As this move prevents the target from acting, the only way to subsequently remove it from the field is to faint it.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'shift-gear': {
        'id': 508,
        'name': 'Shift-Gear',
        'type': 'steel',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Attack by one stage and its Speed by two stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }, {
                'change': 2,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'circle-throw': {
        'id': 509,
        'name': 'Circle-Throw',
        'type': 'fighting',
        'category': 'physical',
        'power': 60,
        'pp': 10,
        'accuracy': 90,
        'priority': -6,
        'description': "Inflicts regular damage, then switches the target out for another of its trainer's Pokémon, selected at random.\n\nIf the target is under the effect of ingrain or suction cups, or it has a substitute, or its Trainer has no more usable Pokémon, it will not be switched out.  If the target is a wild Pokémon, the battle ends instead.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'incinerate': {
        'id': 510,
        'name': 'Incinerate',
        'type': 'fire',
        'category': 'special',
        'power': 60,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  If the target is holding a berry, it's destroyed and cannot be used in response to this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'quash': {
        'id': 511,
        'name': 'Quash',
        'type': 'dark',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Forces the target to act last this turn, regardless of Speed or move priority.  If the target has already acted this turn, this move will fail.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'acrobatics': {
        'id': 512,
        'name': 'Acrobatics',
        'type': 'flying',
        'category': 'physical',
        'power': 55,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If the user has no held item, this move has double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'reflect-type': {
        'id': 513,
        'name': 'Reflect-Type',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': "User's type changes to match the target's.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'retaliate': {
        'id': 514,
        'name': 'Retaliate',
        'type': 'normal',
        'category': 'physical',
        'power': 70,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If a friendly Pokémon fainted on the previous turn, this move has double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'final-gambit': {
        'id': 515,
        'name': 'Final-Gambit',
        'type': 'fighting',
        'category': 'special',
        'power': None,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts damage equal to the user's remaining HP.  User faints.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'bestow': {
        'id': 516,
        'name': 'Bestow',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 15,
        'accuracy': None,
        'priority': 0,
        'description': "Transfers the user's held item to the target.  If the user has no held item, or the target already has a held item, this move will fail.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'inferno': {
        'id': 517,
        'name': 'Inferno',
        'type': 'fire',
        'category': 'special',
        'power': 100,
        'pp': 5,
        'accuracy': 50,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 100
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'water-pledge': {
        'id': 518,
        'name': 'Water-Pledge',
        'type': 'water',
        'category': 'special',
        'power': 80,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If a friendly Pokémon used grass pledge earlier this turn, all opposing Pokémon have halved Speed for four turns (including this one).',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fire-pledge': {
        'id': 519,
        'name': 'Fire-Pledge',
        'type': 'fire',
        'category': 'special',
        'power': 80,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If a friendly Pokémon used water pledge earlier this turn, moves used by any friendly Pokémon have doubled effect chance for four turns (including this one).',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'grass-pledge': {
        'id': 520,
        'name': 'Grass-Pledge',
        'type': 'grass',
        'category': 'special',
        'power': 80,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If a friendly Pokémon used fire pledge earlier this turn, all opposing Pokémon will take 1/8 their max HP in damage at the end of every turn for four turns (including this one).',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'volt-switch': {
        'id': 521,
        'name': 'Volt-Switch',
        'type': 'electric',
        'category': 'special',
        'power': 70,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage, then the user immediately switches out, and the trainer selects a replacement Pokémon from the party.  If the target faints from this attack, the user's trainer selects the new Pokémon to send out first.  If the user is the last Pokémon in its party that can battle, it will not switch out.\n\nThe user may be hit by pursuit when it switches out, if it has been targeted and pursuit has not yet been used.\n\nThis move may be used even if the user is under the effect of ingrain.  ingrain's effect will end.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'struggle-bug': {
        'id': 522,
        'name': 'Struggle-Bug',
        'type': 'bug',
        'category': 'special',
        'power': 50,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Special Attack by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'bulldoze': {
        'id': 523,
        'name': 'Bulldoze',
        'type': 'ground',
        'category': 'physical',
        'power': 60,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Speed by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'frost-breath': {
        'id': 524,
        'name': 'Frost-Breath',
        'type': 'ice',
        'category': 'special',
        'power': 60,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Always scores a critical hit.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 100
            },
            'crit_rate': 6,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'dragon-tail': {
        'id': 525,
        'name': 'Dragon-Tail',
        'type': 'dragon',
        'category': 'physical',
        'power': 60,
        'pp': 10,
        'accuracy': 90,
        'priority': -6,
        'description': "Inflicts regular damage, then switches the target out for another of its trainer's Pokémon, selected at random.\n\nIf the target is under the effect of ingrain or suction cups, or it has a substitute, or its Trainer has no more usable Pokémon, it will not be switched out.  If the target is a wild Pokémon, the battle ends instead.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'work-up': {
        'id': 526,
        'name': 'Work-Up',
        'type': 'normal',
        'category': 'status',
        'power': None,
        'pp': 30,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Attack and Special Attack by one stage each.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'attack',
                    'url': 'https://pokeapi.co/api/v2/stat/2/'
                }
            }, {
                'change': 1,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'electroweb': {
        'id': 527,
        'name': 'Electroweb',
        'type': 'electric',
        'category': 'special',
        'power': 55,
        'pp': 15,
        'accuracy': 95,
        'priority': 0,
        'description': "Lowers the target's Speed by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'wild-charge': {
        'id': 528,
        'name': 'Wild-Charge',
        'type': 'electric',
        'category': 'physical',
        'power': 90,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User takes 1/4 the damage it inflicts in recoil.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': -25,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'drill-run': {
        'id': 529,
        'name': 'Drill-Run',
        'type': 'ground',
        'category': 'physical',
        'power': 80,
        'pp': 10,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  User's critical hit rate is one level higher when using this move.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 1,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'dual-chop': {
        'id': 530,
        'name': 'Dual-Chop',
        'type': 'dragon',
        'category': 'physical',
        'power': 40,
        'pp': 15,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits twice in one turn.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 2,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'heart-stamp': {
        'id': 531,
        'name': 'Heart-Stamp',
        'type': 'psychic',
        'category': 'physical',
        'power': 60,
        'pp': 25,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'horn-leech': {
        'id': 532,
        'name': 'Horn-Leech',
        'type': 'grass',
        'category': 'physical',
        'power': 75,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Drains half the damage inflicted to heal the user.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 50,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'sacred-sword': {
        'id': 533,
        'name': 'Sacred-Sword',
        'type': 'fighting',
        'category': 'physical',
        'power': 90,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Damage calculation ignores the target's stat modifiers, including evasion.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'razor-shell': {
        'id': 534,
        'name': 'Razor-Shell',
        'type': 'water',
        'category': 'physical',
        'power': 75,
        'pp': 10,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Defense by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 50,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'heat-crash': {
        'id': 535,
        'name': 'Heat-Crash',
        'type': 'fire',
        'category': 'physical',
        'power': None,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  The greater the user's weight compared to the target's, the higher power this move has, to a maximum of 120.\n\nUser's weight                    | Power\n-------------------------------- | ----:\nUp to 2× the target's weight     |    40\nUp to 3× the target's weight     |    60\nUp to 4× the target's weight     |    80\nUp to 5× the target's weight     |   100\nMore than 5× the target's weight |   120\n",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'leaf-tornado': {
        'id': 536,
        'name': 'Leaf-Tornado',
        'type': 'grass',
        'category': 'special',
        'power': 65,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's accuracy by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 50,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'accuracy',
                    'url': 'https://pokeapi.co/api/v2/stat/7/'
                }
            }]
        }
    },
    'steamroller': {
        'id': 537,
        'name': 'Steamroller',
        'type': 'bug',
        'category': 'physical',
        'power': 65,
        'pp': 20,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.\n\nPower is doubled against Pokémon that have used minimize since entering the field.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'cotton-guard': {
        'id': 538,
        'name': 'Cotton-Guard',
        'type': 'grass',
        'category': 'status',
        'power': None,
        'pp': 10,
        'accuracy': None,
        'priority': 0,
        'description': "Raises the user's Defense by three stages.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': [{
                'change': 3,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }]
        }
    },
    'night-daze': {
        'id': 539,
        'name': 'Night-Daze',
        'type': 'dark',
        'category': 'special',
        'power': 85,
        'pp': 10,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's accuracy by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 40,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'accuracy',
                    'url': 'https://pokeapi.co/api/v2/stat/7/'
                }
            }]
        }
    },
    'psystrike': {
        'id': 540,
        'name': 'Psystrike',
        'type': 'psychic',
        'category': 'special',
        'power': 100,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Damage calculation always uses the target's Defense, regardless of this move's damage class.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'tail-slap': {
        'id': 541,
        'name': 'Tail-Slap',
        'type': 'normal',
        'category': 'physical',
        'power': 25,
        'pp': 10,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits 2–5 times in one turn.\n\nHas a 3/8 chance each to hit 2 or 3 times, and a 1/8 chance each to hit 4 or 5 times.  Averages to 3 hits per use.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 5,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'hurricane': {
        'id': 542,
        'name': 'Hurricane',
        'type': 'flying',
        'category': 'special',
        'power': 110,
        'pp': 10,
        'accuracy': 70,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to confuse the target.\n\nThis move can hit Pokémon under the effect of bounce, fly, or sky drop.\n\nDuring rain dance, this move has 100% accuracy.  During sunny day, this move has 50% accuracy.',
        'meta': {
            'ailment': {
                'name': 'confusion',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 5,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'head-charge': {
        'id': 543,
        'name': 'Head-Charge',
        'type': 'normal',
        'category': 'physical',
        'power': 120,
        'pp': 15,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  User takes 1/4 the damage it inflicts in recoil.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': -25,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'gear-grind': {
        'id': 544,
        'name': 'Gear-Grind',
        'type': 'steel',
        'category': 'physical',
        'power': 50,
        'pp': 15,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  Hits twice in one turn.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': 2,
            'max_turns': None,
            'min_hits': 2,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'searing-shot': {
        'id': 545,
        'name': 'Searing-Shot',
        'type': 'fire',
        'category': 'special',
        'power': 100,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'techno-blast': {
        'id': 546,
        'name': 'Techno-Blast',
        'type': 'normal',
        'category': 'special',
        'power': 120,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  If the user is holding a plate or a drive, this move's type is the type corresponding to that item.\n\nNote: This effect is technically shared by both techno blast and judgment; however, Techno Blast is only affected by drives, and Judgment is only affected by plates.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'relic-song': {
        'id': 547,
        'name': 'Relic-Song',
        'type': 'normal',
        'category': 'special',
        'power': 75,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to put the target to sleep.\nIf the user is a meloetta, it will toggle between Aria and Pirouette Forme.',
        'meta': {
            'ailment': {
                'name': 'sleep',
                'chance': 10
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': 4,
            'min_hits': None,
            'min_turns': 2,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'secret-sword': {
        'id': 548,
        'name': 'Secret-Sword',
        'type': 'fighting',
        'category': 'special',
        'power': 85,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Damage calculation always uses the target's Defense, regardless of this move's damage class.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'glaciate': {
        'id': 549,
        'name': 'Glaciate',
        'type': 'ice',
        'category': 'special',
        'power': 65,
        'pp': 10,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  Lowers the target's Speed by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'bolt-strike': {
        'id': 550,
        'name': 'Bolt-Strike',
        'type': 'electric',
        'category': 'physical',
        'power': 130,
        'pp': 5,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 20
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'blue-flare': {
        'id': 551,
        'name': 'Blue-Flare',
        'type': 'fire',
        'category': 'special',
        'power': 130,
        'pp': 5,
        'accuracy': 85,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 20
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fiery-dance': {
        'id': 552,
        'name': 'Fiery-Dance',
        'type': 'fire',
        'category': 'special',
        'power': 80,
        'pp': 10,
        'accuracy': 100,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to raise the user's Special Attack by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 50,
            'stat_changes': [{
                'change': 1,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'freeze-shock': {
        'id': 553,
        'name': 'Freeze-Shock',
        'type': 'ice',
        'category': 'physical',
        'power': 140,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to paralyze the target.  User charges for one turn before attacking.',
        'meta': {
            'ailment': {
                'name': 'paralysis',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'ice-burn': {
        'id': 554,
        'name': 'Ice-Burn',
        'type': 'ice',
        'category': 'special',
        'power': 140,
        'pp': 5,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to burn the target.  User charges for one turn before attacking.',
        'meta': {
            'ailment': {
                'name': 'burn',
                'chance': 30
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'snarl': {
        'id': 555,
        'name': 'Snarl',
        'type': 'dark',
        'category': 'special',
        'power': 55,
        'pp': 15,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  Has a $effect_chance% chance to lower the target's Special Attack by one stage.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'special-attack',
                    'url': 'https://pokeapi.co/api/v2/stat/4/'
                }
            }]
        }
    },
    'icicle-crash': {
        'id': 556,
        'name': 'Icicle-Crash',
        'type': 'ice',
        'category': 'physical',
        'power': 85,
        'pp': 10,
        'accuracy': 90,
        'priority': 0,
        'description': 'Inflicts regular damage.  Has a $effect_chance% chance to make the target flinch.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 30,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'v-create': {
        'id': 557,
        'name': 'V-Create',
        'type': 'fire',
        'category': 'physical',
        'power': 180,
        'pp': 5,
        'accuracy': 95,
        'priority': 0,
        'description': "Inflicts regular damage.  Lowers the user's Defense, Special Defense, and Speed by one stage each.",
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 100,
            'stat_changes': [{
                'change': -1,
                'stat': {
                    'name': 'defense',
                    'url': 'https://pokeapi.co/api/v2/stat/3/'
                }
            }, {
                'change': -1,
                'stat': {
                    'name': 'special-defense',
                    'url': 'https://pokeapi.co/api/v2/stat/5/'
                }
            }, {
                'change': -1,
                'stat': {
                    'name': 'speed',
                    'url': 'https://pokeapi.co/api/v2/stat/6/'
                }
            }]
        }
    },
    'fusion-flare': {
        'id': 558,
        'name': 'Fusion-Flare',
        'type': 'fire',
        'category': 'special',
        'power': 100,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If a friendly Pokémon used fusion bolt earlier this turn, this move has double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    },
    'fusion-bolt': {
        'id': 559,
        'name': 'Fusion-Bolt',
        'type': 'electric',
        'category': 'physical',
        'power': 100,
        'pp': 5,
        'accuracy': 100,
        'priority': 0,
        'description': 'Inflicts regular damage.  If a friendly Pokémon used fusion flare earlier this turn, this move has double power.',
        'meta': {
            'ailment': {
                'name': 'none',
                'chance': 0
            },
            'crit_rate': 0,
            'drain': 0,
            'flinch_chance': 0,
            'healing': 0,
            'max_hits': None,
            'max_turns': None,
            'min_hits': None,
            'min_turns': None,
            'stat_chance': 0,
            'stat_changes': []
        }
    }
}