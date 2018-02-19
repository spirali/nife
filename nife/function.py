import sympy as sp
import itertools
from functools import reduce
import operator


class Function:

    def __init__(self, expression, vars):
        self.expression = expression
        self.vars = vars

    def eval_point(self, point):
        assert len(point) == len(self.vars)
        print("BEFORE", self.expression, point, self.vars, list(zip(self.vars, point)))
        print("AFTER",  self.expression.subs(list(zip(self.vars, point))))
        return self.expression.subs(list(zip(self.vars, point)))

    @property
    def params(self):
        return self.expression.free_symbols.difference(self.vars)

    def line_itegrate(self, curve):
        return sp.line_integrate(self.expression, curve, self.vars)


def polynom(degree, variables, coef_prefix="a"):
    i = 1
    result = []
    variables = [sp.sympify(v) for v in variables]
    for d in range(degree, -1, -1):
        for v in itertools.combinations_with_replacement(variables, d):
            result.append(reduce(operator.mul,
                                 v,
                                 sp.Symbol("{}_{}".format(coef_prefix, i))))
            i += 1
    return sum(result)
