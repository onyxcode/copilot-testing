# randomly generate a hex color
def randomcolor():
    import random
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    print("#%02x%02x%02x" % (r, g, b))

# run the main function
if __name__ == "__main__":
    randomcolor()