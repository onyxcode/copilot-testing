# find the current screen resolution and display it
def main():
    import os
    import sys
    import subprocess
    # get the current screen resolution
    output = subprocess.check_output(['xrandr'])
    # find the current screen resolution
    resolution = output.decode('utf-8').split('\n')[0].split()[0]
    # print the current screen resolution
    print(resolution)
    # save the current screen resolution to a file
    with open('resolution.txt', 'w') as f:
        f.write(resolution)
    # change the resolution to the saved resolution
    os.system('xrandr --output eDP1 --mode ' + resolution)
# seems a bit dangerous to run this as a script
if __name__ == '__main__':
    main()
