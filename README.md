# 2D Geometry Area Suite

A lightweight Python suite for calculating the area of various 2D geometric shapes based on their standard mathematical formulas.

Written in pure Python with zero dependencies—no external packages, and no standard library modules (not even `math`).

---

## Supported Shapes & Formulas

- **Circle**: `pi * r^2`
- **Rectangle**: `width * height`
- **Square**: `side^2`
- **Triangle**: `0.5 * base * height`
- **Heron's Triangle**: `sqrt(s * (s-a) * (s-b) * (s-c))` where `s = (a+b+c)/2` (implemented with `** 0.5`)
- **Trapezoid**: `((a + b) / 2) * height`
- **Parallelogram**: `base * height`
- **Rhombus**: `(d1 * d2) / 2`
- **Ellipse**: `pi * a * b`
- **Circular Sector**: `(angle / 360) * pi * r^2`

---

## Project Structure

```text
geometry_suite/
├── geometry.py         # Shape classes and area formulas
├── main.py             # Demonstration script with debug breakpoints
└── README.md
```
