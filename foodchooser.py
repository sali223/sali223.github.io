import random

def food_chooser():
    # List of food items
    food_list = [
        "Pizza", "Burger", "Sushi", "Pasta", "Salad", 
        "Tacos", "Sandwich", "Steak", "Soup", "Ice Cream"
    ]
    
    # Randomly choose a food item
    chosen_food = random.choice(food_list)
    
    print("You should have:", chosen_food)

# Run the function
food_chooser()
