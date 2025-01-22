import numpy as np
import s328890

if __name__ == '__main__':
    # > Setup
    problem = np.load('data/problem_1.npz')
    input = problem['x']
    labels = problem['y']
    terminal_list = ['x' + str(i) for i in range(input.shape[0])]
    # < Setup
    # > Test
    print(f"MSE (train): {100*np.square(labels-s328890.f1(input).sum()/len(labels)):g}")
    # < Test
   
