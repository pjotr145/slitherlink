#!/usr/bin/env python
''' Most basic test of puzzle-files.
    Just checks nmr of lines and number of chars per line.
'''

from hulp import get_file_name

FILE_EXPR = 'puzzle*.txt'

filename = get_file_name(FILE_EXPR)

with open(filename) as f:
    lines = f.read().splitlines()

print("\nEr zijn {} regels tekst.".format(len(lines)))

for line in lines:
    print("{:>3}) {}".format(len(line), line))
