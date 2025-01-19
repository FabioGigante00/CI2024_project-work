import numpy as np


if __name__ == '__main__':
    # > Setup
    problem = np.load('data/problem_1.npz')
    input = problem['x']
    labels = problem['y']
    terminal_list = ['x' + str(i) for i in range(input.shape[0])]
    # < Setup
    output = np.sin(input.flatten())
    # > Test
    print(f"MSE (train): {100*np.square(labels-np.sin(input.flatten())).sum()/len(labels):g}")
    # < Test
   
