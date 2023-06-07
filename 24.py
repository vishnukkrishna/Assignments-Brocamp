pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli power": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipe = {
    "Butter Chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli power",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and Chips":[
        "chicken",
        "potatoes",
        "salt",
        "malt vineger",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg Sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on Toast": [
        "beans",
        "bread"
    ],
    "Spam a la tin": [
        "spam",
        "tIn opener",
        "spoon",
    ],
}
print(pantry)
print("------Butter Chicken items------")
for item in recipe["Butter Chicken"]:
    print(item)
    pantry[item]=1
    print("--------------Update Pantry----------------")
    print(pantry)
