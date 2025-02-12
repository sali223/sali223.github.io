from flask import Flask, render_template

app = Flask(__name__)


recipes = [
    {
        'name': 'Spaghetti Bolognese',
        'category': 'Italian',
        'ingredients': ['spaghetti', 'ground beef', 'tomato sauce', 'onions', 'garlic'],
        'instructions': 'Cook pasta, brown beef, mix with sauce, and simmer.'
    },
    {
        'name': 'Tacos',
        'category': 'Mexican',
        'ingredients': ['taco shells', 'ground beef', 'lettuce', 'cheese', 'salsa'],
        'instructions': 'Cook beef, assemble tacos with toppings.'
    },
    {
        'name': 'Sushi Rolls',
        'category': 'Japanese',
        'ingredients': ['sushi rice', 'seaweed', 'salmon', 'avocado', 'soy sauce'],
        'instructions': 'Roll rice, fish, and veggies in seaweed.'
    }
]


@app.route('/')
def home():
    return render_template('index.html', recipes=recipes)


@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe = recipes[recipe_id]
    return render_template('recipe.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)
