# coding: utf-8
from sympy.abc import a, b, c, d, p, q, x, y
solve([
a*x + c*y - p,
b*x + d*y - q
], x , y)
# ⎧   -c⋅q + d⋅p     a⋅q - b⋅p⎫
# ⎨x: ──────────, y: ─────────⎬
# ⎩   a⋅d - b⋅c      a⋅d - b⋅c⎭

