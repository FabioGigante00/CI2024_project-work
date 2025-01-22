import numpy as np


# ============== Functions =============== #
def my_sqrt(x: np.ndarray) -> np.ndarray:
    return np.sqrt(np.abs(x))

def my_log(x: np.ndarray) -> np.ndarray:
    return np.log(np.abs(x))

def my_reciprocal(x: np.ndarray) -> np.ndarray:
    if not isinstance(x, np.ndarray):
        if x == 0:
            return 0
        else:
            return np.reciprocal(x)
        
    out = []
    for el in x:
        if el == 0:
            out.append(el)
        else:
            out.append(np.reciprocal(el))
    return np.array(out)

def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray:
    # Leo
    return np.multiply(np.add(np.add(np.multiply(x[0], 112.933), np.multiply(19, x[2])), np.multiply(19, x[1])), 1e4)
def f3(x: np.ndarray) -> np.ndarray:
    # Dragos
    return np.subtract(np.multiply(np.multiply(my_sqrt(np.add(np.abs(np.divide(np.subtract(np.subtract(-3, np.multiply(np.subtract(np.divide(x[2], 1), 14), np.divide(x[1], x[1]))), np.multiply(my_sqrt(np.add(np.abs(np.divide(np.subtract(np.subtract(-3, np.multiply(np.subtract(np.divide(x[2], 1), 14), np.divide(x[1], x[1]))), np.multiply(np.subtract(np.abs(np.abs(x[0])), -0.333333), np.subtract(np.abs(x[0]), -0.333333))), my_sqrt(x[0]))), 14)), np.subtract(np.abs(np.abs(np.subtract(np.abs(np.abs(x[0])), -0.333333))), my_reciprocal(np.subtract(-3, np.divide(x[1], x[1])))))), my_sqrt(x[0]))), np.abs(np.divide(np.abs(np.subtract(np.divide(x[2], 1), 14)), np.divide(x[1], x[1]))))), np.subtract(np.abs(np.abs(x[0])), my_reciprocal(np.subtract(-3, my_sqrt(np.multiply(np.abs(np.add(np.add(np.abs(np.abs(np.divide(np.abs(x[0]), x[0]))), 3.4641), x[2])), 9)))))), my_sqrt(x[0])), np.subtract(np.add(np.add(np.abs(np.subtract(-3, np.add(x[2], 1))), np.subtract(np.add(np.add(np.divide(x[1], x[1]), np.multiply(np.multiply(x[1], np.multiply(np.abs(x[1]), np.subtract(np.abs(x[1]), np.divide(np.divide(np.abs(np.divide(2.66667, x[1])), 18), x[1])))), np.divide(x[1], x[1]))), x[2]), my_sqrt(my_sqrt(np.divide(np.subtract(np.subtract(-3, np.multiply(np.subtract(np.divide(np.subtract(np.divide(np.subtract(-3, my_sqrt(my_sqrt(x[0]))), 1), 14), 1), np.subtract(1, my_reciprocal(np.subtract(-3, my_sqrt(np.abs(np.abs(np.divide(4, x[0])))))))), np.divide(x[1], x[1]))), np.multiply(4, np.abs(np.subtract(np.subtract(-3, np.multiply(np.subtract(np.divide(np.subtract(my_sqrt(x[0]), x[2]), 1), 14), np.divide(x[1], x[1]))), np.multiply(4, np.abs(np.divide(np.subtract(np.subtract(-3, np.multiply(np.subtract(np.divide(x[2], 1), 14), np.divide(x[1], x[1]))), np.multiply(my_sqrt(np.add(np.abs(np.add(my_sqrt(x[0]), 1)), np.abs(np.divide(17, np.divide(x[1], x[1]))))), np.subtract(np.abs(np.abs(x[0])), -0.333333))), my_sqrt(x[0])))))))), my_sqrt(my_reciprocal(np.subtract(np.subtract(my_sqrt(x[0]), x[2]), -3)))))))), x[2]), 3.4641))# Resulting fitness

def f4(x: np.ndarray) -> np.ndarray:
    # Dragos
    return my_log(np.multiply(np.multiply(np.multiply(np.exp(np.exp(np.cos(x[1]))), np.multiply(np.exp(np.cos(np.abs(x[1]))), np.add(np.cos(np.abs(x[1])), my_sqrt(my_sqrt(np.exp(np.cos(np.exp(np.cos(x[1]))))))))), np.abs(my_sqrt(np.sin(np.exp(np.cos(np.exp(np.cos(x[1])))))))), np.abs(np.multiply(np.exp(np.cos(np.abs(x[1]))), np.multiply(np.multiply(np.multiply(my_sqrt(x[1]), np.exp(np.cos(x[1]))), np.exp(np.exp(np.cos(x[1])))), np.divide(np.exp(np.add(my_sqrt(my_sqrt(my_sqrt(my_sqrt(x[1])))), np.cos(x[1]))), my_sqrt(x[1])))))))# Resulting fitness

def f5(x: np.ndarray) -> np.ndarray:
    # Dragos
    # Use the new one when it's done, it's much better than e-18
    return np.multiply(np.subtract(np.divide(np.subtract(np.power(x[0], x[1]), 19), np.add(my_sqrt(np.multiply(-19.4744, x[1])), np.subtract(np.sin(np.subtract(x[1], np.sin(np.divide(x[0], my_sqrt(np.multiply(19, x[0])))))), 19))), my_sqrt(np.divide(np.divide(np.subtract(np.power(x[1], x[0]), x[1]), np.add(np.add(np.sin(np.cos(my_sqrt(np.abs(np.multiply(np.multiply(19, x[1]), x[1]))))), np.subtract(x[1], 19)), my_sqrt(np.multiply(19, x[0])))), np.add(18, np.sin(np.divide(x[0], np.add(np.subtract(np.multiply(19, x[1]), 19), 19))))))), 1e-10)# Resulting Fitness

