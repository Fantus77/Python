"""
while expA:
    expB

# where expA is a boolean expression that evalues to true
# expB is any expression

for var in range(int, int):
    expA

# where var is a variable that will be assigned a value
# where range takes two ints
# where expA will evaluate
# during each loop iteration var will be assigned the next integer value in the range
# then the expA will execute

More generic for each style loop

for var in list:
    expA
"""

"""
For variable in this string. Print that variable
"""
def Example1():
    string1 = "Hello Jay"
    for character in string1:
        print(character)


def Example2():
    lst  = [123, 2, 3, 4, 5]
    for item in lst:
        print(item)

def Example3():
    for value in range(25, 29):
        print(value)


Example1()
print('\n')
Example2()
print('\n')
Example3()