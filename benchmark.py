# find the current usage of the CPU and RAM
def main():
    import psutil
    import time

    while True:
        # clear the screen
        print("\n" * 100)
        print("CPU: ", psutil.cpu_percent())
        print("RAM: ", psutil.virtual_memory().percent)
        time.sleep(1)
# run the main function
if __name__ == "__main__":
    main()