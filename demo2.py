
import nife
import sympy as sp

sp.init_printing()

triangle = nife.Polygon([sp.Point(0, 0), sp.Point(0, 1), sp.Point(1, 0)])


def integrator_edge(triangle, fns, body):
    return [
        body(f, e)
        for f in fns
        for e in triangle.edges
    ]


def builder1(phi, triangle, fns):
    def body(f, e):
        return sp.line_integrate(phi.expression.dot(nife.unit_normal(e)) * f,
                                 nife.segment_to_curve(e),
                                 phi.vars)
    return integrator_edge(triangle, fns, body)


def builder2(phi, triangle, fns, t):
    def body(f, e):
        return phi.eval_point(nife.segment_to_curve(e).subs(sp.Symbol("t", real=True), t)) # .dot(nife.unit_normal(e))
        #return nife.segment_to_curve(e).subs(sp.Symbol("t", real=True), t)

    return integrator_edge(triangle, fns, body)



phi = nife.Function(sp.Matrix(sp.sympify("a*x + b, a*y + c")),
                    sp.sympify("x, y"))

exprs = builder1(phi, triangle, [sp.sympify(1)])
sp.pprint(exprs)
r = nife.make_shape_functions(phi, exprs)
sp.pprint(r)

#phi = nife.Function(sp.sympify("a*x + b*y + c"), sp.sympify("x, y"))
exprs = builder2(phi, triangle, [sp.sympify(1)], 0)
sp.pprint(exprs)
r = nife.make_shape_functions(phi, exprs)
sp.pprint(r)

"""
fn = nife.Function(sp.sympify("a*x + b*y + c"), sp.sympify("x, y"))

# V rozich
exprs = [fn.eval_point(p) for p in triangle.points]
sp.pprint(nife.make_shape_functions(fn, exprs))

# Integral pres hranu
exprs = [fn.line_itegrate(nife.segment_to_curve(e)) for e in triangle.edges]
sp.pprint(nife.make_shape_functions(fn, exprs))

# RT
phi = nife.Function(sp.Matrix(sp.sympify("a*x + b, a*y + c")),
                    sp.sympify("x, y"))

exprs = [sp.line_integrate(phi.expression.dot(nife.unit_normal(e)),
                           nife.segment_to_curve(e),
                           phi.vars)
         for e in triangle.edges]
sp.pprint(nife.make_shape_functions(phi, exprs))
"""

