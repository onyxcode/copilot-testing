# find every binary in /bin and /sbin and create a json file
# with the name of the binary and the path to it
def binary_list():
    import os
    import json
    import sys
    import re
    import subprocess
    # create a list of all the binaries in /bin and /sbin
    bin_list = []
    for root, dirs, files in os.walk('/bin'):
        for file in files:
            bin_list.append(os.path.join(root, file))
    for root, dirs, files in os.walk('/sbin'):
        for file in files:
            bin_list.append(os.path.join(root, file))
    # create a list of all the binaries in /usr/bin and /usr/sbin
    for root, dirs, files in os.walk('/usr/bin'):
        for file in files:
            bin_list.append(os.path.join(root, file))
    for root, dirs, files in os.walk('/usr/sbin'):
        for file in files:
            bin_list.append(os.path.join(root, file))
    # create a list of all the binaries in /usr/local/bin and /usr/local/sbin
    for root, dirs, files in os.walk('/usr/local/bin'):
        for file in files:
            bin_list.append(os.path.join(root, file))
    for root, dirs, files in os.walk('/usr/local/sbin'):
        for file in files:
            bin_list.append(os.path.join(root, file))
    # print the list of binaries
    print(bin_list)

# run the binary_list function
binary_list()