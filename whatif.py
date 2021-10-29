# create a cli coin flip game
def main():
    # set up the random module
    import random
    # set up the coin flip
    coin = random.randint(0,1)
    # set up the user input
    user_input = input("Heads or Tails? ")
    # set up the coin flip
    if coin == 0:
        coin_flip = "Heads"
    else:
        coin_flip = "Tails"
    # set up the result
    if user_input.lower() == coin_flip.lower():
        result = "You win!"
    else:
        result = "You lose!"
    # print the result
    print(result)

# run the main function
main()