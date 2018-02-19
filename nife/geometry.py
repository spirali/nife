import sympy as sp


def segment_to_curve(line):
    t = sp.Symbol("t", real=True)
    return sp.Curve(line.arbitrary_point(t), (t, 0, 1))


def unit_normal(line):
    a, b = line.points
    c = b - a
    return sp.Matrix((-c[1], c[0])).normalized()


"""
def to_curve(obj):
    if isinstance(obj, sp.Curve):
        return obj
    if isinstance(obj, sp.Segment):
        return segment_to_curve(obj)
    raise Exception("Cannot convert {!r} to curve".format(obj))
"""


class Polygon:

    def __init__(self, points):
        self.points = tuple(points)
        assert len(self.points) > 2

    @property
    def edges(self):
        for i in range(len(self.points) - 1):
            yield sp.Line(self.points[i], self.points[i + 1])
        yield sp.Line(self.points[-1], self.points[0])

    @property
    def normals(self):
        for edge in self.edges:
            yield unit_normal(edge)
