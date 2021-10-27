import sympy
x = sympy.Symbol('x')
s = sympy.diff(x**3, x)
print(sympy.latex(sympy.sympify(s)))