from sympy import *


def system_threshold(c, g, m):
    return (g * m) / 100 + c / 2


def average(x):
    return sum(x) / len(x)


def zone_threshold(x):
    sum = 0
    l = len(x)
    ax = average(x)
    for xi in x:
        sum += (ax - xi) ** 2
    return sqrt(sum / l)


def container_threshold(x, linear,  c, g=1, m=100):
    dsys = system_threshold(c, g, m)
    if linear:
        dsys = c
    dzone = zone_threshold(x)
    return sqrt(dsys ** 2 + dzone ** 2)


# class Var:
#     def __init__(self, x, threshold, symbol):
#         self.x = x
#         self.threshold = threshold
#         self.symb_x = Symbol(symbol)
#         self.symb_threashold = Symbol("\Delta " + symbol)
#
#     def __add__(self, other):


