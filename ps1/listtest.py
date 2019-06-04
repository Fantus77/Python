"""
This is where I start to mess around with lists
"""

lst = list(range(1, 101))
# val = 14
def FindBest(lst):
    lstlen = len(lst)
    fun = lst[0:lstlen - 50]
    print(fun)


FindBest(lst)