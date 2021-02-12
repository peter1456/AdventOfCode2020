from utils import read_split_line_input
from itertools import chain
import numpy as np

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

ingredients_no_allergen = np.argwhere(possible_ingredients_bin_mat.sum(axis=0) == 0).flatten()
print(ingredients_bin_mat[:,ingredients_no_allergen].sum())
