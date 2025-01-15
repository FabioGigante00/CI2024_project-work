#   *        Giovanni Squillero's GP Toolbox
#  / \       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2   +      A no-nonsense GP in pure Python
#    / \
#  10   11   Distributed under MIT License

import numbers
import random
import warnings
from typing import Callable

from .draw import draw
from .utils import arity

__all__ = ['Node']


class Node:
    _func: Callable
    _successors: tuple['Node']
    _arity: int
    _str: str
    _height: int

    def __init__(self, node=None, successors=None, *, name=None):
        if callable(node):

            def _f(*_args, **_kwargs):
                return node(*_args)
            self._height=None
            self._func = _f
            if successors is None:
                successors = tuple([])
            else:
                self._successors = tuple(successors)
            self._arity = arity(node)
            assert self._arity is None or len(tuple(successors)) == self._arity, (
                "Panic: Incorrect number of children."
                + f" Expected {len(tuple(successors))} found {arity(node)}"
            )
            self._leaf = False
            assert all(isinstance(s, Node) for s in successors), "Panic: Successors must be `Node`"
            self._successors = tuple(successors)
            if name is not None:
                self._str = name
            elif node.__name__ == '<lambda>':
                self._str = 'λ'
            else:
                self._str = node.__name__
        elif isinstance(node, numbers.Number):
            self._func = eval(f'lambda **_kw: {node}')
            self._successors = tuple()
            self._arity = 0
            self._str = f'{node:g}'
        elif isinstance(node, str):
            self._func = eval(f'lambda *, {node}, **_kw: {node}')
            self._successors = tuple()
            self._arity = 0
            self._str = str(node)
        else:
            assert False

    def __call__(self, **kwargs):
        return self._func(*[c(**kwargs) for c in self._successors], **kwargs)

    def __str__(self):
        return self.long_name

    def __len__(self):
        return 1 + sum(len(c) for c in self._successors)

    @property
    def value(self):
        return self()

    @property
    def arity(self):
        return self._arity

    @property
    def successors(self):
        return list(self._successors)

    @successors.setter
    def successors(self, new_successors):
        assert len(new_successors) == len(self._successors)
        self._successors = tuple(new_successors)

    @property
    def is_leaf(self):
        return not self._successors

    @property
    def short_name(self):
        return self._str

    @property
    def long_name(self):
        if self.is_leaf:
            return self.short_name
        else:
            return f'{self.short_name}(' + ', '.join(c.long_name for c in self._successors) + ')'

    @property
    def subtree(self):
        result = set()
        _get_subtree(result, self)
        return result

    def draw(self):
        """ 
        Draws the tree. Note that if the depth is too high, you may need to save the output figure and then zoom in using a photo viewer.
        """
        try:
            print(f"Drawing tree with height {self._height}...")
            return draw(self, self._height)
        except Exception as msg:
            warnings.warn(f"Drawing not available ({msg})", UserWarning, 2)
            return None


    """ Additions by Leonardo, Fabio, Dragos """
    def get_random_node(self):
        nodes = list(self.subtree)
        return random.choice(nodes)

    def set_height(self, height):
        self._height = height

    def get_height(self):
        return self._height
    
    def set_func(self, func, name=None):
        def _f(*_args, **_kwargs):
                return func(*_args)
        if callable(func):
            self._func = _f
            self._arity = arity(func)
            if name is not None:
                self._str = name
            elif func.__name__ == '<lambda>':
                self._str = 'λ'
            else:
                self._str = func.__name__
        elif isinstance(func, numbers.Number):
            self._func = eval(f'lambda **_kw: {func}')
            self._arity = 0
            self._str = f'{func:g}'
        elif isinstance(func, str):
            self._func = eval(f'lambda *, {func}, **_kw: {func}')
            self._arity = 0
            self._str = str(func)
        else:
            assert False

    def replace_tree(self, tree):
        self._func = tree._func
        self._successors = tree._successors
        self._arity = tree._arity
        self._str = tree._str
        self._height = tree._height
    def get_leafs(self):
        leafs = []
        for node in self.subtree:
            if node.is_leaf:
                leafs.append(node)
        return leafs
    def clone(self):
        #recursive clone of the tree
        if self.is_leaf:
            return Node(self._func, name=self._str)
        else:
            return Node(self._func, [c.clone() for c in self._successors], name=self._str)
        


def _get_subtree(bunch: set, node: Node):
    bunch.add(node)
    for c in node._successors:
        _get_subtree(bunch, c)
