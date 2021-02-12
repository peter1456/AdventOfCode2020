from utils import read_split_line_input
from itertools import chain
import numpy as np
from networkx import Graph
from networkx.algorithms import bipartite

input_list = read_split_line_input(21)

def parse_food(food):
    ingredients, allergens = food.split(" (contains ")
    ingredients = ingredients.split(" ")
    allergens = allergens[:-1].split(", ")
    return ingredients, allergens

ingredients_matrix, allergens_matrix = zip(*(parse_food(line) for line in input_list))
ingredients_mapping = {val: idx for idx, val in enumerate(set(chain.from_iterable(ingredients_matrix)))}
allergens_mapping = {val: idx for idx, val in enumerate(set(chain.from_iterable(allergens_matrix)))}

ingredients_bin_mat = np.zeros((len(ingredients_matrix), len(ingredients_mapping)), dtype=np.int8)
allergens_bin_mat = np.zeros((len(allergens_matrix), len(allergens_mapping)), dtype=np.int8)
possible_ingredients_bin_mat = np.zeros((len(allergens_mapping), len(ingredients_mapping)), dtype=np.int8)

for idx, food in enumerate(ingredients_matrix):
    ingredients_mapped = [ingredients_mapping[ingredient] for ingredient in food]
    ingredients_bin_mat[idx,ingredients_mapped] = 1

for idx, allergens in enumerate(allergens_matrix):
    allergens_mapped = [allergens_mapping[allergen] for allergen in allergens]
    allergens_bin_mat[idx,allergens_mapped] = 1

for i in range(len(allergens_mapping)):
    food_count = allergens_bin_mat[:,i].sum()
    possible_ingredients_bin_mat[i,:] = (ingredients_bin_mat * allergens_bin_mat[:,i].reshape((-1,1))).sum(axis=0) == food_count

ingredients_with_allergen = np.argwhere(possible_ingredients_bin_mat.sum(axis=0) != 0).flatten()

allergen_ingredient_matching = Graph()
allergen_ingredient_matching.add_nodes_from(allergens_mapping.keys(), bipartite=0)
allergen_ingredient_matching.add_nodes_from([ingredient for idx, ingredient in ingredients_mapping.items() if idx in ingredients_with_allergen], bipartite=1)

def reverse_lookup(val, dictionary):
    return next(key for key, value in dictionary.items() if value == val)

for i in range(len(allergens_mapping)):
    for j in ingredients_with_allergen:
        if possible_ingredients_bin_mat[i,j] == 1:
            allergen = reverse_lookup(i, allergens_mapping)
            ingredient = reverse_lookup(j, ingredients_mapping)
            allergen_ingredient_matching.add_edge(allergen, ingredient)

matching = bipartite.matching.hopcroft_karp_matching(allergen_ingredient_matching, allergens_mapping.keys())
print(",".join([matching[allergen] for allergen in sorted(allergens_mapping.keys())]))
