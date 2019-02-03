import matplotlib.pyplot as plt
import itertools
import unittest

def touching_chance(attack_bonus, ac):
    posssibilities_of_beating_ac = attack_bonus-ac+21
    return max(min(posssibilities_of_beating_ac, 19), 1)/20

def chance_of_n_hits(attack_chances, ac):
    number_of_attacks = len(attack_chances)
    result_proba = []
    proba_n_attack_hit_before = []
    proba_to_be_nth_success = [[0 for i in range(number_of_attacks)] for j in range(number_of_attacks)]
    for number_of_success in range(number_of_attacks+1):
        subsets = itertools.combinations(range(number_of_attacks), number_of_success)
        proba_all_combination_of_size_n = 0
        for subset in subsets:
            proba_this_subset = 1
            for element in subset:
                proba_this_subset*=attack_chances[element]
            for element in set(set(range(len(attack_chances))) - set(subset)):
                proba_this_subset*=(1-attack_chances[element])

            for i in range(len(subset)):
                proba_to_be_nth_success[subset[i]][i] +=proba_this_subset
            proba_all_combination_of_size_n += proba_this_subset

        result_proba.append(proba_all_combination_of_size_n)
    return result_proba, proba_to_be_nth_success


def proba_specific_outcome(subset):
    pass



def hammer_the_gap_bonus(attacks, ac):
    probas_n_hits, proba_to_be_nth_attack = chance_of_n_hits(attac_chance, ac)
    total_damage_bonus = 0
    current_bonus = 0
    for i in range(len(proba)):
        current_bonus+=i
        total_damage_bonus+=current_bonus*proba[i]
    return total_damage_bonus


def dmg(ac, attacks, damages, is_hammer_the_gap):
    result = 0
    for attack, damage in zip(attacks, damages):
        result += touching_chance(attack, ac)*damage
    return result
