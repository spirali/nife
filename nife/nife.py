import sympy as sp


def make_shape_functions(fn, exprs):
    params = fn.params
    result = []
    for i, e in enumerate(exprs):
        es = exprs[:]
        es[i] = e - 1
        solution = sp.solve(es, params)
        result.append(fn.expression.subs(solution))
    return result
