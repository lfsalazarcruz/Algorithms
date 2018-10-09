#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  added_recipes = []
  min_value = 0
  for k, k2 in zip(recipe, ingredients):
    if set(recipe.keys()) != set(ingredients.keys()):
      added_recipes = 0
    else:
      batches = ingredients[k2] // recipe[k]
      added_recipes.append(batches)
      min_value = min(added_recipes)
  return min_value
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))