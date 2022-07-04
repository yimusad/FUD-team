## Title: How to Create a Food Website with an API
## Author: RapidAPI staff
## Date: 2020
## Code version: n/a
## https://spoonacular.com/food-api


from flask import Flask, render_template, request
import requests
app = Flask(__name__)

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

headers = {
  'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
  'x-rapidapi-key': "618623e3a9msh2bde9f08f506715p10d82ejsn767640c583f9",
  }

random_recipe = "food/jokes/random"
find = "recipes/findByIngredients"


# landing page 
@app.route('/')
def search_page(): #endpoint
  search_response = str(requests.request("GET", url + random_recipe, headers=headers).json()['text'])
  return render_template('search.html', recipe=search_response)


@app.route('/recipes')
def get_recipes():  # has two different endpoints 
  querystring = {"number":"10","ranking":"1","ignorePantry":"false","ingredients":request.args['ingridients']}
  response = requests.request("GET", url + find,headers=headers, params=querystring).json()
  return render_template('recipes.html', recipes=response)

# display cooking instructions, serving size, ingredients to use
@app.route('/recipe')
def get_recipe():
  recipe_id = request.args['id']
  recipe_info_endpoint = "recipes/{0}/information".format(recipe_id)
  ingredientsWidget = "recipes/{0}/ingredientWidget".format(recipe_id)

  recipe_info = requests.request("GET", url + recipe_info_endpoint, headers=headers).json()
    
  recipe_headers = {
      'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
      'x-rapidapi-key': "618623e3a9msh2bde9f08f506715p10d82ejsn767640c583f9", 
      'accept': "text/html"
  }
  querystring = {"defaultCss":"true", "showBacklink":"false"}

  recipe_info['inregdientsWidget'] = requests.request("GET", url + ingredientsWidget, headers=recipe_headers, params=querystring).text
  
    
  return render_template('recipe.html', recipe=recipe_info)


if __name__ == '__main__':
  app.run()