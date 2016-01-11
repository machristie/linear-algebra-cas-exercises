# coding: utf-8

# a
solve([2*x + 2*y - 5, x - 4*y])
# {x: 2, y: 1/2}

# b
solve([-x + y - 1, x + y - 2])
# {x: 1/2, y: 3/2}

# c
solve([x - 3*y + z - 1, x + y + 2*z - 14])
#⎧     7⋅z   43       z   13⎫
#⎨x: - ─── + ──, y: - ─ + ──⎬
#⎩      4    4        4   4 ⎭

# d
solve([-x - y - 1, -3*x - 3*y - 2])
# No solution

# e
solve([
4*y + z - 20,
2*x - 2*y + z,
x + z - 5,
x + y - z - 10
])
# [{x: 5, y: 5, z: 0}]

# f
from sympy.abc import w
solve([
2*x + z + w - 5,
y - w + 1,
3*x - z - w,
4*x + y + 2*z + w - 9
])
# {w: -z + 3, x: 1, y: -z + 2}
