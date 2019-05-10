

"""
def fibSum(N):
    if N == 1:
        return 1
    else:
        return 0
    if N == (N + 1):


def fib2():
    X = 1
    Y = X + X
    Z = X + Y
"""

def fib(X):
    #N = (X - 1) + (X - 2)
    if X == 1:
        return 1
    if X == 2:
        return 1
    if X == 3:
        return fib(X - 1) + 1





# EXPECTED VALUES - TEST CASES
print(fib(1) == 1)
print(fib(2) == 1)
print(fib(6) == 8)

"""
print(fibSum(1) == 1) # 1
print(fibSum(3) == 4) # 1 + 1 + 2
print(fibSum(8) == 54) # 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21
"""
fib(3)