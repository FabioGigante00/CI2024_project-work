""" This file contains the functions that are used to: generate, mutate, and combine the population """

import random
from typing import List
from gxgp.node import Node
from utils.operations_dict import basic_function_set, complex_function_set

def generate_random_tree(max_depth: int, pc: float, terminal_list: List[str],
                         constants: list[float] = None, p_pick_constant: float = 0.2, p_cut_tree: float = 0.2,
                         is_root: bool = True) -> Node:
    """
    Generate a random symbolic expression tree.

    Mandatory Parameters
    ----------
    max_depth : int
        The maximum depth of the tree.
    pc : float
        The probability of choosing a complex function over a basic function.
    terminal_list : List[str]
        The terminal list to choose from. Example: ['x0', 'x1', 'x2']

    Optional Parameters
    ----------
    constants : list[float]
        A list of constants that can be used in the tree (default is None).
    p_pick_constant : float
        The probability of choosing a constant over a terminal (default is 0.2).
    p_cut_tree : float
        The probability of cutting the tree early (default is 0.2).
    is_root : bool
        Flag to check if root, in order not to create 0-length trees

    Returns
    -------
    Node
        A Node object representing the root of the tree.
    """

    # Cut the tree early with probability 0.2
    if (not is_root and random.random() < p_cut_tree) or max_depth == 0:  
        # If constants are provided, choose one with probability p_pick_constant
        if constants is not None and random.random() < p_pick_constant: 
            terminal = random.choice(constants) 
        # Otherwise, pick from the terminal set
        else:                                                
            terminal = random.choice(terminal_list)

        # Set the depth of the node to 0
        my_node = Node(terminal)
        my_node.set_depth(0)
        return my_node
    else:
        # Choose a complex function with probability pc
        if random.random() < pc:                       
            func = random.choice(list(complex_function_set.keys()))
            num_children = complex_function_set[func].__code__.co_argcount  # Numero di argomenti della funzione
            children = [generate_random_tree(max_depth - 1, pc, terminal_list, constants, p_pick_constant, p_cut_tree, False)
                        for _ in range(num_children)]
            
            # Set depth
            cur_depth = max([child.get_depth() for child in children]) + 1
            my_node = Node(complex_function_set[func], children, name=cur_depth)
            my_node.set_depth(cur_depth)
            return my_node
        # Otherwise, choose a basic function
        else:                                           
            func = random.choice(list(basic_function_set.keys()))
            num_children = basic_function_set[func].__code__.co_argcount  # Numero di argomenti della funzione
            children = [generate_random_tree(max_depth - 1, pc, terminal_list, constants, p_pick_constant, p_cut_tree, False)
                        for _ in range(num_children)]
            # Set depth
            cur_depth = max([child.get_depth() for child in children]) + 1
            my_node = Node(basic_function_set[func], children, name=cur_depth)
            my_node.set_depth(cur_depth)
            return my_node