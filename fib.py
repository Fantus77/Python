"""
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
#This doesn't work...need to figure out proper formula still
def fibSum(Y):
    #N = fibSum(??) ?+? fibSum(??)
    if Y == 1:
        return 1
    if Y == 3:
        return 4
    if Y >= 3:
        return fibSum(Y - 1) + fibSum(Y - 2) #Is it the same as fib? I think it has to do more with adding positions together...but how to describe that in the formula?



# EXPECTED VALUES - TEST CASES FOR fibSum
print(fibSum(1) == 1) # 1
print(fibSum(3) == 4) # 1 + 1 + 2
print(fibSum(8) == 54) # 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21


#fib(6)
fibSum(35)
