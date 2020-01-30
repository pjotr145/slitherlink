''' Creating a population.
'''

import random
from individual import Individual
import numpy as np


class Population():
    ''' Defining a population. Functions to create new generations
        should go here.
    '''

    def create_one_individual(self, gene):
        ''' Creating one individual so that only a gene needs to be
            added as a parameter.
        '''
        one_individual = Individual(gene,
                                    self.gene_length,
                                    self.all_walls,
                                    self.all_rooms,
                                    self.wall_index_per_room,
                                    self.room_value_index,
                                    self.dot_wall_indices)
        return one_individual

    def __init__(self,
                 gene_length,
                 all_walls,
                 all_rooms,
                 wall_index_per_room,
                 room_value_index,
                 dot_wall_indices,
                 settings):
        ''' The initialization of a population.
        '''
        self.gene_length = gene_length
        self.all_walls = all_walls
        self.all_rooms = all_rooms
        self.wall_index_per_room = wall_index_per_room
        self.room_value_index = room_value_index
        self.dot_wall_indices = dot_wall_indices
        self.settings = settings
        print("New population")

        self.pop = []
        for _ in range(self.settings['population_size']):
            new_gene = np.random.randint(2, size=self.gene_length)
            # Make sure the walls given by the puzzle are set to 1.
            for i in self.all_walls:
                new_gene[i] = 1
#            print("Ind gene: {}".format(self.gene))
            one_individual = Individual(new_gene,
                                        self.gene_length,
                                        self.all_walls,
                                        self.all_rooms,
                                        self.wall_index_per_room,
                                        self.room_value_index,
                                        dot_wall_indices)
            self.pop.append(one_individual)
#            print("pop: indiv-nmr: {}".format(i))


    def calc_fitnesses(self):
        ''' Calculate the fitness for each indiviual in the population.
        '''
        for individual in self.pop:
            individual.calc_fitness()

    def sort_pop_on_fitness(self):
        ''' Sort the population on the individuals fitness value.
            Reverse=False so fittest (lowest fitnes value) will be first.
        '''
        self.pop.sort(key=lambda x: x.fitness, reverse=False)
#        for ind, gene in enumerate(self.pop):
#            print("ind: {:>3} has fitness: {}".format(ind, gene.fitness))

    def get_diversity(self):
        uniqueness = []
        for ind in self.pop[:self.settings['elite_size']]:
            uniqueness.append(list(ind.gene))
        return len(uniqueness)

    def get_new_pop_superras(self):
        ''' Create new generation following the Superras method.
        '''
        self.sort_pop_on_fitness()
        new_pop = self.pop[0:2]
        gene1 = new_pop[0].gene
        gene2 = new_pop[1].gene
        for _ in range(int((self.settings['population_size'] - 2) / 2)):
            split = np.random.randint(self.gene_length)
            gene_a = np.append(gene1[:split], gene2[split:])
            gene_b = np.append(gene2[:split], gene1[split:])
            new_pop.append(self.create_one_individual(gene_a))
            new_pop.append(self.create_one_individual(gene_b))
        for individual in new_pop[2:]:
            individual.mutate_gene(self.settings['mutation_rate'])
            individual.set_fixed_walls()
        self.pop = new_pop

    def get_new_pop_elitism(self):
        ''' Create a new generation following the Elitism method.
        '''
        select_pop = []
        self.sort_pop_on_fitness()
        new_pop = self.pop[0:self.settings['elite_size']]
        for i in new_pop:
            select_pop.append(i)
        for _ in range(int((self.settings['population_size'] - 2) / 2)):
            breed = random.sample(select_pop, 2)
            split = np.random.randint(self.gene_length)
#            print("Breed: {}".format(breed[0].gene))
            gene_a = np.append(breed[0].gene[:split], breed[1].gene[split:])
            gene_b = np.append(breed[1].gene[:split], breed[0].gene[split:])
            new_pop.append(self.create_one_individual(gene_a))
            new_pop.append(self.create_one_individual(gene_b))
        for individual in new_pop[self.settings['elite_size']:]:
            individual.mutate_gene(self.settings['mutation_rate'])
            individual.set_fixed_walls()
        self.pop = new_pop
