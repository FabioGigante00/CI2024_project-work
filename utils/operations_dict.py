import numpy as np
function_set = {
    'add': lambda x, y: np.add(x, y),
    'sub': lambda x, y: np.subtract(x, y),
    'mul': lambda x, y: np.multiply(x, y),
    'div': lambda x, y: np.divide(x, y),
    'exp': lambda x: np.exp(x),
    'sin': lambda x: np.sin(x),
    'cos': lambda x: np.cos(x),
    'neg': lambda x: np.negative(x),
    'inv': lambda x: np.reciprocal(x) if x != 0 else x,
    'sqrt': lambda x: np.sqrt(np.abs(x)),
    'log': lambda x: np.log(np.abs(x)),
    'abs': lambda x: np.abs(x),
    'pow': lambda x, y: np.power(x, y),
}
basic_function_set = {
    'add': function_set['add'],
    'sub': function_set['sub'],
    'mul': function_set['mul'],
    'div': function_set['div'],
    'abs': function_set['abs'],
    'sqrt': function_set['sqrt'],
}
complex_function_set = {
    'exp': function_set['exp'],
    'sin': function_set['sin'],
    'cos': function_set['cos'],
    'neg': function_set['neg'],
    'inv': function_set['inv'],
    'log': function_set['log'],
    'pow': function_set['pow'],
}
