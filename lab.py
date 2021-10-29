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


class Formula:
    def __init__(self, symbol):
        self.symbol = symbol
        self.value = {}
        self.__buf1 = []
        self.thresholds = {}
        self.__buf2 = []
        self.symbols = []
        self.__count = 0
        self.formula = ""
        self.__thresholds_formula = ""
        self.__threshold = 0

    def add(self, symbol, value, threshold):
        self.__count += 1
        self.symbols.append(symbol)
        self.__buf1.append(value)
        self.value = {self.symbols[i]:  self.__buf1[i] for i in range(self.__count)}
        self.__buf2.append(threshold)
        self.thresholds = {self.symbols[i]: self.__buf2[i] for i in range(self.__count)}

    def count(self):
        form = simplify(self.formula)
        return form.evalf(subs=self.value)

    def get_tex(self):
        return self.symbol + " = " +  latex(simplify(self.formula))

    def recount_threshold(self):
        els = ""
        res = 0
        for i in range(self.__count):
            el = diff(self.formula, self.symbols[i])
            d = Symbol("\Delta " + self.symbols[i])
            el *= d
            ev_subs = self.value
            ev_subs[d] = self.thresholds[self.symbols[i]]
            ev_val = el.evalf(subs=ev_subs)
            s1 = Symbol("(" + latex(el) + ")")
            ev_val **= 2
            s1 **= 2
            res += ev_val
            if i == 0:
                els = s1
            else:
                els += s1
        els = sqrt(els)
        self.__threshold = sqrt(res)
        self.__thresholds_formula = els

    def get_tex_threshold(self):
        return "\Delta " + self.symbol + " = " + latex(self.__thresholds_formula)

    def threshold(self):
        return self.__threshold

    def get_all(self):
        print("Value", self.count())
        print("Latex", self.get_tex())
        print()
        self.recount_threshold()
        print("Threshold", self.threshold())
        print("Latex", self.get_tex_threshold())