#!/usr/bin/python3
""" hey """
from sys import argv

dest = "passords.txt"
count = 0

with open(argv[1]) as f:
    lines = f.readlines()
    with open(dest, 'w') as d:
        for line in lines:
            if len(line) == 12:
                d.write(line)
                count += 1
print(count)
