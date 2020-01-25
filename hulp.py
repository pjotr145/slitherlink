#!/usr/bin/env python
''' Some helpfull functions.
'''

import glob
import numpy as np
from itertools import islice


def list_file_names(globber):
    ''' With given expression returns list of files.
        With ** this function searches recursively.
    '''
    return glob.glob('**/' + globber)


def get_file_name(globber):
    ''' Prints list of files with given expression in the filename.
        Lets user select one and returns that filename.
    '''
    files = list_file_names(globber)
    files.sort()
    for idx, val in enumerate(files):
        print("{:>3}) {}".format(idx, val))
#    for i in range(len(files)):
#        print("{:>3}) {}".format(i, files[i]))
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
#    for i in range(len(ver_walls)):
    for i, _ in enumerate(ver_walls):
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


def walls_to_01s(list_of_walls):
    ''' Walls are spaces, -'s or |'s. These are "0" for spaces
        and "1" fore the - or |.
    '''
    the_walls = []
    for i in list_of_walls:
        if i == ' ':
            the_walls += [0]
        else:
            the_walls += [1]
    return np.array(the_walls)


def rooms_to_1d(list_of_rooms):
    ''' Flatten the 2D lists of rooms to a 1D list.
    '''
    return [x for sublist in list_of_rooms for x in sublist]


def rooms_to_integers(list_of_rooms):
    ''' Converts empty rooms to 9 and rooms with values to integers.
    '''
    all_rooms = []
    for i in list_of_rooms:
        if i == ' ':
            all_rooms += [9]
        else:
            all_rooms += [int(i)]
    return all_rooms


def get_walls_and_rooms(content):
    ''' Finds all the walls and rooms in content array.
        Returns 2 arrays for the walls and rooms.
    '''
    ver_wall_lines = range(1, len(content), 2)
    hor_wall_lines = range(0, len(content), 2)

    vertical_walls, horizontal_walls, rooms = [], [], []

    horizontal_walls = _get_walls(content, hor_wall_lines, ver_wall_lines)
    vertical_walls = _get_walls(content, ver_wall_lines, hor_wall_lines)
    walls = _merge_ver_and_hor(vertical_walls, horizontal_walls)
    all_walls = walls_to_01s(walls)
    rooms = _get_walls(content, ver_wall_lines, ver_wall_lines)
    rooms = rooms_to_1d(rooms)
    rooms = rooms_to_integers(rooms)
    return all_walls, rooms


def find_walls_per_room(dimension):
    ''' Every room has 4 walls. Calculates for given dimension which walls
        are around each room. For each room shows 0's for no wall and 1's
        for a wall.
    '''
    dim = int((dimension + 1) / 2)
    aant_kamers = (dim - 1) * (dim - 1)
    gen_length = 2 * dim * (dim - 1)
    walls_for_rooms = []
    for teller in range(aant_kamers):
        regel = np.zeros(gen_length, dtype=int)
        mymod, rest = divmod(teller, dim - 1)
        first_one = mymod * (2 * dim - 1) + rest
        regel[first_one] = 1
        regel[first_one + dim] = 1
        regel[first_one + dim - 1] = 1
        regel[first_one + dim + dim - 1] = 1
        walls_for_rooms.append(regel)
    return walls_for_rooms


def find_index_all_ones(my_list):
    ''' Finds indices of all the 1's in a list.
    '''
    return [i for i, x in enumerate(my_list) if x == 1]


def find_index_no_nine(my_list):
    ''' Finds indices for all fields that are not nine.
        These are the rooms that have a value in the puzzle.
        A 9 means no-value in the puzzle.
    '''
    return [i for i, x in enumerate(my_list) if x != 9]


def get_wall_indices_per_room(dimension):
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


def _chunks(this_list, chunk_size):
    ''' Splits a list into chunk_size chunks.
        If list length is not n*chunk_size then last chunk will be smaller.
        Returns a generator
    '''
    for i in range(0, len(this_list), chunk_size):
        yield this_list[i:i+chunk_size]


def printable_rooms(dimension, rooms):
    ''' All the rooms are integers but printing needs strings.
        Also the empty rooms are shown as 9's but should be spaces.
    '''
    dimension = int((dimension - 1) / 2)
    rooms_to_print = []
    for i in rooms:
        if i == 9:
            rooms_to_print.append(' ')
        else:
            rooms_to_print.append(str(i))
    return list(_chunks(rooms_to_print, dimension))


def _create_split_list(dim):
    ''' Creates list alternating dim and dim + 1 and adds another dim.
        example dim=2 => [2, 3, 2, 3, 2]
    '''
    split_list = []
    for i in range(dim):
        split_list += [dim, dim + 1]
    split_list += [dim]
    return split_list


def split_gene_into_puzzle(dimension, gene):
    it = iter(gene)
    split_list = _create_split_list(dimension)
    return [list(islice(it, i)) for i in split_list]
