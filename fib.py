
def fib(X):
    #N = (X - 1) + (X - 2)
    if X == 1:
        return 1
    if X == 2:
        return 1
    if X >= 3:
        return fib(X - 1) + fib(X - 2)

# EXPECTED VALUES - TEST CASES FOR fib
print(fib(1) == 1)
print(fib(2) == 1)
print(fib(6) == 8)

"""
def fibSum(Y):
    #N = ??
    if X == 1:
        return 1
    if X == 2:
        return 1
    if X >= 3:
        return 
"""

"""
# EXPECTED VALUES - TEST CASES FOR fibSum
print(fibSum(1) == 1) # 1
print(fibSum(3) == 4) # 1 + 1 + 2
print(fibSum(8) == 54) # 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21
"""
fib(6)
#fibSum()
