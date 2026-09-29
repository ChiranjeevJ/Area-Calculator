from geometry import (
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


print("--- 2D Shape Area Calculations ---\n")

# 1. Circle
radius = float(input("Enter radius of circle: "))
c = Circle(radius)
print("The circle's with radius,", radius, "has an area of", f"{c.area():.4f}", "\n")

# 2. Rectangle
rect_w = float(input("Enter width of rectangle: "))
rect_h = float(input("Enter height of rectangle: "))
rect = Rectangle(rect_w, rect_h)
print("The rectangle with width,", rect_w, "and height,", rect_h, "has an area of", f"{rect.area():.2f}", "\n")

# 3. Square
side = float(input("Enter side length of square: "))
sq = Square(side)
print("The square with side,", side, "has an area of", f"{sq.area():.2f}", "\n")

# 4. Standard Triangle
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
tri_basic = Triangle(base, height)
print("The triangle with base,", base, "and height,", height, "has an area of", f"{tri_basic.area():.2f}", "\n")

# 5. Heron's Triangle (from 3 sides)
print("Heron's Formula Triangle:")
a = float(input("  Enter side a: "))
b = float(input("  Enter side b: "))
c = float(input("  Enter side c: "))
tri_heron = TriangleHeron(a, b, c)
print("The triangle with sides,", a, ",", b, "and", c, "has an area of", f"{tri_heron.area():.2f}", "\n")

# 6. Common Quadrilaterals
b1 = float(input("Enter 1st base of trapezoid: "))
b2 = float(input("Enter 2nd base of trapezoid: "))
trap_h = float(input("Enter height of trapezoid: "))
trap = Trapezoid(b1, b2, trap_h)
print("The trapezoid with bases,", b1, "and", b2, "and height,", trap_h, "has an area of", f"{trap.area():.2f}", "\n")

plg_b = float(input("Enter base of parallelogram: "))
plg_h = float(input("Enter height of parallelogram: "))
plg = Parallelogram(plg_b, plg_h)
print("The parallelogram with base,", plg_b, "and height,", plg_h, "has an area of", f"{plg.area():.2f}", "\n")

rh_d1 = float(input("Enter 1st diagonal of rhombus: "))
rh_d2 = float(input("Enter 2nd diagonal of rhombus: "))
rh = Rhombus(rh_d1, rh_d2)
print("The rhombus with diagonals,", rh_d1, "and", rh_d2, "has an area of", f"{rh.area():.2f}", "\n")

# 7. Curved Shapes
el_a = float(input("Enter semi-major axis of ellipse: "))
el_b = float(input("Enter semi-minor axis of ellipse: "))
el = Ellipse(el_a, el_b)
print("The ellipse with semi-major axis,", el_a, "and semi-minor axis,", el_b, "has an area of", f"{el.area():.4f}", "\n")

sec_r = float(input("Enter radius of sector: "))
sec_deg = float(input("Enter angle of sector (degrees): "))
sec = Sector(sec_r, sec_deg)
print("The sector with radius,", sec_r, "and angle,", sec_deg, "has an area of", f"{sec.area():.4f}", "\n")

print("--- All calculations complete! ---")