from sympy import *
import pandas as pd
# pip install --user pandas
# pip install --user openpyxl xlsxwriter xlrd
# pip install --user sympy


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
        self.__value = {}
        self.__buf1 = []
        self.__thresholds = {}
        self.__buf2 = []
        self.__symbols = []
        self.__count = 0
        self.formula = ""
        self.__thresholds_formula = ""
        self.threshold_value = 0
        self.result_value = 0
        self.__exel = {}
        self.__exel[self.symbol] = []
        self.__exel["d" + self.symbol] = []

    def add(self, symbol, value, threshold):
        self.__count += 1
        self.__symbols.append(symbol)
        self.__buf1.append(value)
        self.__value = {self.__symbols[i]:  self.__buf1[i] for i in range(self.__count)}
        self.__buf2.append(threshold)
        self.__thresholds = {self.__symbols[i]: self.__buf2[i] for i in range(self.__count)}
        self.__exel[symbol] = []
        self.__exel["d" + symbol] = []

    def count(self):
        form = simplify(self.formula)
        self.result_value = form.evalf(subs=self.__value)

    def rewrite_values(self, vals):
        self.__buf1 = vals
        self.__value = {self.__symbols[i]:  vals[i] for i in range(self.__count)}
        self.count()

    def rewrite_thresholds(self, vals):
        self.__buf2 = vals
        self.__thresholds = {self.__symbols[i]: vals[i] for i in range(self.__count)}
        self.count_threshold()

    def get_tex(self):
        return self.symbol + " = " + latex(simplify(self.formula))

    def count_threshold(self):
        els = ""
        res = 0
        for i in range(self.__count):
            el = diff(self.formula, self.__symbols[i])
            d = Symbol("\Delta " + self.__symbols[i])
            el *= d
            ev_subs = self.__value
            ev_subs[d] = self.__thresholds[self.__symbols[i]]
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
        self.threshold_value = sqrt(res)
        self.__thresholds_formula = els

    def count_all(self):
        self.count()
        self.count_threshold()

    def get_tex_threshold(self):
        return "\Delta " + self.symbol + " = " + latex(self.__thresholds_formula)

    def print_all_tex(self):
        print("Formula:", self.get_tex())
        print()
        print("Threshold:", self.get_tex_threshold())

    def add_to_exel(self):
        for i in range(self.__count):
            self.__exel[self.__symbols[i]].append(self.__buf1[i])
            self.__exel["d" + self.__symbols[i]].append(self.__buf2[i])
        self.__exel[self.symbol].append(self.result_value)
        self.__exel["d" + self.symbol].append(self.threshold_value)

    def write_excel(self, file_name):
        df = pd.DataFrame(self.__exel)
        df.to_excel('./' + file_name + '.xlsx')