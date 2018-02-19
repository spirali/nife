
import nife
import sympy as sp

sp.init_printing()

triangle = nife.Polygon([sp.Point(0, 0), sp.Point(0, 1), sp.Point(1, 0)])
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
