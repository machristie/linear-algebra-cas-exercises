# coding: utf-8

# a
solve([
3*x + 6*y - 18,
x + 2*y - 6
])
# {x: -2⋅y + 6}

# b
solve([
x + y - 1,
x - y + 1
])
# {x: 0, y: 1}

# c
x1, x2, x3 = symbols('x1 x2 x3')
solve([
x1 + x3 - 4,
x1 - x2 + 2*x3 -5,
4*x1 - x2 + 5*x3 - 17
])
# {x₁: -x₃ + 4, x₂: x₃ - 1}

# d
from sympy.abc import a, b, c
solve([
2*a + b - c - 2,
2*a + c - 3,
a - b
])
# {a: 1, b: 1, c: 1}

# e
solve([
x + 2*y - z - 3,
2*x + y + w - 4,
x - y + z + w - 1
])
# {w: 3⋅y - 2⋅z - 2, x: -2⋅y + z + 3}

# f
solve([
x + z + w - 4,
2*x + y - w - 2,
3*x + y + z - 7
])
# No solution
