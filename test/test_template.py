import numpy as np

from operations.terminal_constants import crammed_constants
from operations.evolution import generate_random_tree

if __name__ == '__main__':
    # > Setup
    problem = np.load('problem_0.npz')
    input = problem['x']
    labels = problem['y']
    terminal_list = ['x' + str(i) for i in range(input.shape[0])]
    # < Setup

    # > Test

    # < Test
   
