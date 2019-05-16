
def fib(X):
    if X == 1:
        return 1
    if X == 2:
        return 1
    if X >= 3:
        return fib(X - 1) + fib(X - 2)
"""
# EXPECTED VALUES - TEST CASES FOR fib
print(fib(1) == 1)
print(fib(2) == 1)
print(fib(6) == 8)
"""
"""
This now works! It's as simple as:
1. fibSum(X) - Enter the number that coorisponds to the position in fib where you want to start as X
2. fibSum(X) will take that number, and using fib(), calculate the value of that position
3. fibSum(X) will then add that value to the value before it by taking 1 away from X before the recursion
4. Once X becomes < 1 then fibSum(X) will return 0 and the total sum of all the positions of fib will be calculated
"""
def fibSum(Y):
    if Y >= 1:
        #return fib(Y) + fibSum(Y - 1)
        return str(fib(Y)) + "+" + str(fibSum(Y - 1))
    else:
        #return 0
        return "0"
"""
# EXPECTED VALUES - TEST CASES FOR fibSum
print(fibSum(1) == 1) # 1
print(fibSum(3) == 4) # 1 + 1 + 2
print(fibSum(8) == 54) # 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21
"""

fib(12)
print (fib(12))
"""
fibSum(12)
print (fibSum(12))
"""