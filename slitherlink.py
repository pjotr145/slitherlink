#!/usr/bin/env python

import yaml
from hulp import get_file_name, get_walls_and_rooms
from hulp import get_wall_indices_per_room, find_index_no_nine
from hulp import find_index_all_ones
from population import Population

FILE_EXPR = "puzzle*.txt"
SETTINGS_FILE = "settings.yaml"

# Read the initial settings for the GA
with open(SETTINGS_FILE) as f:
    SETTINGS = yaml.load(f, Loader=yaml.FullLoader)

# Read the puzzle
filename = get_file_name(FILE_EXPR)
with open(filename) as f:
    content = f.read().splitlines()

all_walls, all_rooms = get_walls_and_rooms(content)
wall_index_per_room = get_wall_indices_per_room(len(content))
room_with_value_index = find_index_no_nine(all_rooms)

#for idx, val in enumerate(content):
#    print("{:>3})  {}".format(idx, val))
#
#print("len rooms      : {}".format(len(all_rooms)))
#print("len walls      : {}".format(len(all_walls)))
#print("len walls w val: {}".format(len(room_with_value_index)))
#print("R-val: {}".format(room_with_value_index))
#print("Rooms: {}".format(all_rooms))
#print("Walls: {}".format(all_walls))
#print("Walls: {}".format(wall_index_per_room))

population = Population(all_walls, all_rooms, wall_index_per_room,
                        room_with_value_index, SETTINGS)
print("Walls: {}".format(all_walls))
print("Walls: {}".format(find_index_all_ones(all_walls)))
