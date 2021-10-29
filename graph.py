# generate a random slope and intercept graph and save it as a png
def main():
    import matplotlib.pyplot as plt
    import numpy as np
    import random
    x = np.arange(-10, 10, 0.1)
    y = x * random.uniform(0, 10) + random.uniform(-10, 10)
    plt.plot(x, y)
    plt.savefig('graph.png')
    plt.show()

# run the main function
if __name__ == '__main__':
    main()