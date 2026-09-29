# geometry.py - 2D geometry area formulas in pure Python
# No external libraries or standard modules used.

PI = 3.141592653589793


def _to_pos_float(val, label):
    """Small helper to ensure inputs are positive numbers."""
    try:
        f = float(val)
    except (TypeError, ValueError):
        raise TypeError(f"{label} must be numeric, got {type(val).__name__}")
    if f <= 0:
        raise ValueError(f"{label} must be > 0 (got {val})")
    return f


class Circle:
    """Circle area: pi * r^2"""
    def __init__(self, r):
        self.r = _to_pos_float(r, "radius")

    def area(self):
        return PI * self.r * self.r

    def __str__(self):
        return f"Circle(r={self.r})"


class Rectangle:
    """Rectangle area: width * height"""
    def __init__(self, width, height):
        self.w = _to_pos_float(width, "width")
        self.h = _to_pos_float(height, "height")

    def area(self):
        return self.w * self.h

    def __str__(self):
        return f"Rectangle(w={self.w}, h={self.h})"


class Square(Rectangle):
    """Square area: side^2"""
    def __init__(self, side):
        s = _to_pos_float(side, "side")
        super().__init__(s, s)
        self.side = s

    def __str__(self):
        return f"Square(side={self.side})"


class Triangle:
    """Triangle area using base and perpendicular height: 0.5 * b * h"""
    def __init__(self, base, height):
        self.base = _to_pos_float(base, "base")
        self.height = _to_pos_float(height, "height")

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Triangle(base={self.base}, height={self.height})"


class TriangleHeron:
    """
    Triangle area from 3 side lengths using Heron's formula:
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    """
    def __init__(self, a, b, c):
        self.a = _to_pos_float(a, "side a")
        self.b = _to_pos_float(b, "side b")
        self.c = _to_pos_float(c, "side c")

        # Triangle inequality theorem: sum of any 2 sides must exceed the 3rd
        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            raise ValueError(f"Sides {self.a}, {self.b}, {self.c} cannot form a valid triangle")

    def semi_perimeter(self):
        return (self.a + self.b + self.c) / 2.0

    def area(self):
        s = self.semi_perimeter()
        radicand = s * (s - self.a) * (s - self.b) * (s - self.c)
        # Using base Python ** 0.5 instead of importing math.sqrt
        return radicand ** 0.5

    def __str__(self):
        return f"TriangleHeron(a={self.a}, b={self.b}, c={self.c})"


class Trapezoid:
    """Trapezoid area: ((a + b) / 2) * h"""
    def __init__(self, top_base, bottom_base, height):
        self.a = _to_pos_float(top_base, "top base")
        self.b = _to_pos_float(bottom_base, "bottom base")
        self.h = _to_pos_float(height, "height")

    def area(self):
        return 0.5 * (self.a + self.b) * self.h

    def __str__(self):
        return f"Trapezoid(a={self.a}, b={self.b}, h={self.h})"


class Parallelogram:
    """Parallelogram area: base * height"""
    def __init__(self, base, height):
        self.base = _to_pos_float(base, "base")
        self.height = _to_pos_float(height, "height")

    def area(self):
        return self.base * self.height

    def __str__(self):
        return f"Parallelogram(base={self.base}, height={self.height})"


class Rhombus:
    """Rhombus area from diagonals: (d1 * d2) / 2"""
    def __init__(self, d1, d2):
        self.d1 = _to_pos_float(d1, "d1")
        self.d2 = _to_pos_float(d2, "d2")

    def area(self):
        return (self.d1 * self.d2) / 2.0

    def __str__(self):
        return f"Rhombus(d1={self.d1}, d2={self.d2})"


class Ellipse:
    """Ellipse area: pi * a * b"""
    def __init__(self, semi_major, semi_minor):
        self.a = _to_pos_float(semi_major, "semi-major")
        self.b = _to_pos_float(semi_minor, "semi-minor")

    def area(self):
        return PI * self.a * self.b

    def __str__(self):
        return f"Ellipse(a={self.a}, b={self.b})"


class Sector:
    """Circular sector area: (angle / 360) * pi * r^2"""
    def __init__(self, radius, angle_deg):
        self.r = _to_pos_float(radius, "radius")
        try:
            deg = float(angle_deg)
        except (TypeError, ValueError):
            raise TypeError("angle_deg must be numeric")
        if not (0 < deg <= 360):
            raise ValueError(f"angle_deg must be between 0 and 360, got {angle_deg}")
        self.angle_deg = deg

    def area(self):
        return (self.angle_deg / 360.0) * PI * (self.r ** 2)

    def __str__(self):
        return f"Sector(r={self.r}, deg={self.angle_deg})"

