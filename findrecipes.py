# find me a recipe for an omellete and print the link
def main():
    # get the ingredients from the user
    ingredients = input("Enter ingredients separated by commas: ").split(",")
    # remove any blanks
    ingredients = [ingredient.strip() for ingredient in ingredients]
    # convert to lowercase
    ingredients = [ingredient.lower() for ingredient in ingredients]
    # get the recipe
    recipe = get_recipe(ingredients)
    # print the recipe
    print(recipe)