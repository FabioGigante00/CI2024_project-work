""" This file contains the functions that are used to: generate, mutate, and combine the population """

import random
from typing import List
from gxgp.node import Node
from operations.operations_dict import basic_function_set, complex_function_set

def generate_random_tree(max_depth: int, pc: float, terminal_list: List[str],
                         constants: list[float] = None, pcst: float = 0.2, full_tree: bool = False) -> Node:
    """
    Generate a random symbolic expression tree.

    Mandatory Parameters
    ----------
    max_depth : int
        The maximum depth of the tree. By default, the tree is full, but this can be changed by setting full_tree to False.
    pc : float
        The probability of choosing a complex function over a basic function.
    terminal_list : List[str]
        The terminal list to choose from. Example: ['x0', 'x1', 'x2']

    Optional Parameters
    ----------
    constants : list[float], optional
        A list of constants that can be used in the tree (default is None).
    pcst : float, optional
        The probability of choosing a constant over a terminal (default is 0.2).
    full_tree : bool, optional
        Whether the tree should be full or have a 0.2 probability of stopping at each level (default is False).

    Returns
    -------
    Node
        A Node object representing the root of the tree.
    """

    # Cut the tree early with probability 0.2
    if (not full_tree and random.random() < 0.2) or max_depth == 0:  
        # If constants are provided, choose one with probability pcst
        if constants is not None and random.random() < pcst: 
            terminal = random.choice(constants) 
        # Otherwise, pick from the terminal set
        else:                                                
            terminal = random.choice(terminal_list)
        return Node(terminal)
    else:
        # Choose a complex function with probability pc
        if random.random() < pc:                       
            func = random.choice(list(complex_function_set.keys()))
            num_children = complex_function_set[func].__code__.co_argcount  # Numero di argomenti della funzione
            children = [generate_random_tree(max_depth - 1, pc, terminal_list, constants, pcst, full_tree)
                        for _ in range(num_children)]
            return Node(complex_function_set[func], children,name=func)
        # Otherwise, choose a basic function
        else:                                           
            func = random.choice(list(basic_function_set.keys()))
            num_children = basic_function_set[func].__code__.co_argcount  # Numero di argomenti della funzione
            children = [generate_random_tree(max_depth - 1, pc, terminal_list, constants, pcst, full_tree)
                        for _ in range(num_children)]
            return Node(basic_function_set[func], children,name=func)