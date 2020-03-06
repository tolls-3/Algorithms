#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  lowVal = 0
  for k in recipe:
    #print(k, v)
    if k in ingredients:
      ing = ingredients[k]
      x = int(ing)//int(recipe[k])
      #print('i am x',x)
      if lowVal == 0 or x < lowVal:
        lowVal = x
    else:
      return 0
  return lowVal or 0



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))