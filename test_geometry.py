# test_geometry.py - Verification checks using base python assertions

from geometry import (
    PI,
    Circle,
    Rectangle,
    Square,
    Triangle,
    TriangleHeron,
    Trapezoid,
    Parallelogram,
    Rhombus,
    Ellipse,
    Sector,
)


def close_enough(a, b, tol=1e-6):
    return abs(a - b) < tol



# Circle
c = Circle(4)
assert close_enough(c.area(), PI * 16), "circle area error"

# Rectangle & Square
r = Rectangle(3.5, 2.0)
assert close_enough(r.area(), 7.0), "rectangle area error"
sq = Square(5.0)
assert close_enough(sq.area(), 25.0), "square area error"

# Triangles
t = Triangle(8, 5)
assert close_enough(t.area(), 20.0), "triangle area error"

# 3-4-5 right triangle area is 6.0
th = TriangleHeron(3, 4, 5)
assert close_enough(th.semi_perimeter(), 6.0)
assert close_enough(th.area(), 6.0), "heron formula error on 3-4-5 triangle"

# Quadrilaterals
trap = Trapezoid(4.0, 6.0, 3.0)
assert close_enough(trap.area(), 15.0), "trapezoid area error"

plg = Parallelogram(10, 4)
assert close_enough(plg.area(), 40.0), "parallelogram area error"

rh = Rhombus(6, 8)
assert close_enough(rh.area(), 24.0), "rhombus area error"

# Ellipse & Sector
el = Ellipse(4, 2)
assert close_enough(el.area(), PI * 8), "ellipse area error"

sec = Sector(3, 180)  # semi-circle: 0.5 * PI * 9
assert close_enough(sec.area(), 4.5 * PI), "sector area error"

# Bad inputs
caught = 0
try:
    Circle(-1)
except ValueError:
    caught += 1

try:
    TriangleHeron(1, 2, 10)  # impossible triangle
except ValueError:
    caught += 1

try:
     Sector(4, 450)  # angle out of bounds
except ValueError:
    caught += 1

assert caught == 3, f"Expected 3 caught exceptions, got {caught}"

print("All tests passed!")