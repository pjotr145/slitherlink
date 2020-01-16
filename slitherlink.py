#!/usr/bin/env python

#from hulp import get_file_name, get_walls_and_rooms
from hulp import *

FILE_EXPR = "puzzle*.txt"

filename = get_file_name(FILE_EXPR)

with open(filename) as f:
    content = f.read().splitlines()

for i in range(len(content)):
    print("{:>3})  {}".format(i, content[i]))

all_walls, rooms = get_walls_and_rooms(content)

print("rooms: {}".format(len(rooms)))
print("alle : {}".format(len(all_walls)))

for i in rooms:
    print("N) {}".format(i))
print(all_walls)

wall_index_per_room = wall_indices_per_room(len(content))

print(wall_index_per_room)
