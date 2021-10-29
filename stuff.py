# print all .png paths in /home/onyxia/
def findpng():
    import os
    import glob
    import sys
    import re
    import argparse
    parser = argparse.ArgumentParser(description='Find all .png files in a directory')
    parser.add_argument('-d', '--directory', help='Directory to search', required=True)
    args = parser.parse_args()
    directory = args.directory
    if not os.path.exists(directory):
        print('Directory does not exist')
        sys.exit(1)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search('.png$', file):
                print(os.path.join(root, file))

# run the function
findpng()