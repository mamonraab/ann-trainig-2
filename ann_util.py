import math
import random

def sigmoid(x):
    return 1.0 / (1 + math.exp(-x))

def deriv_sigmoid(x):
    sgmd  = sigmoid(x)
    return (1 - sgmd) * sgmd
def between(min,max):
    """
    retrun real random value between min and max
    """
    return random.random() * (max - min) + min


def make_matrix(n , m):
    """
    make an N rows by M columns matrix
    """
    return [[0 for i in range(m)] for i in range(n)]
