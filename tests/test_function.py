from nife.function import polynom
import sympy as sp


def test_polynom():
    assert sp.sympify("x * b_1 + b_2") == polynom(1, ("x",), "b")
    assert sp.sympify("x**3*b_1 + x**2*b_2 + x*b_3 + b_4") \
        == polynom(3, ("x",), "b")
    assert sp.sympify("b_1*x**2 + b_2*x*y + b_3*y**2 + b_4*x + b_5*y + b_6") \
        == polynom(2, ("x", "y"), "b")
