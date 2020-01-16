#!/usr/bin/env python

import glob
import numpy as np

def list_file_names(globber):
    ''' With given expression returns list of files in current dir.
    '''
    return glob.glob(globber)


def get_file_name(globber):
    ''' Prints list of files with given expression in the filename.
        Lets user select one and returns that filename.
    '''
    files = list_file_names(globber)
    files.sort()
    for i in range(len(files)):
        print("{:>3}) {}".format(i, files[i]))
    filenmr = input("Kies een file: ")
    try:
        number = int(filenmr)
    except ValueError:
        print("This was not an integer. Default of 0 is used.")
        number = 0
    return files[number]


def _get_walls(content, line_choice, field_choice):
    ''' With given line and field ranges finds specific
        fields in content array.
        Returns 2D list.
    '''
    these_walls = []
    for i in line_choice:
        this_line = []
        for j in field_choice:
            this_line.append(content[i][j])
        these_walls.append(this_line)
    return these_walls


def _merge_ver_and_hor(ver_walls, hor_walls):
    ''' Dimension of hor_walls is always dimenson of ver_walls + 1.
        Returns 1D list with all walls from left-top to right-bottom.
    '''
    all_walls = []
    for i in range(len(ver_walls)):
        all_walls += hor_walls[i]
        all_walls += ver_walls[i]
    all_walls += hor_walls[-1]
    return all_walls


def translate_walls_to_01s(my_list):
    ''' List of walls should be 1's and 0's.
    '''
    binary_walls = []
    for i in my_list:
        if i == ' ':
            binary_walls += 0
        else:
            binary_walls += 1
    return binary_walls


def get_walls_and_rooms(content):
    ''' Finds all the walls and rooms in content array.
    Returns 2 arrays for the walls and rooms.
    '''
    ver_wall_lines = range(1, len(content), 2)
    hor_wall_lines = range(0, len(content), 2)

    vertical_walls, horizontal_walls, rooms = [], [], []

    horizontal_walls = _get_walls(content, hor_wall_lines, ver_wall_lines)
    vertical_walls = _get_walls(content, ver_wall_lines, hor_wall_lines)
    all_walls = _merge_ver_and_hor(vertical_walls, horizontal_walls)
    rooms = _get_walls(content, ver_wall_lines, ver_wall_lines)
    return all_walls, rooms


def find_walls_per_room(dimension):
    ''' Every room has 4 walls. Calculates for given dimension which walls
        are around each room. For each room shows 0's for no wall and 1's
        for a wall.
    '''
    DIM = int((dimension + 1) / 2)
    aant_kamers = (DIM - 1) * (DIM - 1)
    gen_length = 2 * DIM * (DIM - 1)
    walls_for_rooms = []
    for teller in range(aant_kamers):
        regel = np.zeros(gen_length, dtype = int)
        mymod, rest = divmod(teller, DIM - 1)
        first_one = mymod * (2 * DIM - 1) + rest
        regel[first_one] = 1
        regel[first_one + DIM] = 1
        regel[first_one + DIM - 1] = 1
        regel[first_one + DIM + DIM - 1] = 1
        walls_for_rooms.append(regel)
    return walls_for_rooms


def find_index_all_ones(my_list):
    ''' Finds indices of all the 1's in a list.
    '''
    indices = [i for i, x in enumerate(my_list) if x == 1]
    return indices


def wall_indices_per_room(dimension):
    ''' Per room calculates which indices of the walls-list belong
        to that room. So calculats which walls belong to each room.
        Returns list with list of 4 indices for each room.
    '''
    all_walls_per_room = find_walls_per_room(dimension)
    indices_per_room = []
    for line in all_walls_per_room:
        these_indices = find_index_all_ones(line)
        indices_per_room.append(these_indices)
    return indices_per_room