def f6(x: np.ndarray) -> np.ndarray:
    return np.add(x[1], np.subtract(np.divide(np.add(np.add(x[1], x[1]), np.subtract(x[1], np.subtract(np.divide(np.add(x[1], np.subtract(np.divide(np.add(np.add(x[1], x[0]), np.subtract(np.add(x[1], np.subtract(x[1], np.subtract(np.divide(np.divide(np.subtract(np.multiply(np.divide(x[1], 3.4641), np.subtract(np.add(x[1], -0.48014), 0.31986)), np.subtract(np.divide(np.add(np.divide(np.add(np.add(x[1], x[1]), np.subtract(x[1], np.subtract(x[0], x[0]))), 3.4641), np.subtract(np.add(x[1], np.subtract(x[1], np.subtract(np.divide(np.divide(np.subtract(np.multiply(-0.48014, np.subtract(np.add(x[1], -0.48014), 0.31986)), x[1]), 1), 3.4641), x[0]))), np.subtract(np.divide(np.abs(np.add(x[1], np.divide(x[1], np.multiply(np.divide(4.3589, np.subtract(4.3589, x[1])), np.add(x[1], x[1]))))), 18), np.abs(np.add(x[1], np.abs(np.add(x[1], np.divide(x[1], np.multiply(np.divide(4.3589, np.subtract(4.3589, x[1])), np.add(x[1], x[1])))))))))), 3.4641), x[0])), 1), 3.4641), x[0]))), np.subtract(np.divide(np.abs(x[1]), 18), x[0]))), 3.4641), x[0])), 3.4641), x[0]))), 3.4641), x[0]))# Resulting fitness


def f7(x: np.ndarray) -> np.ndarray:
    # Fabio
    return np.multiply(my_sqrt(np.multiply(np.multiply(np.multiply(np.multiply(x[0], 13), my_sqrt(np.subtract(1.03972, np.abs(my_log(np.subtract(x[0], x[1])))))), np.add(np.divide(x[1], 8), np.abs(my_log(np.subtract(x[0], x[1]))))), my_sqrt(np.subtract(1.71699, np.abs(np.add(np.add(np.subtract(x[0], x[0]), np.abs(my_sqrt(np.subtract(np.add(np.subtract(x[0], x[0]), np.abs(my_sqrt(np.subtract(1.03972, np.abs(my_log(np.subtract(x[0], x[1]))))))), np.abs(np.abs(my_log(np.subtract(x[0], x[1])))))))), x[0])))))), np.abs(np.subtract(np.multiply(np.divide(x[1], 8), np.subtract(my_sqrt(np.subtract(np.multiply(np.divide(x[1], np.multiply(np.divide(x[1], 8), x[1])), np.subtract(np.subtract(x[1], np.subtract(np.divide(x[1], 31), np.subtract(np.subtract(x[1], x[1]), np.subtract(np.multiply(np.multiply(np.multiply(np.subtract(x[0], x[1]), x[0]), x[0]), np.abs(my_log(x[0]))), x[1])))), np.subtract(np.divide(x[1], np.multiply(np.divide(x[1], 8), x[1])), x[1]))), np.subtract(1.03972, my_log(np.subtract(x[1], x[0]))))), np.subtract(np.divide(np.subtract(np.divide(np.subtract(my_sqrt(np.abs(x[1])), np.subtract(np.abs(my_sqrt(np.subtract(1.03972, np.abs(np.divide(x[1], 8))))), x[0])), x[1]), np.subtract(np.multiply(13, np.abs(np.add(x[0], x[0]))), x[1])), 8), np.subtract(np.multiply(13, np.abs(np.add(x[0], x[1]))), np.divide(x[1], 8))))), np.multiply(np.divide(x[1], 8), np.subtract(x[0], np.subtract(np.multiply(np.multiply(np.multiply(np.divide(x[1], 8), 31), x[0]), np.abs(my_log(np.subtract(x[1], x[0])))), np.abs(x[0])))))))

def f8(x: np.ndarray) -> np.ndarray:
    # Fabio
    return np.multiply(np.multiply(9.94444, np.add(x[5], 0.841471)), np.add(np.add(np.subtract(np.multiply(x[5], np.add(x[5], x[5])), np.subtract(np.multiply(0.1, np.divide(np.add(9.94444, np.subtract(np.multiply(np.add(0.1, np.cos(np.add(np.add(0.841471, x[5]), x[5]))), np.subtract(np.multiply(x[5], np.subtract(np.multiply(np.subtract(18.9444, np.subtract(np.multiply(9.94444, np.add(x[5], 0.841471)), 9.39445)), np.add(0.841471, x[5])), np.add(x[5], 18.9444))), np.subtract(np.multiply(np.subtract(18.9444, np.subtract(np.subtract(np.multiply(9.94444, x[5]), 9.39445), 9.39445)), np.multiply(x[5], np.add(10.2359, x[5]))), np.multiply(x[5], np.add(x[5], x[5]))))), 9)), 13)), np.subtract(np.abs(np.add(np.abs(np.add(np.subtract(np.subtract(np.multiply(np.subtract(18.9444, np.subtract(np.multiply(9.94444, np.add(x[5], 0.841471)), 9.39445)), np.add(0.841471, x[5])), -9.39445), np.multiply(x[5], np.add(np.add(x[5], 0.841471), x[5]))), x[5])), -9.39445)), 9.94444))), -9.39445), -9.39445))
# =========== End of Functions =========== #