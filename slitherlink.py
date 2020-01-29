#!/usr/bin/env python

import yaml
import gui
from hulp import get_file_name, get_walls_and_rooms
from hulp import get_wall_indices_per_room, find_index_no_nine
from hulp import find_index_all_ones, printable_rooms, split_gene_into_puzzle
from population import Population
from dot import get_dots_wall_indices

FILE_EXPR = "puzzle*.txt"
SETTINGS_FILE = "settings.yaml"

# Read the initial settings for the GA
with open(SETTINGS_FILE) as f:
    SETTINGS = yaml.load(f, Loader=yaml.FullLoader)

# Read the puzzle
filename = get_file_name(FILE_EXPR)
#filename = "puzzles/puzzle-20181212.txt"
with open(filename) as f:
    content = f.read().splitlines()

all_walls, all_rooms = get_walls_and_rooms(content)
gene_length = len(all_walls)
all_walls_index = find_index_all_ones(all_walls)
wall_index_per_room = get_wall_indices_per_room(len(content))
room_with_value_index = find_index_no_nine(all_rooms)
rooms_to_print = printable_rooms(len(content), all_rooms)
dot_wall_indices = get_dots_wall_indices(int((len(content) + 1) / 2))

#for idx, val in enumerate(content):
#    print("{:>3})  {}".format(idx, val))
#
#print("len rooms      : {}".format(len(all_rooms)))
#print("len walls      : {}".format(len(all_walls)))
#print("len walls w val: {}".format(len(room_with_value_index)))
#print("R-val: {}".format(room_with_value_index))
#print("Rooms: {}".format(all_rooms))
#print("Walls: {}".format(all_walls))
#print("Print: {}".format(rooms_to_print))
#print("Walls: {}".format(wall_index_per_room))

frame = gui.Window()
print(frame.winfo_screenheight())
frame.geometry("{}x{}+{}+0".format(frame.winfo_screenheight(),
                                   frame.winfo_screenheight(),
                                   int(frame.winfo_screenwidth()/2)))
frame.update()
print(frame.winfo_screenheight())
frame.set_schermhoogte(frame.winfo_screenheight())
population = Population(gene_length,
                        all_walls_index,
                        all_rooms,
                        wall_index_per_room,
                        room_with_value_index,
                        dot_wall_indices,
                        SETTINGS)
population.calc_fitnesses()
population.sort_pop_on_fitness()
#print("Generatie: {:>3} -> Fittest ind: {}".format(0, population.pop[0].fitness))
print("Generatie: {:>3} -> Fittest ind: {:>3} -> worst: {:>3}".format(0,
                                                                      population.pop[0].fitness,
                                                                      population.pop[-1].fitness))
#frame.teken_puzzle(int((len(content) + 1) / 2), population.pop[0].gene)
gene_to_print = split_gene_into_puzzle(9, population.pop[0].gene)
frame.setWaardes(rooms_to_print, gene_to_print)

#print("Walls: {}".format(all_walls))
#print("Walls: {}".format(find_index_all_ones(all_walls)))
for generation_count in range(1, 1 + SETTINGS["aant_generaties"]):
#    population.get_new_pop_superras()
    population.get_new_pop_elitism()
    # TODO: still needs mutation of the new genes
    population.calc_fitnesses()
    population.sort_pop_on_fitness()
    gene_to_print = split_gene_into_puzzle(9, population.pop[0].gene)
    frame.setWaardes(rooms_to_print, gene_to_print)
    frame.update()
    print("Generatie: {:>3} -> Fittest ind: {:>3} -> worst: {:>3}".format(generation_count,
                                                       population.pop[0].fitness,
                                                       population.pop[-1].fitness))
print("Einde!")
frame.mainloop()
