from sympy.abc import h, i, j, k

# coding: utf-8
A1a = Matrix([
[40,15],
[-50,25]])
u1a = Matrix(2,1,[100,50])
A1a.LUsolve(u1a)

A1b = Matrix([
[7*h,0,-7*j,0],
[8*h,1*i,-5*j,-2*k],
[0,1*i,-3*j,0],
[0,3*i,-6*j,-1*k]])
u1b = Matrix(4,1,[0,0,0,0])
#A1b.LUsolve(u1b)
# This gives an error. How to handle free variables with sympy?

# Use the equation solver instead
# Note that it looks like Sympy has a real linear system solver in master but
# it hasn't been release yet
# (https://github.com/sympy/sympy/pull/9438/files)
solve([7*h - 7*j, 8*h + i - 5*j - 2*k, i-3*j, 3*i - 6*j - k])
