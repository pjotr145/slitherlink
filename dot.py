''' Help functions to get the  proper walls for each dot.
'''

from hulp import find_index_all_ones


class Wall():
    ''' A single wall. Which can be available for a given dim puzzle or not.
        The value means it's a wall or not
    '''
    def __init__(self):
        self.available = True
        self.value = 0


class ExtraLargeGene():
    def __init__(self, dim):
        ''' Create gene of correct length
        '''
        self.dim = dim
        self.gene = []
        small = dim + 1
        large = dim + 2
        # Create gene of correct length. Should be larger dim
        for _ in range(small * (small + large) + small):
            self.gene.append(Wall())

    def set_availability(self):
        small = self.dim + 1
        large = self.dim + 2
        sum_ = small + large
        sel_range = [0, self.dim, small, self.dim + large ]
        # for dim=5 => [0, 5, 6, 12]
        for i in range(1, small, 1):
            # for dim=5 => range is 1..5
            for x in sel_range:
                self.gene[i * sum_ + x].available = False
        for i in self.gene[0:sum_]:
            i.available = False
        for i in self.gene[-1*sum_:]:
            i.available = False


class DotsWithWalls():
    def __init__(self, dim):
        self.dim = dim
        self.dot_pool = []
        self.get_walls()

    def get_walls(self):
        small = self.dim + 1
        large = self.dim + 2
        sum_ = small + large
        wall_range = [0, small, large, sum_]
        walls_for_dot = []
        for i in range(self.dim):
            offset = i * sum_
            for c in range(self.dim):
                walls_for_dot = ExtraLargeGene(self.dim)
                walls_for_dot.set_availability()
                for set_wall in wall_range:
                    index = c + large + offset + set_wall
                    walls_for_dot.gene[index].value = 1
                self.dot_pool.append(walls_for_dot)


def get_the_dots_walls(dim):
    ''' Returns a list with for each dot a list that contains all the
        walls as a zero except for the walls connected to that dot.
    '''
    stippen = DotsWithWalls(dim)
    all_dots = []
    for i in stippen.dot_pool:
        one_dot = []
        for j in i.gene:
            if j.available == True:
                one_dot.append(j.value)
        all_dots.append(one_dot)
    return all_dots

def get_dots_wall_indices(dim):
    ''' For each dot lists the indices of the walls that connect to the dot
    '''
    dot_wall_indexes = []
    all_dots = get_the_dots_walls(dim)
    for dot in all_dots:
        dot_wall_indexes.append(find_index_all_ones(dot))
    return dot_wall_indexes

