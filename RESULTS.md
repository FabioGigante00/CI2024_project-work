1)
crossover = recombination_crossover
favorite_mutation = random_mutation # random_mutation(), point_mutation, subtree_mutation, expansion_mutation, permutation_mutation, collaps_mutation, hoist_mutation
OFFSPRING_SIZE = 200
POPULATION_SIZE = 40
OUTSIDER_SIZE = math.ceil(OFFSPRING_SIZE*0.1)
pm = 0.05
x_elitism = 0.08
MAX_GENERATIONS = 40
HEIGHT = 5
PC = 0.1
P_PICK_CONSTANT = 0.4
P_CUT_TREE = 0.05

final_fitness = 2171349835.3408346